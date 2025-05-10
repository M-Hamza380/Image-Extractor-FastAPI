import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)s : %(message)s ]"
)

Project_Name = "ImageExtractor"

list_of_files = [
    f"{Project_Name}/__init__.py",
    f"{Project_Name}/ai_models/__init__.py",
    f"{Project_Name}/ai_models/mistralocr.py",
    f"{Project_Name}/ai_models/gemmaocr.py",
    f"{Project_Name}/config/__init__.py",
    f"{Project_Name}/constants/__init__.py",
    f"{Project_Name}/validation_schemas/__init__.py",
    f"{Project_Name}/utils/__init__.py",
    f"{Project_Name}/routers/__init__.py",
    f"static/styles.css",
    f"templates/index.html",
    "main.py",
    f"Makefile",
    f".env.example",
    f"requirements.txt"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as file:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_path} already exists and is not empty. Skipping creation.")
        

