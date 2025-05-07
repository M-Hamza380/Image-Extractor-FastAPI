# Makefile

# install dependencies
install:
	pip install -r requirements.txt

# run the FastAPI application
run:
	python main.py

fastpai:
	fastapi run main.py

uvicorn:
	uvicorn main:app --workers 2

# Clean .pyc and cache files in all directories
clean:
	@echo Cleaning up Python cache files...
	@for /r "." %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /r "." %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@for /r "." %%f in (*.pyo, *.pyd, .pytest_cache .coverage htmlcov .tox) do @if exist "%%f" rmdir /s /q "%%f"
	@echo Cleanup complete!
