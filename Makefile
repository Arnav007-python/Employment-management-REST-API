.PHONY: install dev test lint format docker-build docker-run

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

dev:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	ruff format .
	ruff check . --fix

docker-build:
	docker build -t employment-management-rest-api .

docker-run:
	docker run --rm -p 8000:8000 employment-management-rest-api
