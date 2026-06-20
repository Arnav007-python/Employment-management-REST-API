# Employment Management REST API

[![CI](https://github.com/Arnav007-python/Employment-management-REST-API/actions/workflows/ci.yml/badge.svg)](https://github.com/Arnav007-python/Employment-management-REST-API/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-friendly FastAPI project for managing employee records through a clean REST API.
It includes validated request models, interactive OpenAPI docs, tests, linting, Docker support,
and GitHub Actions CI.

## Features

- Employee CRUD endpoints
- Department, status, and text search filters
- Email uniqueness validation
- Pydantic request and response schemas
- Interactive Swagger UI at `/docs`
- Health check endpoint
- Pytest test suite
- Ruff linting
- Docker and Docker Compose support
- GitHub Actions workflow

## Tech stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Ruff

## Project structure

```text
Employment-management-REST-API/
|-- .github/workflows/ci.yml
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- main.py
|   |-- models.py
|   `-- repository.py
|-- tests/
|   `-- test_main.py
|-- .env.example
|-- .gitignore
|-- Dockerfile
|-- Makefile
|-- README.md
|-- docker-compose.yml
|-- pyproject.toml
|-- requirements-dev.txt
`-- requirements.txt
```

## Getting started

Clone the repository:

```bash
git clone https://github.com/Arnav007-python/Employment-management-REST-API.git
cd Employment-management-REST-API
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open:

- API root: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | API welcome response |
| `GET` | `/health` | Service health check |
| `GET` | `/employees` | List employees |
| `POST` | `/employees` | Create an employee |
| `GET` | `/employees/{employee_id}` | Get one employee |
| `PATCH` | `/employees/{employee_id}` | Update an employee |
| `DELETE` | `/employees/{employee_id}` | Delete an employee |

### List employees with filters

```bash
curl "http://127.0.0.1:8000/employees?department=Engineering&status=active&search=developer"
```

### Create an employee

```bash
curl -X POST "http://127.0.0.1:8000/employees" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Neha",
    "last_name": "Kapoor",
    "email": "neha.kapoor@example.com",
    "department": "Finance",
    "role": "Financial Analyst",
    "salary": 72000,
    "hire_date": "2025-03-10",
    "status": "active"
  }'
```

### Update an employee

```bash
curl -X PATCH "http://127.0.0.1:8000/employees/1" \
  -H "Content-Type: application/json" \
  -d '{"role": "Senior Backend Developer", "salary": 95000}'
```

### Delete an employee

```bash
curl -X DELETE "http://127.0.0.1:8000/employees/1"
```

## Run with Docker

Build and run:

```bash
docker build -t employment-management-rest-api .
docker run --rm -p 8000:8000 employment-management-rest-api
```

Or use Docker Compose:

```bash
docker compose up --build
```

## Tests and linting

```bash
pytest
ruff check .
```

You can also use Make:

```bash
make install
make test
make lint
make dev
```

## Environment variables

Copy `.env.example` to `.env` when you need local overrides:

```bash
cp .env.example .env
```

| Variable | Default | Description |
| --- | --- | --- |
| `APP_NAME` | `Employment Management REST API` | Display name used by API metadata |
| `APP_VERSION` | `1.0.0` | Service version |
| `DEBUG` | `false` | Reserved for local debugging configuration |


## License

This project is licensed under the [MIT License](LICENSE).
