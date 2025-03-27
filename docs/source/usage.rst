Usage Guide
==========

This guide covers the basic and advanced usage of StegAnalyzer.

Basic Usage
----------

Analyzing a Single Image
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from steganalyzer import AdvancedStegAnalyzer

   # Initialize the analyzer
   analyzer = AdvancedStegAnalyzer(
       output_dir="analysis_results",
       verbose=True
   )

   # Analyze a single image
   results = analyzer.analyze_file("image.jpg")
   print(results)

Analyzing Multiple Images
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Analyze all images in a directory
   results = analyzer.analyze_directory("images_folder")
   print(results)

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Basic analysis
   steganalyzer image.jpg

   # With visualization and deobfuscation
   steganalyzer image.jpg --visualize --deobfuscate

   # Custom output directory
   steganalyzer image.jpg -o custom_output

   # Verbose output
   steganalyzer image.jpg -v

Advanced Usage
------------

Custom Detection Thresholds
~~~~~~~~~~~~~~~~~~~~~~~~~

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

Enhanced Visualizations
~~~~~~~~~~~~~~~~~~~~~

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

Deobfuscation Techniques
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from steganalyzer import StegDeobfuscator

   # Initialize deobfuscator
   deobfuscator = StegDeobfuscator()

   # Apply various deobfuscation techniques
   deobfuscator.apply_adaptive_thresholding("image.jpg")
   deobfuscator.apply_high_pass_filtering("image.jpg")
   deobfuscator.apply_denoising("image.jpg")
   deobfuscator.apply_unsharp_masking("image.jpg")
   deobfuscator.apply_histogram_equalization("image.jpg")
   deobfuscator.apply_laplacian_pyramid("image.jpg")
   deobfuscator.apply_frequency_domain_analysis("image.jpg")

Output Structure
--------------

The analysis results are organized as follows:

.. code-block:: text

   analysis_results/
   ├── analysis_reports/
   │   └── image_analysis.json
   ├── visualization_output/
   │   ├── channel_comparison.png
   │   ├── histogram_comparison.png
   │   └── edge_comparison.png
   ├── enhanced_visualization_output/
   │   ├── frequency_analysis.png
   │   └── texture_analysis.png
   └── deobfuscation_output/
       ├── adaptive_threshold.png
       ├── high_pass_filter.png
       └── denoising.png

Analysis Report Format
~~~~~~~~~~~~~~~~~~~~

The analysis report (JSON format) includes:

.. code-block:: json

   {
     "file_info": {
       "filename": "image.jpg",
       "size": 1234567,
       "dimensions": [800, 600],
       "format": "JPEG"
     },
     "analysis_summary": {
       "detection_probability": 0.85,
       "analysis_timestamp": "2024-02-13T20:39:52"
     },
     "detailed_results": {
       "color_analysis": {
         "color_anomaly": 0.7,
         "palette_anomaly": 0.65
       },
       "dct_analysis": {
         "dct_anomaly": 0.75
       },
       "edge_analysis": {
         "edge_anomaly": 0.6
       },
       "lsb_analysis": {
         "lsb_anomaly": 0.7
       },
       "texture_analysis": {
         "texture_anomaly": 0.8
       }
     }
   }

Best Practices
------------

1. Image Preparation
   ^^^^^^^^^^^^^^^^

   * Use high-quality images for better analysis
   * Ensure images are in a supported format (JPEG, PNG, BMP)
   * Consider image size and memory constraints

2. Analysis Configuration
   ^^^^^^^^^^^^^^^^^^^^^

   * Adjust thresholds based on your needs
   * Use appropriate visualization options
   * Consider the trade-off between analysis depth and performance

3. Results Interpretation
   ^^^^^^^^^^^^^^^^^^^^^

   * Review all generated visualizations
   * Consider multiple detection methods
   * Look for patterns across different analysis types

4. Performance Optimization
   ^^^^^^^^^^^^^^^^^^^^^^

   * Use appropriate batch sizes for multiple images
   * Consider using multiprocessing for large datasets
   * Monitor memory usage during analysis

Troubleshooting
-------------

Common issues and solutions:

1. Memory Issues
   ^^^^^^^^^^^^

   * Reduce image size before analysis
   * Process images in smaller batches
   * Monitor system resources

2. False Positives
   ^^^^^^^^^^^^^^

   * Adjust detection thresholds
   * Use multiple analysis methods
   * Consider image context

3. Performance Issues
   ^^^^^^^^^^^^^^^^^

   * Use appropriate batch sizes
   * Enable multiprocessing
   * Optimize visualization settings

For more examples and advanced usage, see the :doc:`examples` section. 