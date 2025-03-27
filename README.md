# StegAssimilator

A comprehensive tool for detecting and analyzing steganography in images, featuring advanced visualization and deobfuscation capabilities.

![StegAssimilator Logo](https://via.placeholder.com/150x150?text=StegAssimilator)

## Features

### Analysis Capabilities
- Color distribution analysis
- DCT coefficient analysis
- Edge pattern detection
- LSB pattern analysis
- Color palette analysis
- Texture pattern analysis
- Channel correlation analysis
- Frequency domain analysis

### Visualization Features
- Channel comparison visualization
- Histogram analysis
- Edge detection comparison
- Frequency domain visualization
- Texture analysis visualization
- Comparison grids
- Enhanced statistical plots

### Deobfuscation Techniques
- Adaptive thresholding
- High-pass filtering
- Non-local means denoising
- Unsharp masking
- Histogram equalization
- Laplacian pyramid analysis
- Frequency domain analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/StegAssimilator.git
cd StegAssimilator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Analysis
```bash
python advanced_steg_analysis.py
```

### Custom Directory Analysis
```python
from advanced_steg_analysis import AdvancedStegAssimilator

analyzer = AdvancedStegAssimilator()
analyzer.generate_report("path/to/your/image.jpg")
```

## Output Structure

The tool generates three types of output:

1. **Analysis Reports** (`analysis_output/`)
   - JSON reports with detailed analysis
   - Statistical summaries
   - Suspicious pattern detection

2. **Enhanced Visualizations** (`enhanced_visualization_output/`)
   - Channel comparisons
   - Histogram analysis
   - Edge detection results
   - Frequency domain analysis
   - Texture analysis

3. **Deobfuscation Results** (`deobfuscation_output/`)
   - Processed images
   - Pattern detection results
   - Enhanced details

## Analysis Features

### Color Distribution Analysis
- Mean, standard deviation, skewness, kurtosis
- Channel entropy analysis
- Channel correlation detection
- Statistical anomaly detection

### DCT Analysis
- Coefficient distribution
- High-frequency component analysis
- Entropy calculation
- Pattern detection

### Edge Analysis
- Multiple edge detection methods
- Edge density calculation
- Pattern recognition
- Anomaly detection

### LSB Analysis
- Channel-wise LSB pattern analysis
- Entropy calculation
- Distribution analysis
- Anomaly detection

### Texture Analysis
- GLCM-based features
- Contrast, homogeneity, energy
- Pattern recognition
- Anomaly detection

## Visualization Features

### Channel Comparison
- RGB channel separation
- Individual channel analysis
- Correlation visualization

### Histogram Analysis
- Channel-wise histograms
- KDE overlay
- Statistical distribution

### Edge Detection
- Multiple method comparison
- Pattern visualization
- Anomaly highlighting

### Frequency Analysis
- Magnitude spectrum
- Phase spectrum
- Combined visualization

### Texture Analysis
- Contrast maps
- Homogeneity maps
- Energy maps

## Deobfuscation Techniques

### Adaptive Thresholding
- Reveals hidden patterns
- Adapts to local image characteristics
- Pattern enhancement

### High-Pass Filtering
- Highlights high-frequency components
- Reveals hidden details
- Pattern detection

### Denoising
- Non-local means denoising
- Pattern preservation
- Detail enhancement

### Unsharp Masking
- Edge enhancement
- Detail amplification
- Pattern highlighting

### Histogram Equalization
- Contrast enhancement
- Detail revelation
- Pattern visibility

### Laplacian Pyramid
- Multi-scale analysis
- Detail decomposition
- Pattern detection

### Frequency Analysis
- FFT-based analysis
- Pattern detection
- Anomaly identification

## Requirements

- Python 3.8+
- NumPy
- OpenCV
- Pillow
- SciPy
- Matplotlib
- Seaborn
- scikit-image

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV community for image processing algorithms
- SciPy team for scientific computing tools
- Matplotlib team for visualization capabilities

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. 