# Contributing

Thanks for helping improve the Employment Management REST API.

## Local setup

1. Fork and clone the repository.
2. Create a virtual environment.
3. Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

4. Run the API:

```bash
uvicorn app.main:app --reload
```

## Quality checks

Run these before opening a pull request:

```bash
ruff check .
pytest
```

## Pull requests

- Keep changes focused.
- Add or update tests for behavior changes.
- Update the README when endpoints, setup, or usage changes.
