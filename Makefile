# Makefile

# Install dependencies
install:
	poetry install

# Run tese case using pytest
test:
	poetry run pytest -v tests/

# Format code using black
format:
	poetry run black ImageExtractor/ tests/

# Sorted the imports using isort
sort:
	poetry run isort ImageExtractor/ tests/ --verbose

# Linting the code using flake8
lint:
	poetry run flake8 ImageExtractor/ tests/ --verbose

# Clean pre-commit hooks
pre-commit-clean:
	poetry run pre-commit clean

# Uninstall pre-commit hooks:
pre-commit-uninstall:
	poetry run pre-commit uninstall

# Install pre-commit hooks:
pre-commit-install:
	poetry run pre-commit install

# Run pre-commit hooks
pre-commit-run:
	poetry run pre-commit run --all-files

# Run the FastAPI application with python
run:
	poetry run python main.py

# Run the FastAPI application with uvicorn
uvicorn:
	poetry run uvicorn main:app --workers 2

# Run the FastAPI application with poetry
pt_run:
	poetry run uvicorn main:app --reload

# Clean .pyc and cache files in all directories
clean:
	@echo Cleaning up Python cache files...
	@for /r "." %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /r "." %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@for /r "." %%f in (*.pyo, *.pyd, .pytest_cache .coverage htmlcov .tox) do @if exist "%%f" rmdir /s /q "%%f"
	@echo Cleanup complete!
