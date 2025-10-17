---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Archivos y Manejo de Excepciones en Python

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/07_archivos.ipynb)

## Descripción

Esta lección introduce técnicas para trabajar con archivos y manejar excepciones en Python, enfocándose en su importancia para la programación geoespacial. Gestionar archivos de manera efectiva es crucial al leer, escribir o procesar datos geoespaciales. El manejo de excepciones es igualmente importante, ya que permite que tus programas gestionen errores de forma elegante, asegurando que tu código siga siendo robusto y confiable incluso ante problemas inesperados.

## Objetivos de aprendizaje

Al final de esta lección, deberías ser capaz de:

- Leer y escribir archivos en Python, con un enfoque particular en el manejo de datos geoespaciales.
- Implementar manejo de excepciones usando bloques `try`, `except` y `finally` para gestionar errores que puedan ocurrir durante operaciones de archivos.
- Combinar manejo de archivos y excepciones para crear aplicaciones geoespaciales robustas y confiables.
- Desarrollar habilidades para identificar y gestionar problemas comunes en el procesamiento de archivos, como archivos faltantes, datos corruptos o errores de formato.
- Asegurar que tus programas geoespaciales puedan manejar escenarios de datos reales de manera efectiva mediante el uso de mejores prácticas para el manejo de archivos y excepciones.

+++

## Creación de un archivo de ejemplo

Antes de trabajar con archivos, es esencial asegurar que los archivos que pretendes procesar realmente existan. En esta sección, aprenderás cómo crear un archivo de ejemplo `coordenadas.txt` programáticamente. Este archivo se usará en los ejemplos siguientes.

```{code-cell} ipython3
# Crear un archivo de coordenadas de ejemplo
datos_ejemplo = """19.4,-99.1
40.7128,-74.0060
34.0522,-118.2437
-33.8688,151.2093
51.5074,-0.1278"""

archivo_salida = "coordenadas.txt"

try:
    with open(archivo_salida, "w") as archivo:
        archivo.write(datos_ejemplo)
    print(f"Archivo de ejemplo '{archivo_salida}' creado correctamente.")
except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")
```

En este código, creamos un archivo de texto simple llamado `coordenadas.txt` que contiene pares de latitud y longitud para varias ciudades alrededor del mundo. El archivo se escribe en el directorio de trabajo actual.

Después de ejecutar este script, el archivo `coordenadas.txt` estará disponible para usar en los ejemplos siguientes. Si ocurren problemas durante la creación del archivo, el script los manejará e imprimirá un mensaje de error.

+++

## Lectura y escritura de archivos

En programación geoespacial, a menudo necesitas leer o escribir archivos. Python proporciona funciones integradas para manejar estas tareas. Empecemos leyendo de un archivo de texto que contiene coordenadas y escribiendo los resultados a un nuevo archivo.

```{code-cell} ipython3
# Ejemplo de lectura y escritura de coordenadas
input_file = "coordenadas.txt"
output_file = "coordenadas_salida.txt"

try:
    with open(input_file, "r") as infile:
        coordenadas = infile.readlines()

    with open(output_file, "w") as outfile:
        for linea in coordenadas:
            lat, lon = linea.strip().split(",")
            outfile.write(f"Latitud: {lat}, Longitud: {lon}\n")

    print(f"Coordenadas escritas en {output_file}")
except FileNotFoundError:
    print(f"Error: El archivo {input_file} no se encontró.")
```

## Manejo de excepciones

El manejo de excepciones permite gestionar errores durante la ejecución del programa. Esto es crucial en programación geoespacial, donde pueden surgir problemas como archivos faltantes, datos corruptos o entradas inválidas.

Exploremos cómo manejar diferentes tipos de excepciones usando `try`, `except` y `finally`.

