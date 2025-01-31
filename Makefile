.PHONY: clean build publish test

clean:
	rm -rf dist/ build/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	python -m twine upload dist/*

test:
	pytest

install-dev:
	pip install -e ".[dev]"

lint:
	flake8 src/
	black --check src/
	isort --check-only src/

format:
	black src/
	isort src/
