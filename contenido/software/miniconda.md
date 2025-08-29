# Miniconda

[Miniconda](https://www.anaconda.com/download/success) es un instalador mínimo y gratuito para conda. Es una versión ligera de Anaconda que incluye solo conda, Python, sus dependencias y algunos paquetes útiles como pip y zlib.

## Instalación

Para instalar Miniconda, descarga el instalador desde el [sitio oficial de Miniconda](https://www.anaconda.com/download/success) y ejecútalo. El instalador te pedirá aceptar la licencia, elegir el directorio de instalación y agregar conda al perfil de tu shell.

## Uso básico

Después de instalar Miniconda, abre la **Terminal** (o **Anaconda Prompt** en Windows) y crea un nuevo entorno para el curso con los siguientes comandos:

```bash
conda create -n geo python=3.11
conda activate geo
conda install -c conda-forge mamba
mamba install -c conda-forge geemap leafmap
```

## Acceso a Conda en Windows Terminal

Si no agregaste Conda al PATH durante la instalación, puedes hacerlo manualmente:

1. Abre el menú Inicio y busca "Variables de entorno".
2. Haz clic en "Editar las variables de entorno del sistema".
3. En la ventana de propiedades del sistema, haz clic en "Variables de entorno".
4. En "Variables del sistema", busca la variable **Path** y selecciónala.
5. Haz clic en "Editar" y luego en "Nuevo".
6. Agrega la ruta: `C:\Users\<TuUsuario>\miniconda3\Scripts`
7. Haz clic en "Aceptar" para cerrar todas las ventanas.

![image](https://github.com/user-attachments/assets/427ea290-8ea8-42a5-b070-854696f71fc5)

## Comandos comunes

### Crear y gestionar entornos

- **Crear un nuevo entorno:**

  ```bash
  conda create -n mi_entorno python=3.11
  ```
  Cambia `mi_entorno` por el nombre que prefieras y `python=3.11` por la versión deseada.

- **Activar un entorno:**

  ```bash
  conda activate mi_entorno
  ```

- **Desactivar el entorno actual:**

  ```bash
  conda deactivate
  ```

- **Listar todos los entornos:**

  ```bash
  conda env list
  ```

- **Eliminar un entorno:**
  ```bash
  conda remove -n mi_entorno --all
  ```

### Instalar y gestionar paquetes

- **Instalar un paquete en el entorno actual:**

  ```bash
  conda install numpy
  ```

- **Instalar un paquete en un entorno específico:**

  ```bash
  conda install -n mi_entorno pandas
  ```

- **Instalar paquetes desde el canal conda-forge:**

  ```bash
  conda install -c conda-forge geopandas
  ```

- **Instalar varios paquetes a la vez:**

  ```bash
  conda install scipy matplotlib seaborn
  ```

- **Actualizar todos los paquetes en un entorno:**

  ```bash
  conda update --all
  ```

- **Buscar un paquete:**

  ```bash
  conda search scikit-learn
  ```

- **Listar todos los paquetes instalados en el entorno actual:**

  ```bash
  conda list
  ```

- **Eliminar un paquete:**
  ```bash
  conda remove numpy
  ```

### Uso de Mamba (gestión más rápida)

Después de instalar Mamba, puedes usarlo para gestionar paquetes de forma más rápida:

- **Instalar mamba en el entorno base:**

  ```bash
  conda install -n base mamba -c conda-forge
  ```

- **Instalar paquetes usando mamba:**
  ```bash
  mamba install -c conda-forge geemap leafmap
  ```

Estos comandos te ayudarán a gestionar entornos y paquetes de Python usando Miniconda de manera eficiente.
