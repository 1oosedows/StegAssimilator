#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from advanced_steg_analysis import AdvancedStegAssimilator

def main():
    parser = argparse.ArgumentParser(description="Advanced Steganography Analysis Tool")
    parser.add_argument("input", help="Input image file or directory to analyze")
    parser.add_argument("--output", "-o", help="Output directory for results", default="analysis_results")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--threshold", "-t", type=float, default=0.8,
                      help="Detection threshold (0.0-1.0, default: 0.8)")
    parser.add_argument("--visualize", action="store_true", help="Generate visualizations")
    parser.add_argument("--deobfuscate", action="store_true", help="Apply deobfuscation techniques")
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize analyzer
    analyzer = AdvancedStegAssimilator(
        output_dir=str(output_dir),
        verbose=args.verbose,
        detection_threshold=args.threshold
    )
    
    # Process input
    input_path = Path(args.input)
    if input_path.is_file():
        # Single file analysis
        try:
            results = analyzer.analyze_file(str(input_path))
            if args.visualize:
                analyzer.generate_visualizations(str(input_path))
            if args.deobfuscate:
                analyzer.apply_deobfuscation(str(input_path))
            print(f"\nAnalysis complete. Results saved to: {output_dir}")
        except Exception as e:
            print(f"Error analyzing file: {e}", file=sys.stderr)
            sys.exit(1)
    elif input_path.is_dir():
        # Directory analysis
        try:
            results = analyzer.analyze_directory(str(input_path))
            print(f"\nAnalysis complete. Results saved to: {output_dir}")
        except Exception as e:
            print(f"Error analyzing directory: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Error: Input path '{args.input}' does not exist", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 