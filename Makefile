.PHONY: help

help:
	@echo "help   : Show this help message"
	@echo "build  : Build mkdocs"
	@echo "install: Install dependencies"
	@echo "serve  : Run server"
	@echo "publish: Deploy to GitHub pages"
	@echo "test   : Test project"

build:
	@mkdocs build

install:
	@pip install mkdocs-material==8.2.8 twine==3.8.0

serve:
	@mkdocs serve

publish:
	@mkdocs gh-deploy --clean --force

package:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist
	@rm -rf *.egg-info

test:
	@python test.py
