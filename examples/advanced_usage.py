#!/usr/bin/env python3
from advanced_steg_analysis import AdvancedStegAssimilator
from steg_visualization_enhanced import EnhancedStegVisualizer
from steg_deobfuscation import StegDeobfuscator
import json
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_with_custom_thresholds(image_path, thresholds):
    """Analyze image with custom detection thresholds."""
    analyzer = AdvancedStegAssimilator(
        output_dir="custom_threshold_results",
        verbose=True,
        detection_threshold=thresholds["general"]
    )
    
    # Update analyzer thresholds
    analyzer.thresholds.update(thresholds)
    
    # Perform analysis
    results = analyzer.analyze_file(image_path)
    
    # Generate enhanced visualizations
    visualizer = EnhancedStegVisualizer()
    visualizer.generate_enhanced_visualizations(image_path)
    
    return results

def compare_deobfuscation_methods(image_path):
    """Compare different deobfuscation methods."""
    deobfuscator = StegDeobfuscator()
    results = {}
    
    # Apply different deobfuscation methods
    methods = [
        ("adaptive_threshold", deobfuscator.apply_adaptive_thresholding),
        ("high_pass_filter", deobfuscator.apply_high_pass_filtering),
        ("denoising", deobfuscator.apply_denoising),
        ("unsharp_masking", deobfuscator.apply_unsharp_masking),
        ("histogram_equalization", deobfuscator.apply_histogram_equalization),
        ("laplacian_pyramid", deobfuscator.apply_laplacian_pyramid),
        ("frequency_domain", deobfuscator.apply_frequency_domain_analysis)
    ]
    
    for method_name, method in methods:
        try:
            result = method(image_path)
            results[method_name] = {
                "success": True,
                "result": result
            }
        except Exception as e:
            results[method_name] = {
                "success": False,
                "error": str(e)
            }
    
    return results

def analyze_texture_patterns(image_path):
    """Analyze texture patterns in detail."""
    analyzer = AdvancedStegAssimilator(
        output_dir="texture_analysis_results",
        verbose=True
    )
    
    # Perform texture analysis
    texture_results = analyzer.analyze_texture_patterns(image_path)
    
    # Visualize texture features
    visualizer = EnhancedStegVisualizer()
    visualizer.generate_texture_visualizations(image_path, texture_results)
    
    return texture_results

def main():
    # Example image path - replace with your image
    image_path = "path/to/your/image.jpg"
    
    # Example 1: Custom threshold analysis
    print("\nPerforming custom threshold analysis...")
    custom_thresholds = {
        "general": 0.7,
        "color_anomaly": 0.6,
        "dct_anomaly": 0.75,
        "edge_anomaly": 0.65,
        "lsb_anomaly": 0.7,
        "palette_anomaly": 0.6,
        "texture_anomaly": 0.7,
        "frequency_anomaly": 0.75
    }
    threshold_results = analyze_with_custom_thresholds(image_path, custom_thresholds)
    
    # Example 2: Compare deobfuscation methods
    print("\nComparing deobfuscation methods...")
    deobfuscation_results = compare_deobfuscation_methods(image_path)
    
    # Example 3: Detailed texture analysis
    print("\nPerforming detailed texture analysis...")
    texture_results = analyze_texture_patterns(image_path)
    
    # Save all results
    results = {
        "threshold_analysis": threshold_results,
        "deobfuscation_comparison": deobfuscation_results,
        "texture_analysis": texture_results
    }
    
    with open("advanced_analysis_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\nAdvanced analysis complete. Results saved to advanced_analysis_results.json")

if __name__ == "__main__":
    main() 