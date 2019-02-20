PYTHON ?= python
.DEFAULT_GOAL := help

install_pulumi:
	curl -fsSL https://get.pulumi.com | sh

install_pyenv:
	curl https://pyenv.run | bash

install:  ## Install python packages
	pipenv install --dev

pep8:  ## Format all Python Files
	@yapf -i $$(find * -type f -name '*.py')
	@flake8 ./app ./tests

clean:  ## Clean temporary files
	find * -type f -name *.pyc | xargs rm -f
	find * -type f -name *~ |xargs rm -f
	find * -type d -name __pycache__ |xargs rm -rf
	rm -rf *.egg-info
	rm -rf dist/
	rm -f *.csv

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
