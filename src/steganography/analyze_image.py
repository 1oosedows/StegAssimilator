import sys
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Union
import numpy as np
import cv2
from PIL import Image
from scipy import fftpack
from skimage import feature
import io

def analyze_color_distribution(image: np.ndarray) -> Dict[str, float]:
    # Convert to RGB if needed
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Calculate color histogram 
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX).flatten()
    
    # Calculate histogram statistics
    mean = float(np.mean(hist))
    std = float(np.std(hist))
    
    return {"mean": mean, "std": std}

def analyze_dct_coefficients(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply 2D DCT
    dct = fftpack.dct(fftpack.dct(image.T, norm='ortho').T, norm='ortho')
    
    # Calculate DCT statistics
    mean = float(np.mean(np.abs(dct)))
    std = float(np.std(np.abs(dct)))
    
    return {"mean": mean, "std": std}

def analyze_edge_patterns(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Calculate edge features
    edges = feature.canny(image, sigma=2)
    edge_density = float(np.mean(edges))
    
    return {"edge_density": edge_density}

def analyze_lsb_patterns(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Extract LSB plane
    lsb = image & 1
    lsb_density = float(np.mean(lsb))
    
    return {"lsb_density": lsb_density}

def analyze_texture_patterns(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Calculate GLCM features
    glcm = feature.graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
    contrast = feature.graycoprops(glcm, 'contrast')[0]
    
    return {"contrast": float(np.mean(contrast))}

def analyze_frequency_domain(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Calculate FFT
    fft = np.fft.fft2(image)
    fft_shift = np.fft.fftshift(fft)
    magnitude = np.abs(fft_shift)
    
    # Calculate frequency statistics
    mean = float(np.mean(magnitude))
    std = float(np.std(magnitude))
    
    return {"mean": mean, "std": std}

def analyze_bit_plane(image: np.ndarray) -> Dict[str, List[float]]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Analyze bit planes
    bit_planes = []
    for i in range(8):
        plane = (image >> i) & 1
        bit_planes.append(float(np.mean(plane)))
    
    return {"bit_planes": bit_planes}

def analyze_noise_level(image: np.ndarray) -> Dict[str, float]:
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Calculate noise level using Laplacian variance
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    noise_level = float(np.var(laplacian))
    
    return {"noise_level": noise_level}

def calculate_detection_probability(results: Dict[str, Dict[str, Union[float, List[float]]]]) -> float:
    # Weight different analysis results
    weights = {
        'color_distribution': 0.15,
        'dct_coefficients': 0.2,
        'edge_patterns': 0.15,
        'lsb_patterns': 0.2,
        'texture_patterns': 0.1,
        'frequency_domain': 0.1,
        'bit_plane': 0.05,
        'noise_level': 0.05
    }
    
    # Calculate weighted probability
    probability = 0
    for key, weight in weights.items():
        if key in results:
            # Get the mean value from the result dictionary
            if isinstance(results[key], dict):
                values = list(results[key].values())
                if values:
                    value = values[0]
                    if isinstance(value, list):
                        # For lists (like bit_planes), use the mean of the list
                        value = float(np.mean(value))
                    else:
                        value = float(value)
                    probability += weight * value
    
    return min(1.0, probability)

def main() -> None:
    if len(sys.argv) != 2:
        print(json.dumps({'error': 'Invalid number of arguments'}))
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    try:
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError('Failed to read image')
        
        # Convert BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Perform analysis
        results = {
            'color_distribution': analyze_color_distribution(image),
            'dct_coefficients': analyze_dct_coefficients(image),
            'edge_patterns': analyze_edge_patterns(image),
            'lsb_patterns': analyze_lsb_patterns(image),
            'texture_patterns': analyze_texture_patterns(image),
            'frequency_domain': analyze_frequency_domain(image),
            'bit_plane': analyze_bit_plane(image),
            'noise_level': analyze_noise_level(image)
        }
        
        # Calculate detection probability
        detection_probability = calculate_detection_probability(results)
        
        # Generate analysis summary
        if detection_probability > 0.7:
            summary = "High probability of hidden information detected"
        elif detection_probability > 0.4:
            summary = "Moderate probability of hidden information detected"
        else:
            summary = "Low probability of hidden information detected"
        
        # Add probability and summary to results
        results['detection_probability'] = detection_probability
        results['analysis_summary'] = summary
        
        print(json.dumps(results))
        
    except Exception as e:
        print(json.dumps({'error': str(e)}))
        sys.exit(1)

if __name__ == '__main__':
    main() 