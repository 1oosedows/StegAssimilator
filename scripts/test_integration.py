import unittest
import os
import sys
from pathlib import Path
import json
import numpy as np
import cv2
from PIL import Image

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from steganography.analyze_image import (
    analyze_color_distribution,
    analyze_dct_coefficients,
    analyze_edge_patterns,
    analyze_lsb_patterns,
    analyze_texture_patterns,
    analyze_frequency_domain,
    analyze_bit_plane,
    analyze_noise_level,
    calculate_detection_probability
)

class TestSteganographyAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test image
        cls.test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cls.test_image[25:75, 25:75] = 255  # White square in the middle
        
        # Save the test image
        cls.test_image_path = str(Path(__file__).parent / "test_image.png")
        cv2.imwrite(cls.test_image_path, cls.test_image)

    def test_color_distribution(self):
        result = analyze_color_distribution(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('mean', result)
        self.assertIn('std', result)
        self.assertIsInstance(result['mean'], float)
        self.assertIsInstance(result['std'], float)

    def test_dct_coefficients(self):
        result = analyze_dct_coefficients(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('mean', result)
        self.assertIn('std', result)
        self.assertIsInstance(result['mean'], float)
        self.assertIsInstance(result['std'], float)

    def test_edge_patterns(self):
        result = analyze_edge_patterns(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('edge_density', result)
        self.assertIsInstance(result['edge_density'], float)

    def test_lsb_patterns(self):
        result = analyze_lsb_patterns(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('lsb_density', result)
        self.assertIsInstance(result['lsb_density'], float)

    def test_texture_patterns(self):
        result = analyze_texture_patterns(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('contrast', result)
        self.assertIsInstance(result['contrast'], float)

    def test_frequency_domain(self):
        result = analyze_frequency_domain(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('mean', result)
        self.assertIn('std', result)
        self.assertIsInstance(result['mean'], float)
        self.assertIsInstance(result['std'], float)

    def test_bit_plane(self):
        result = analyze_bit_plane(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('bit_planes', result)
        self.assertIsInstance(result['bit_planes'], list)
        self.assertEqual(len(result['bit_planes']), 8)
        self.assertTrue(all(isinstance(x, float) for x in result['bit_planes']))

    def test_noise_level(self):
        result = analyze_noise_level(self.test_image)
        self.assertIsInstance(result, dict)
        self.assertIn('noise_level', result)
        self.assertIsInstance(result['noise_level'], float)

    def test_detection_probability(self):
        results = {
            'color_distribution': {'mean': 0.5, 'std': 0.2},
            'dct_coefficients': {'mean': 0.3, 'std': 0.1},
            'edge_patterns': {'edge_density': 0.4},
            'lsb_patterns': {'lsb_density': 0.5},
            'texture_patterns': {'contrast': 0.6},
            'frequency_domain': {'mean': 0.7, 'std': 0.3},
            'bit_plane': {'bit_planes': [0.5] * 8},
            'noise_level': {'noise_level': 0.2}
        }
        probability = calculate_detection_probability(results)
        self.assertIsInstance(probability, float)
        self.assertGreaterEqual(probability, 0)
        self.assertLessEqual(probability, 1)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test image
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)

if __name__ == '__main__':
    unittest.main() 