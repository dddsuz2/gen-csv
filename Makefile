lint:
	poetry run pflake8 .
	poetry run isort .
	poetry run black .
	poetry run mypy .
