# Makefile

# install dependencies
install:
	pip install -r requirements.txt

# run the FastAPI application with python
run:
	python main.py

# run the FastAPI application with fastapi
fastpai:
	fastapi run main.py

# run the FastAPI application with uvicorn
uvicorn:
	uvicorn main:app --workers 2

# run the FastAPI application with poetry
pt run:
	poetry run uvicorn main:app --reload

# Clean .pyc and cache files in all directories
clean:
	@echo Cleaning up Python cache files...
	@for /r "." %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /r "." %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@for /r "." %%f in (*.pyo, *.pyd, .pytest_cache .coverage htmlcov .tox) do @if exist "%%f" rmdir /s /q "%%f"
	@echo Cleanup complete!
