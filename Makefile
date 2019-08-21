.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv install --dev

check:
	isort --recursive --check-only app tests
	black -S -l 79 --check app tests
	pylint app

format:
	isort -rc -y app tests
	black -S -l 79 app tests

test:
	python -m pytest

coverage:
	python -m pytest --cov app --cov-report term --cov-report xml

htmlcov:
	python -m pytest --cov app --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.txt
