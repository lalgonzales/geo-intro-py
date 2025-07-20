# JupyterLab

JupyterLab es un entorno de desarrollo interactivo basado en la web para notebooks de Jupyter, código y datos. Es flexible: puedes configurar y organizar la interfaz para adaptarla a distintos flujos de trabajo en ciencia de datos, computación científica y aprendizaje automático. Además, JupyterLab es extensible y modular: puedes escribir complementos que añadan nuevos componentes o se integren con los existentes.

## Instalación

Para instalar JupyterLab, utiliza el siguiente comando:

```bash
pip install jupyterlab
```

## Uso

Para iniciar JupyterLab, ejecuta:

```bash
jupyter lab
```

Para crear un nuevo notebook, haz clic en el icono **+** en el navegador de archivos y selecciona el kernel deseado.

![](https://book.geemap.org/_images/ch01_jupyterlab.jpg)

## Atajos de teclado

JupyterLab tiene dos modos: **Modo edición** y **Modo comando**. El modo edición permite escribir en las celdas como en un editor de texto. El modo comando permite editar el notebook como un todo, pero no escribir en celdas individuales. Existen muchos atajos de teclado. Aquí algunos de los más usados (para Windows y Linux; en Mac reemplaza `Ctrl` por `Command`):

Atajos en ambos modos:

- `Shift + Enter`: ejecutar la celda actual y seleccionar la siguiente
- `Ctrl + Enter`: ejecutar las celdas seleccionadas
- `Alt + Enter`: ejecutar la celda actual e insertar una debajo
- `Ctrl + S`: guardar y crear punto de control

En modo comando (presiona `Esc` para activar):

- `A`: insertar celda arriba
- `B`: insertar celda abajo
- `X`: cortar celdas seleccionadas
- `C`: copiar celdas seleccionadas
- `V`: pegar celdas debajo
- `Y`: cambiar celda a tipo Código
- `M`: cambiar celda a tipo Markdown
- `P`: abrir paleta de comandos

En modo edición (presiona `Enter` para activar):

- `Esc`: activar modo comando
- `Tab`: autocompletar o indentar
- `Shift + Tab`: mostrar tooltip
