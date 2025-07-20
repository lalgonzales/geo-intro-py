# Google Colab

[Google Colab](https://colab.research.google.com/) es un servicio gratuito en la nube que permite ejecutar notebooks de Python con acceso a GPU y TPU sin necesidad de configuración local. Es un entorno basado en Jupyter que facilita escribir, ejecutar y compartir código directamente desde el navegador, guardando los archivos en Google Drive.

## Consejos y Trucos

1. **Notebook de Scratch:** <https://colab.research.google.com/notebooks/empty.ipynb>
2. **Abrir notebooks desde GitHub:** Simplemente reemplaza `github.com` por `githubtocolab.com` en la URL para abrir el notebook en Colab.
3. **Extensión "Open in Colab" para Chrome:** Instala la [extensión Open in Colab](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo) para abrir notebooks de GitHub en Colab con un solo clic.
4. **Ver tiempo de ejecución de una celda:** Pasa el cursor sobre el ícono de ejecución de la celda para ver el tiempo estimado de ejecución.
5. **Ejecutar parte de una celda:** Usa `Runtime -> Run Selection` o el atajo `Ctrl + Shift + Enter`.
6. **Atajos de teclado más usados:**
   - Ejecutar celda (`Ctrl + Enter`)
   - Ejecutar celda y agregar nueva abajo (`Alt + Enter`)
   - Ejecutar celda e ir a la siguiente (`Shift + Enter`)
   - Comentar línea actual (`Ctrl + /`)
7. **Atajos de Jupyter Notebook:** Ve a Herramientas → Atajos de teclado o antepone `Ctrl + M` al atajo de Jupyter:
   - Agregar celda arriba (`Ctrl + M + A`)
   - Agregar celda abajo (`Ctrl + M + B`)
   - Cambiar celda a código (`Ctrl + M + Y`)
   - Cambiar celda a markdown (`Ctrl + M + M`)
8. **Saltar a la definición de una clase:** Mantén presionada `Ctrl` y haz clic en el nombre de la clase.
9. **Ejecutar comandos de bash:**
   - Descargar datos: `!wget <URL>`
   - Instalar librerías: `!pip install <LIBRERÍA>`
   - Clonar repositorio: `!git clone <URL>`
   - Cambiar directorio: `!cd`
10. **Montar Google Drive en Colab:**

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

11. **Subir archivos desde tu computadora:**

```python
from google.colab import files
files.upload()
```

12. **Descargar archivos desde Colab:**

```python
from google.colab import files
files.download('ruta/al/archivo')
```

13. **Badge "Open in Colab":** Puedes agregar un badge para abrir notebooks en Colab usando:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)

```text
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
```

**Referencias:**
- [Google Colab Tips for Power Users](https://amitness.com/2020/06/google-colaboratory-tips/)
- [10 trucos para una mejor experiencia en Google Colab](https://towardsdatascience.com/10-tips-for-a-better-google-colab-experience-33f8fe721b82)
