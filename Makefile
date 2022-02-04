PIPENV_RUN := pipenv run

isort-src:
	$(PIPENV_RUN) isort -rc ./mogoca

isort-docs:
	$(PIPENV_RUN) isort -rc ./docs/src -o mogoca

format: isort-src isort-docs
	$(PIPENV_RUN) black .

test:
	$(PIPENV_RUN) pytest --cov=mogoca/

docs-serve:
	$(PIPENV_RUN) mkdocs serve

docs-publish:
	$(PIPENV_RUN) mkdocs gh-deploy

bumpversion-major:
	$(PIPENV_RUN) bumpversion major

bumpversion-minor:
	$(PIPENV_RUN) bumpversion minor

bumpversion-patch:
	$(PIPENV_RUN) bumpversion patch
