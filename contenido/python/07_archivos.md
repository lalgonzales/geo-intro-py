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

Esta sección introduce técnicas para trabajar con archivos y manejar excepciones en Python, enfocándose en su importancia para la programación geoespacial. Aprenderás a leer y escribir archivos, así como a manejar errores de forma robusta para crear aplicaciones confiables.

## Objetivos de aprendizaje

- Leer y escribir archivos en Python, especialmente para datos geoespaciales.
- Implementar manejo de excepciones con `try`, `except` y `finally` para gestionar errores en operaciones de archivos.
- Combinar manejo de archivos y excepciones para crear aplicaciones robustas.
- Identificar y gestionar problemas comunes en el procesamiento de archivos, como archivos faltantes o datos corruptos.
- Aplicar buenas prácticas para el manejo de datos reales en proyectos geográficos.

---

## Creación de un archivo de ejemplo

Antes de trabajar con archivos, es útil crear un archivo de ejemplo programáticamente. Este archivo se usará en los ejemplos siguientes.

```{code-cell} ipython3
# Crear un archivo de coordenadas de ejemplo
datos_ejemplo = """19.4,-99.1\n40.7128,-74.0060\n34.0522,-118.2437\n-33.8688,151.2093\n51.5074,-0.1278"""

archivo_salida = "coordenadas.txt"

try:
    with open(archivo_salida, "w") as archivo:
        archivo.write(datos_ejemplo)
    print(f"Archivo de ejemplo '{archivo_salida}' creado correctamente.")
except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")
```

---


## Lectura y escritura de archivos

En programación geoespacial, es común leer y escribir archivos con coordenadas u otros datos. Python facilita estas tareas con funciones integradas.

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

---

# Manejo de excepciones al parsear coordenadas
```{code-cell} ipython3
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

# Combinando manejo de archivos y excepciones
```{code-cell} ipython3
def procesar_archivo_geoespacial(input_file):
    try:
        with open(input_file, "r") as infile:
            for linea in infile:
                coords = parsear_coordenadas(linea)
                if coords:
                    print(f"Coordenadas procesadas: {coords}")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file} no se encontró.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")
    finally:
        print(f"Finalizó el procesamiento de {input_file}")

procesar_archivo_geoespacial("datos.txt")
```

# Lectura de GeoJSON desde URL (requiere requests)
```{code-cell} ipython3
# !pip install requests
import requests
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"

def obtener_geojson(url):
datos_geojson = obtener_geojson(url)

---

## Lectura de GeoJSON desde URL

En geoprogramación es común acceder a datos en línea, como archivos GeoJSON. Usaremos la librería `requests` para leer datos desde una URL y manejar posibles errores.

```{code-cell} ipython3
# !pip install requests
import requests
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"

def obtener_geojson(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos_geojson = respuesta.json()
        return datos_geojson
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")
    return None

datos_geojson = obtener_geojson(url)
if datos_geojson:
    features = datos_geojson.get("features", [])
    print(f"Número de ciudades: {len(features)}")
    for feature in features[:5]:
        nombre = feature["properties"].get("name")
        pais = feature["properties"].get("country")
        coords = feature["geometry"]["coordinates"]
        print(f"Nombre: {nombre}, País: {pais}, Coordenadas: {coords}")
```

---

## Ejercicios
1. Crea una función que lea un archivo con nombres de ciudades y coordenadas, manejando excepciones si el archivo falta o una línea está mal formateada.
2. Escribe una función que escriba una lista de coordenadas en un archivo, asegurando el cierre correcto aunque ocurra un error.
3. Crea una función robusta que lea datos de un archivo, los procese y escriba los resultados en otro archivo, manejando todos los errores posibles.

---

## Resumen

El manejo de archivos y excepciones es esencial en la programación geoespacial. Dominar estas técnicas te permitirá crear aplicaciones confiables y eficientes que procesen datos reales de manera robusta.
