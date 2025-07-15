"""
Colab Notebook Orchestrator

- Converts .md files to .ipynb using jupytext
- Uploads/synchronizes .ipynb files to Google Drive using PyDrive2
- Retrieves public Colab links and updates the .md files
- Logs every action for traceability

Requirements: jupytext, PyDrive2, python-dotenv, valid Google Drive credentials
"""

import os
import glob
import subprocess
from dotenv import load_dotenv
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Load environment variables
load_dotenv()
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")  # Read from .env

# Path configuration
MD_PATHS = ["contenido/python/*.md", "contenido/geoespacial/*.md"]
NOTEBOOK_TEMP_DIR = "temp_notebooks"
LOG_PATH = "private/planning/log_orchestrator.txt"

# 1. Convert .md to .ipynb
os.makedirs(NOTEBOOK_TEMP_DIR, exist_ok=True)
md_files = []
for pattern in MD_PATHS:
    md_files.extend(glob.glob(pattern))

for md_file in md_files:
    nb_name = os.path.splitext(os.path.basename(md_file))[0] + ".ipynb"
    nb_path = os.path.join(NOTEBOOK_TEMP_DIR, nb_name)
    subprocess.run(["jupytext", "--to", "notebook", md_file, "-o", nb_path], check=True)

# 2. Google Drive authentication (credentials required)
ga = GoogleAuth()
ga.LocalWebserverAuth()
drive = GoogleDrive(ga)

# 3. Upload notebooks and get public links
for nb_file in glob.glob(f"{NOTEBOOK_TEMP_DIR}/*.ipynb"):
    nb_name = os.path.basename(nb_file)
    # Check if file already exists in Drive
    file_list = drive.ListFile(
        {"q": f"'{DRIVE_FOLDER_ID}' in parents and title='{nb_name}' and trashed=false"}
    ).GetList()
    if file_list:
        gfile = file_list[0]
        gfile.SetContentFile(nb_file)
        gfile.Upload()
    else:
        gfile = drive.CreateFile(
            {"title": nb_name, "parents": [{"id": DRIVE_FOLDER_ID}]}
        )
        gfile.SetContentFile(nb_file)
        gfile.Upload()
    # Make public and get Colab link
    gfile.InsertPermission({"type": "anyone", "value": "anyone", "role": "reader"})
    public_url = f"https://colab.research.google.com/drive/{gfile['id']}"
    # 4. Update .md file with Colab link
    md_file = f"contenido/python/{nb_name.replace('.ipynb','.md')}"
    target_nb_path = f"contenido/python/{nb_name}"
    if not os.path.exists(md_file):
        md_file = f"contenido/geoespacial/{nb_name.replace('.ipynb','.md')}"
        target_nb_path = f"contenido/geoespacial/{nb_name}"
    if os.path.exists(md_file):
        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Find and replace Colab badge
        for i, line in enumerate(lines):
            if "Abrir en Colab" in line:
                lines[i] = (
                    f"[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]({public_url})\n"
                )
        with open(md_file, "w", encoding="utf-8") as f:
            f.writelines(lines)
        # 6. Convert updated .md to .ipynb in content folder
        target_nb_path = md_file.replace(".md", ".ipynb")
        subprocess.run(
            ["jupytext", "--to", "notebook", md_file, "-o", target_nb_path], check=True
        )
    # 5. Log action
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"{nb_name}: {public_url}\n")

print("Orchestrator finished. Check logs and Colab links in the .md files.")
