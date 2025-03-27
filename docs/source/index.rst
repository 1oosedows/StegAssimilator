Welcome to StegAssimilator's documentation!
========================================

StegAssimilator is an advanced tool for detecting and analyzing steganography in images. It provides comprehensive analysis capabilities, visualization tools, and deobfuscation techniques.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   examples
   contributing
   changelog

Features
--------

* Advanced steganography detection
* Multiple analysis techniques
* Enhanced visualization capabilities
* Deobfuscation tools
* Comprehensive reporting
* Easy-to-use API
* Command-line interface

Quick Start
----------

Install the package:

.. code-block:: bash

   pip install stegassimilator

Basic usage:

.. code-block:: python

   from stegassimilator import AdvancedStegAssimilator

   analyzer = AdvancedStegAssimilator()
   results = analyzer.analyze_file("image.jpg")
   print(results)

Command-line usage:

.. code-block:: bash

   stegassimilator image.jpg --visualize --deobfuscate

For more detailed information, see the :doc:`usage` guide.

Indices and tables
-----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 