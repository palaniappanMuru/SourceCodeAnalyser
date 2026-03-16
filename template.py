import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trail.ipynb"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created file: {file}")   
    else:
        logging.info(f"File already exists: {file}")