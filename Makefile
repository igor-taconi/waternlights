SRC_DIRS := src

install:
	pip install -U pip
	pip install poetry
	poetry install

check:
	poetry run black $(SRC_DIRS) --check
	poetry run isort $(SRC_DIRS) --check --diff
	poetry run flake8 $(SRC_DIRS)

format:
	poetry run isort $(SRC_DIRS)
	poetry run black $(SRC_DIRS)

run:
	poetry run gunicorn app.wsgi:app --bind 0.0.0.0:5000 --timeout 1000 --threads 100 --worker-class gevent
