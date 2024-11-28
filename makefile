env:
	pip install poetry
	pip install pre-commit
	poetry install
	pre-commit install
	poetry shell

requirements:
	poetry export --without-hashes --without development,notebooks -f requirements.txt -o requirements.txt

