.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	isort --recursive --check-only sqlalchemy_customtypes_test tests
	black -S -l 79 --check sqlalchemy_customtypes_test tests
	pylint sqlalchemy_customtypes_test

format:
	isort -rc -y sqlalchemy_customtypes_test tests
	black -S -l 79 sqlalchemy_customtypes_test tests

test:
	python -m pytest

coverage:
	python -m pytest --cov sqlalchemy_customtypes_test --cov-report term --cov-report xml

htmlcov:
	python -m pytest --cov sqlalchemy_customtypes_test --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.txt