```{code-cell} ipython3
# Ejemplo de manejo de excepciones al parsear coordenadas
def parsear_coordenadas(linea):
    try:
        lat, lon = linea.strip().split(",")
        lat = float(lat)
        lon = float(lon)
        return lat, lon
    except ValueError as e:
        print(f"Error: {e}. No se pudo parsear la línea: {linea.strip()}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Ejemplo de uso
linea = "dato inválido"
coordenadas = parsear_coordenadas(linea)
if coordenadas:
    print(f"Coordenadas parseadas: {coordenadas}")
```

## Combinando manejo de archivos y excepciones

Puedes combinar el manejo de archivos y excepciones para crear aplicaciones geoespaciales robustas. Esto asegura que los archivos se manejen correctamente incluso si ocurren errores.

```{code-cell} ipython3
# Ejemplo de manejo robusto de archivos con excepciones
def procesar_archivo_geoespacial(input_file):
    try:
        with open(input_file, "r") as infile:
            for linea in infile:
                coordenadas = parsear_coordenadas(linea)
                if coordenadas:
                    print(f"Coordenadas procesadas: {coordenadas}")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no se encontró.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")
    finally:
        print(f"Finalizó el procesamiento de {input_file}")

# Ejemplo de uso
procesar_archivo_geoespacial("coordenadas.txt")
```

## Lectura de GeoJSON desde URL

En geoprogramación es común acceder a datasets alojados en línea. Por ejemplo, podemos necesitar leer datos GeoJSON directamente desde una URL. La librería requests de Python facilita la recuperación de estos datos. En este ejemplo, leeremos un archivo GeoJSON que contiene ciudades del mundo y manejaremos cualquier excepción que pueda surgir.

Primero, asegúrate de tener instalada la librería requests. Descomenta y ejecuta el siguiente comando si no la tienes.

```{code-cell} ipython3
# !pip install requests
```

Importa las librerías necesarias y lee los datos GeoJSON desde la URL.

```{code-cell} ipython3
import requests
```

En este caso, leeremos los datos GeoJSON de ciudades del mundo alojados en https://github.com/opengeos/datasets/releases/tag/world, y los procesaremos para extraer nombres y coordenadas de las ciudades.

```{code-cell} ipython3
url = (
    "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"
)
```

Definamos una función para leer los datos GeoJSON desde la URL y extraer nombres de ciudades y coordenadas. También manejaremos excepciones que puedan ocurrir.

```{code-cell} ipython3
def obtener_geojson(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza excepción para errores HTTP
        datos_geojson = respuesta.json()  # Parsea la respuesta JSON
        return datos_geojson
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión al servidor: {conn_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")
    return None
```

Obtener y mostrar un resumen de los datos.

```{code-cell} ipython3
datos_geojson = obtener_geojson(url)
```

Descomenta y ejecuta el siguiente código para mostrar los datos leídos desde la URL.

```{code-cell} ipython3
# datos_geojson
```

La salida anterior es extensa, así que mostraremos solo las primeras ciudades. Puedes modificar el código para mostrar más si es necesario.

```{code-cell} ipython3
if datos_geojson:
    features = datos_geojson.get("features", [])
    print(f"Número de ciudades: {len(features)}")

    # Extraer nombres de ciudades y sus coordenadas
    for feature in features[:5]:  # Mostrar primeras 5 ciudades
        nombre_ciudad = feature["properties"].get("name")
        nombre_pais = feature["properties"].get("country")
        coordenadas = feature["geometry"]["coordinates"]
        print(f"Nombre: {nombre_ciudad}, País: {nombre_pais}, Coordenadas: {coordenadas}")
```

---

## Ejercicios
1. Crea una función que lea un archivo con nombres de ciudades y coordenadas, manejando excepciones si el archivo falta o una línea está mal formateada.
2. Escribe una función que escriba una lista de coordenadas en un archivo, asegurando el cierre correcto aunque ocurra un error.
3. Crea una función robusta que lea datos de un archivo, los procese y escriba los resultados en otro archivo, manejando todos los errores posibles.

---

## Resumen

El manejo de archivos y excepciones es esencial en la programación geoespacial. Dominar estas técnicas te permitirá crear aplicaciones confiables y eficientes que procesen datos reales de manera robusta.

```{code-cell} ipython3

```
