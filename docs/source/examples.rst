Examples
========

This section provides various examples demonstrating the usage of StegAnalyzer.

Basic Examples
------------

Simple Analysis
~~~~~~~~~~~~

.. code-block:: python

   from steganalyzer import AdvancedStegAnalyzer

   # Initialize analyzer
   analyzer = AdvancedStegAnalyzer(
       output_dir="basic_analysis_results",
       verbose=True
   )

   # Analyze a single image
   results = analyzer.analyze_file("image.jpg")
   print("Analysis Results:", results)

   # Generate visualizations
   analyzer.generate_visualizations("image.jpg")

Batch Processing
~~~~~~~~~~~~~

.. code-block:: python

   # Analyze multiple images
   results = analyzer.analyze_directory("images_folder")
   print("Batch Analysis Results:", results)

   # Process with progress bar
   from tqdm import tqdm
   for image_path in tqdm(Path("images_folder").glob("*.jpg")):
       results = analyzer.analyze_file(str(image_path))
       print(f"Results for {image_path.name}:", results)

Advanced Examples
--------------

Custom Threshold Analysis
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Set custom thresholds
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

   analyzer = AdvancedStegAnalyzer(
       output_dir="custom_threshold_results",
       detection_threshold=custom_thresholds["general"]
   )
   analyzer.thresholds.update(custom_thresholds)

   # Analyze with custom thresholds
   results = analyzer.analyze_file("image.jpg")
   print("Custom Threshold Results:", results)

Enhanced Visualization
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from steganalyzer import EnhancedStegVisualizer

   # Initialize visualizer
   visualizer = EnhancedStegVisualizer()

   # Generate various visualizations
   visualizer.generate_channel_comparison("image.jpg")
   visualizer.generate_histogram_comparison("image.jpg")
   visualizer.generate_edge_comparison("image.jpg")
   visualizer.generate_frequency_analysis("image.jpg")
   visualizer.generate_texture_visualizations("image.jpg")

   # Generate all enhanced visualizations
   visualizer.generate_enhanced_visualizations("image.jpg")

Deobfuscation Techniques
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from steganalyzer import StegDeobfuscator

   # Initialize deobfuscator
   deobfuscator = StegDeobfuscator()

   # Apply various deobfuscation techniques
   results = {}
   
   # Adaptive thresholding
   results["adaptive_threshold"] = deobfuscator.apply_adaptive_thresholding("image.jpg")
   
   # High-pass filtering
   results["high_pass_filter"] = deobfuscator.apply_high_pass_filtering("image.jpg")
   
   # Denoising
   results["denoising"] = deobfuscator.apply_denoising("image.jpg")
   
   # Unsharp masking
   results["unsharp_masking"] = deobfuscator.apply_unsharp_masking("image.jpg")
   
   # Histogram equalization
   results["histogram_equalization"] = deobfuscator.apply_histogram_equalization("image.jpg")
   
   # Laplacian pyramid
   results["laplacian_pyramid"] = deobfuscator.apply_laplacian_pyramid("image.jpg")
   
   # Frequency domain analysis
   results["frequency_domain"] = deobfuscator.apply_frequency_domain_analysis("image.jpg")

   print("Deobfuscation Results:", results)

Real-World Examples
----------------

