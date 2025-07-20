# md_to_ipynb_converter.py
#
# Script personal para convertir archivos .md a .ipynb usando jupytext.
# No realiza ninguna acción con Google Drive ni actualiza enlaces Colab.
# Uso: python scripts/md_to_ipynb_converter.py
# Requiere: jupytext


import glob
import subprocess

# Configuración de rutas
MD_PATHS = [
    "contenido/python/*.md",
    "contenido/geoespacial/*.md",
    "contenido/labs/*.md",
]

md_files = []
for pattern in MD_PATHS:
    md_files.extend(glob.glob(pattern))

for md_file in md_files:
    nb_path = md_file.replace(".md", ".ipynb")
    subprocess.run(["jupytext", "--to", "notebook", md_file, "-o", nb_path], check=True)

print(
    "Conversión de .md a .ipynb finalizada. Los archivos .ipynb han sido actualizados en su ubicación original."
)
