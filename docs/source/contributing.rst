Contributing to StegAnalyzer
=========================

Thank you for your interest in contributing to StegAnalyzer! This guide will help you get started.

Development Setup
--------------

1. Fork the repository
2. Clone your fork:

   .. code-block:: bash

      git clone https://github.com/yourusername/steganalyzer.git
      cd steganalyzer

3. Create a virtual environment:

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate  # On Windows: .venv\Scripts\activate

4. Install development dependencies:

   .. code-block:: bash

      pip install -r requirements-dev.txt

5. Install the package in development mode:

   .. code-block:: bash

      pip install -e .

Code Style
---------

We follow PEP 8 guidelines and use the following tools:

* Black for code formatting
* Flake8 for linting
* isort for import sorting

Before submitting a pull request, run:

.. code-block:: bash

   make format
   make lint

Testing
-------

We use pytest for testing. Run the tests with:

.. code-block:: bash

   make test

Write tests for new features and ensure all tests pass before submitting a pull request.

Documentation
-----------

We use Sphinx for documentation. Build the docs with:

.. code-block:: bash

   make docs

Documentation should be updated for any new features or changes.

Pull Request Process
-----------------

1. Create a new branch for your feature:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. Make your changes and commit them:

   .. code-block:: bash

      git add .
      git commit -m "Description of your changes"

3. Push to your fork:

   .. code-block:: bash

      git push origin feature/your-feature-name

4. Create a pull request on GitHub

5. Ensure your pull request:
   * Has a clear description
   * Includes tests
   * Updates documentation
   * Follows code style guidelines
   * Has passing tests

Code Review
---------

All pull requests are reviewed by maintainers. The review process includes:

* Code style check
* Test coverage
* Documentation completeness
* Performance considerations
* Security implications

Please address any feedback from reviewers promptly.

Release Process
------------

1. Update version in setup.py
2. Update CHANGELOG.md
3. Create a release tag
4. Build and upload to PyPI

.. code-block:: bash

   make dist
   make upload

Project Structure
--------------

.. code-block:: text

   steganalyzer/
   ├── docs/                    # Documentation
   ├── examples/                # Example scripts
   ├── steganalyzer/           # Main package
   │   ├── __init__.py
   │   ├── advanced_steg_analysis.py
   │   ├── steg_visualization_enhanced.py
   │   ├── steg_deobfuscation.py
   │   ├── utils/              # Utility functions
   │   ├── types/              # Data structures
   │   ├── exceptions.py       # Custom exceptions
   │   └── config.py           # Configuration
   ├── tests/                  # Test suite
   ├── requirements.txt        # Runtime dependencies
   ├── requirements-dev.txt    # Development dependencies
   ├── setup.py               # Package setup
   ├── Makefile               # Development tasks
   ├── README.md              # Project overview
   ├── LICENSE                # MIT License
   └── CHANGELOG.md           # Version history

Development Guidelines
-------------------

1. Keep code modular and maintainable
2. Write clear docstrings and comments
3. Add type hints where appropriate
4. Follow the existing code style
5. Write comprehensive tests
6. Update documentation as needed

Getting Help
----------

If you need help:

* Check the documentation
* Open an issue on GitHub
* Join our community chat
* Contact the maintainers

Thank you for contributing to StegAnalyzer! 