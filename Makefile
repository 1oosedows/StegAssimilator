.PHONY: install test lint clean docs

# Python interpreter to use
PYTHON = python3

# Install dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -e .

# Run tests
test:
	$(PYTHON) -m unittest discover tests

# Run linter
lint:
	$(PYTHON) -m flake8 steganalyzer tests
	$(PYTHON) -m black --check steganalyzer tests

# Format code
format:
	$(PYTHON) -m black steganalyzer tests

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .eggs/
	rm -rf .tox/
	rm -rf .venv/
	rm -rf venv/
	rm -rf env/
	rm -rf .env/
	rm -rf .idea/
	rm -rf .vscode/
	rm -rf *.pyc
	rm -rf *.pyo
	rm -rf *.pyd
	rm -rf .Python
	rm -rf .DS_Store
	rm -rf Thumbs.db

# Generate documentation
docs:
	$(PYTHON) -m pip install sphinx sphinx-rtd-theme
	$(PYTHON) -m sphinx.cmd.build -b html docs/source docs/build

# Run all checks
check: lint test

# Create virtual environment
venv:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

# Run example scripts
example:
	$(PYTHON) examples/basic_usage.py
	$(PYTHON) examples/advanced_usage.py

# Build distribution
dist:
	$(PYTHON) setup.py sdist bdist_wheel

# Upload to PyPI (requires twine)
upload:
	twine upload dist/* 