API Reference
============

This section provides detailed documentation for the StegAnalyzer API.

Core Classes
-----------

AdvancedStegAnalyzer
~~~~~~~~~~~~~~~~~~

.. autoclass:: steganalyzer.AdvancedStegAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

   .. automethod:: analyze_file

   .. automethod:: analyze_directory

   .. automethod:: analyze_color_distribution

   .. automethod:: analyze_dct_coefficients

   .. automethod:: analyze_edge_patterns

   .. automethod:: analyze_lsb_patterns

   .. automethod:: analyze_texture_patterns

   .. automethod:: generate_report

EnhancedStegVisualizer
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: steganalyzer.EnhancedStegVisualizer
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

   .. automethod:: generate_channel_comparison

   .. automethod:: generate_histogram_comparison

   .. automethod:: generate_edge_comparison

   .. automethod:: generate_frequency_analysis

   .. automethod:: generate_texture_visualizations

   .. automethod:: generate_enhanced_visualizations

StegDeobfuscator
~~~~~~~~~~~~~~

.. autoclass:: steganalyzer.StegDeobfuscator
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

   .. automethod:: apply_adaptive_thresholding

   .. automethod:: apply_high_pass_filtering

   .. automethod:: apply_denoising

   .. automethod:: apply_unsharp_masking

   .. automethod:: apply_histogram_equalization

   .. automethod:: apply_laplacian_pyramid

   .. automethod:: apply_frequency_domain_analysis

Utility Functions
--------------

Image Processing
~~~~~~~~~~~~~

.. autofunction:: steganalyzer.utils.image_processing.load_image

.. autofunction:: steganalyzer.utils.image_processing.save_image

.. autofunction:: steganalyzer.utils.image_processing.preprocess_image

Analysis Utilities
~~~~~~~~~~~~~~~

.. autofunction:: steganalyzer.utils.analysis.calculate_histogram

.. autofunction:: steganalyzer.utils.analysis.calculate_dct

.. autofunction:: steganalyzer.utils.analysis.detect_edges

.. autofunction:: steganalyzer.utils.analysis.extract_lsb

.. autofunction:: steganalyzer.utils.analysis.calculate_texture_features

Visualization Utilities
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: steganalyzer.utils.visualization.plot_histogram

.. autofunction:: steganalyzer.utils.visualization.plot_dct

.. autofunction:: steganalyzer.utils.visualization.plot_edges

.. autofunction:: steganalyzer.utils.visualization.plot_texture

Data Structures
-------------

Analysis Results
~~~~~~~~~~~~~

.. autoclass:: steganalyzer.types.AnalysisResult
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.types.ColorAnalysis
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.types.DCTAnalysis
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.types.EdgeAnalysis
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.types.LSBAnalysis
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.types.TextureAnalysis
   :members:
   :undoc-members:
   :show-inheritance:

Exceptions
--------

.. autoexception:: steganalyzer.exceptions.StegAnalyzerError

.. autoexception:: steganalyzer.exceptions.ImageLoadError

.. autoexception:: steganalyzer.exceptions.AnalysisError

.. autoexception:: steganalyzer.exceptions.VisualizationError

Configuration
-----------

.. autoclass:: steganalyzer.config.AnalyzerConfig
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.config.VisualizerConfig
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: steganalyzer.config.DeobfuscatorConfig
   :members:
   :undoc-members:
   :show-inheritance:

Constants
--------

.. autodata:: steganalyzer.constants.DEFAULT_THRESHOLDS

.. autodata:: steganalyzer.constants.SUPPORTED_FORMATS

.. autodata:: steganalyzer.constants.MAX_IMAGE_SIZE

.. autodata:: steganalyzer.constants.DEFAULT_BATCH_SIZE 