Complete Analysis Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pathlib import Path
   import json
   from datetime import datetime
   from steganalyzer import (
       AdvancedStegAnalyzer,
       EnhancedStegVisualizer,
       StegDeobfuscator
   )

   def analyze_image_pipeline(image_path, output_dir):
       """Complete analysis pipeline for a single image."""
       # Create output directories
       output_dir = Path(output_dir)
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Initialize components
       analyzer = AdvancedStegAnalyzer(
           output_dir=str(output_dir / "analysis"),
           verbose=True
       )
       visualizer = EnhancedStegVisualizer()
       deobfuscator = StegDeobfuscator()
       
       # Perform analysis
       analysis_results = analyzer.analyze_file(str(image_path))
       
       # Generate visualizations
       visualizer.generate_enhanced_visualizations(str(image_path))
       
       # Apply deobfuscation
       deobfuscation_results = {}
       for method in [
           "adaptive_thresholding",
           "high_pass_filtering",
           "denoising",
           "unsharp_masking",
           "histogram_equalization",
           "laplacian_pyramid",
           "frequency_domain_analysis"
       ]:
           try:
               result = getattr(deobfuscator, f"apply_{method}")(str(image_path))
               deobfuscation_results[method] = {
                   "success": True,
                   "result": result
               }
           except Exception as e:
               deobfuscation_results[method] = {
                   "success": False,
                   "error": str(e)
               }
       
       # Combine results
       final_results = {
           "timestamp": datetime.now().isoformat(),
           "image_info": {
               "path": str(image_path),
               "size": image_path.stat().st_size,
               "format": image_path.suffix
           },
           "analysis_results": analysis_results,
           "deobfuscation_results": deobfuscation_results
       }
       
       # Save results
       with open(output_dir / "results.json", "w") as f:
           json.dump(final_results, f, indent=2)
       
       return final_results

   # Usage example
   image_path = Path("path/to/your/image.jpg")
   results = analyze_image_pipeline(image_path, "analysis_results")
   print("Pipeline Results:", results)

Batch Processing with Progress Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from concurrent.futures import ThreadPoolExecutor
   from tqdm import tqdm

   def process_directory(input_dir, output_base_dir, max_workers=4):
       """Process a directory of images with progress tracking."""
       input_dir = Path(input_dir)
       output_base_dir = Path(output_base_dir)
       
       # Get list of images
       image_files = list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png"))
       
       # Create output directory
       output_base_dir.mkdir(parents=True, exist_ok=True)
       
       # Process images with progress bar
       with ThreadPoolExecutor(max_workers=max_workers) as executor:
           futures = []
           for image_path in image_files:
               output_dir = output_base_dir / image_path.stem
               future = executor.submit(
                   analyze_image_pipeline,
                   image_path,
                   output_dir
               )
               futures.append(future)
           
           # Wait for completion with progress bar
           results = []
           for future in tqdm(
               futures,
               total=len(futures),
               desc="Processing images"
           ):
               try:
                   result = future.result()
                   results.append(result)
               except Exception as e:
                   print(f"Error processing image: {e}")
       
       return results

   # Usage example
   input_directory = "path/to/your/images"
   output_directory = "batch_analysis_results"
   results = process_directory(input_directory, output_directory)
   print(f"Processed {len(results)} images")

Error Handling and Logging
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import logging
   from pathlib import Path
   from steganalyzer import AdvancedStegAnalyzer
   from steganalyzer.exceptions import StegAnalyzerError

   # Set up logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[
           logging.FileHandler("steg_analysis.log"),
           logging.StreamHandler()
       ]
   )
   logger = logging.getLogger("steganalyzer")

   def analyze_with_error_handling(image_path):
       """Analyze image with proper error handling and logging."""
       try:
           # Initialize analyzer
           analyzer = AdvancedStegAnalyzer(
               output_dir="error_handling_results",
               verbose=True
           )
           
           # Perform analysis
           logger.info(f"Starting analysis of {image_path}")
           results = analyzer.analyze_file(str(image_path))
           
           # Log results
           logger.info(f"Analysis completed successfully: {results}")
           return results
           
       except FileNotFoundError as e:
           logger.error(f"Image file not found: {e}")
           raise
           
       except StegAnalyzerError as e:
           logger.error(f"Analysis error: {e}")
           raise
           
       except Exception as e:
           logger.error(f"Unexpected error: {e}")
           raise

   # Usage example
   try:
       results = analyze_with_error_handling("path/to/your/image.jpg")
       print("Analysis Results:", results)
   except Exception as e:
       print(f"Error during analysis: {e}") 