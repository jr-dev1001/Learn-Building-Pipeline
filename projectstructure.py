import os
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/logging/logging.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/constants.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/exceptions/exception.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",
]


for path in list_of_files:
    file_path = Path(path)

    filedir, filename = os.path.split(path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as file:
            pass
   