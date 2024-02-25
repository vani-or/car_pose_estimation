.PHONY: notebook docs
.EXPORT_ALL_VARIABLES:

check:
	which pip3
	which python3

install:
	@echo "Installing..."
	mkdir -p .venv
	pipenv install --dev

install_pre_commit:
	pipenv run pre-commit install
	pipenv run pre-commit install --hook-type post-commit

install_on_sagemaker:
	pip3 install pipenv
	pipenv install
	pipenv lock -r > /tmp/pipenv-requirements.txt
	pip3 install -r /tmp/pipenv-requirements.txt

initialize_git:
	git init
	git add -A
	git commit -m 'first commit'
	git branch -M main

setup: initialize_git install install_pre_commit

update:
	@echo "Updating the virtual environment..."
	pipenv update --clear

rebuild:
	@echo "Rebuilding the virtual environment..."
	pipenv lock --clear; pipenv --rm; pipenv install -d

activate:
	@echo "Activating virtual environment"
	pipenv shell

test:
	pipenv run pytest -v

docs_view:
	@echo View API documentation...
	pdoc src --http localhost:8080

docs_save:
	@echo Save documentation to docs...
	pdoc src -o docs

clean:
	pipenv --rm
	rm -rf .venv
	## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache