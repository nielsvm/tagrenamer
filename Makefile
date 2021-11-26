.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-docs clean-pyc clean-test

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-docs: ## remove build artifacts
	rm -fr docs/_build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-venv: ## remove existing virtual environment
	rm -rf venv/

lint/flake8: ## check style with flake8
	flake8 tagrenamer tests

lint: lint/flake8 ## check style

test: ## run tests quickly with the default Python
	python3 setup.py test

coverage: ## check code coverage quickly with the default Python
	coverage run --source tagrenamer setup.py test
	coverage report -m
	coverage html
	echo && realpath htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -rf docs/modules
	sphinx-apidoc -H "Modules" --tocfile "index" -o docs/modules/ tagrenamer
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	echo && realpath docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	echo && find dist/

venv: clean-venv ## create a new virtual environment
	python3 -m venv venv/
	. venv/bin/activate
	pip3 install -r requirements.txt
	pip3 install -r requirements_dev.txt
	echo && echo "RUN: source venv/bin/activate"
