Installation
===========

StegAnalyzer can be installed using pip or by building from source.

Using pip
--------

The simplest way to install StegAnalyzer is using pip:

.. code-block:: bash

   pip install steganalyzer

For development installation:

.. code-block:: bash

   pip install -e git+https://github.com/yourusername/steganalyzer.git#egg=steganalyzer

Building from Source
------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/steganalyzer.git
      cd steganalyzer

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Install the package in development mode:

   .. code-block:: bash

      pip install -e .

Requirements
----------

* Python 3.8 or higher
* NumPy
* Pillow
* OpenCV
* SciPy
* Matplotlib
* Seaborn
* scikit-image

Optional Dependencies
------------------

* Sphinx (for documentation)
* pytest (for testing)
* black (for code formatting)
* flake8 (for linting)

Troubleshooting
-------------

Common issues and solutions:

1. OpenCV installation fails
   ^^^^^^^^^^^^^^^^^^^^^^^^^

   On some systems, you may need to install system-level dependencies first:

   .. code-block:: bash

      # Ubuntu/Debian
      sudo apt-get install python3-opencv

      # macOS
      brew install opencv

2. Memory issues with large images
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   If you encounter memory issues when analyzing large images, you can try:

   * Reducing the image size before analysis
   * Using a machine with more RAM
   * Processing the image in chunks

3. Visualization issues
   ^^^^^^^^^^^^^^^^^^^

   If you encounter issues with visualizations:

   * Ensure you have a display server running
   * Try using a different backend for matplotlib
   * Check if your system supports the required graphics libraries

Getting Help
----------

If you encounter any issues during installation:

* Check the :doc:`troubleshooting` guide
* Open an issue on GitHub
* Contact the development team

Next Steps
---------

After installation, you can:

* Read the :doc:`usage` guide
* Try the :doc:`examples`
* Check the :doc:`api` documentation 