#!/usr/bin/env python3
from advanced_steg_analysis import AdvancedStegAssimilator
from pathlib import Path

def main():
    # Initialize the analyzer
    analyzer = AdvancedStegAssimilator(
        output_dir="example_results",
        verbose=True,
        detection_threshold=0.8
    )
    
    # Example 1: Analyze a single image
    print("\nAnalyzing single image...")
    image_path = "path/to/your/image.jpg"  # Replace with your image path
    results = analyzer.analyze_file(image_path)
    print(f"Analysis results: {results}")
    
    # Example 2: Analyze a directory of images
    print("\nAnalyzing directory of images...")
    image_dir = "path/to/your/images"  # Replace with your directory path
    results = analyzer.analyze_directory(image_dir)
    print(f"Directory analysis results: {results}")
    
    # Example 3: Generate visualizations
    print("\nGenerating visualizations...")
    analyzer.generate_visualizations(image_path)
    
    # Example 4: Apply deobfuscation
    print("\nApplying deobfuscation techniques...")
    analyzer.apply_deobfuscation(image_path)

if __name__ == "__main__":
    main() 