.DEFAULT_GOAL := help

PIPENV_RUN := pipenv run

##################################################
## Help target

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

##################################################
## Formatting targets

isort-src:	## Sort Python imports in source code.
	$(PIPENV_RUN) isort ./mogoca

isort-docs:	## Sort Python imports in documentation code snippets.
	$(PIPENV_RUN) isort ./docs/src -o mogoca

format: isort-src isort-docs ## Format Python code using isort and black.
	$(PIPENV_RUN) black .

##################################################
## Test targets

test:	## Run all tests
	$(PIPENV_RUN) pytest --cov=mogoca/

##################################################
## Documentation targets

docs-serve:	## Server documentation on a local server
	$(PIPENV_RUN) mkdocs serve

docs-publish:	## Publish documentation to
	$(PIPENV_RUN) mkdocs gh-deploy

##################################################
## Version management targets

bumpversion-major:	## Bump library major version.
	$(PIPENV_RUN) bumpversion major

bumpversion-minor:	## Bump library minor version.
	$(PIPENV_RUN) bumpversion minor

bumpversion-patch:	## Bump library patch version.
	$(PIPENV_RUN) bumpversion patch
