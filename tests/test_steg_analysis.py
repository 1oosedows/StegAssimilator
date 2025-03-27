#!/usr/bin/env python3
import unittest
import numpy as np
from pathlib import Path
import tempfile
import shutil
from advanced_steg_analysis import AdvancedStegAssimilator
from steg_visualization_enhanced import EnhancedStegVisualizer
from steg_deobfuscation import StegDeobfuscator

class TestStegAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        # Create temporary directory for test outputs
        cls.temp_dir = tempfile.mkdtemp()
        
        # Create test image
        cls.test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cls.test_image[25:75, 25:75] = 255  # White square in the middle
        cls.test_image_path = Path(cls.temp_dir) / "test_image.png"
        
        # Initialize analyzers
        cls.analyzer = AdvancedStegAssimilator(
            output_dir=str(Path(cls.temp_dir) / "analysis_results"),
            verbose=False
        )
        cls.visualizer = EnhancedStegVisualizer()
        cls.deobfuscator = StegDeobfuscator()
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment."""
        shutil.rmtree(cls.temp_dir)
    
    def test_color_distribution_analysis(self):
        """Test color distribution analysis."""
        results = self.analyzer.analyze_color_distribution(self.test_image)
        self.assertIsInstance(results, dict)
        self.assertIn("color_anomaly", results)
        self.assertIn("palette_anomaly", results)
    
    def test_dct_analysis(self):
        """Test DCT coefficient analysis."""
        results = self.analyzer.analyze_dct_coefficients(self.test_image)
        self.assertIsInstance(results, dict)
        self.assertIn("dct_anomaly", results)
    
    def test_edge_pattern_analysis(self):
        """Test edge pattern analysis."""
        results = self.analyzer.analyze_edge_patterns(self.test_image)
        self.assertIsInstance(results, dict)
        self.assertIn("edge_anomaly", results)
    
    def test_lsb_analysis(self):
        """Test LSB pattern analysis."""
        results = self.analyzer.analyze_lsb_patterns(self.test_image)
        self.assertIsInstance(results, dict)
        self.assertIn("lsb_anomaly", results)
    
    def test_texture_analysis(self):
        """Test texture pattern analysis."""
        results = self.analyzer.analyze_texture_patterns(self.test_image)
        self.assertIsInstance(results, dict)
        self.assertIn("texture_anomaly", results)
    
    def test_deobfuscation_methods(self):
        """Test deobfuscation methods."""
        # Test adaptive thresholding
        result = self.deobfuscator.apply_adaptive_thresholding(self.test_image)
        self.assertIsInstance(result, np.ndarray)
        
        # Test high-pass filtering
        result = self.deobfuscator.apply_high_pass_filtering(self.test_image)
        self.assertIsInstance(result, np.ndarray)
        
        # Test denoising
        result = self.deobfuscator.apply_denoising(self.test_image)
        self.assertIsInstance(result, np.ndarray)
    
    def test_visualization_methods(self):
        """Test visualization methods."""
        # Test channel comparison
        self.visualizer.generate_channel_comparison(self.test_image)
        
        # Test histogram comparison
        self.visualizer.generate_histogram_comparison(self.test_image)
        
        # Test edge detection comparison
        self.visualizer.generate_edge_comparison(self.test_image)
    
    def test_full_analysis(self):
        """Test complete analysis workflow."""
        results = self.analyzer.analyze_file(str(self.test_image_path))
        self.assertIsInstance(results, dict)
        self.assertIn("analysis_summary", results)
        self.assertIn("detection_probability", results)
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Test with non-existent file
        with self.assertRaises(FileNotFoundError):
            self.analyzer.analyze_file("nonexistent_file.png")
        
        # Test with invalid image data
        invalid_image = np.array([[1, 2], [3, 4]])  # 2D array instead of 3D
        with self.assertRaises(ValueError):
            self.analyzer.analyze_color_distribution(invalid_image)

if __name__ == "__main__":
    unittest.main() 