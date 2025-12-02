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

# Lab 4: Numpy, Pandas y GeoPandas para Análisis Geoespacial

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/labs/lab_04.ipynb)

Este laboratorio te ayudará a consolidar tu comprensión del trabajo con `NumPy`, `Pandas` y `GeoPandas` para el análisis de datos geoespaciales. A través de estos ejercicios, realizarás manipulación de datos, análisis espacial y visualizaciones combinando estas poderosas bibliotecas.

**Lecciones relacionadas:**
- [Numpy y Pandas en Python](../python/08_numpy_pandas.md)
- [GeoPandas en Python](../geoespacial/09_geopandas.md)

+++

## Ejercicio 1: Operaciones con arrays de Numpy y coordenadas geoespaciales

1. Crea un array 2D de Numpy con latitud y longitud de: Tokio (35.6895, 139.6917), Nueva York (40.7128, -74.0060), Londres (51.5074, -0.1278), París (48.8566, 2.3522).
2. Convierte los valores de grados a radianes usando `np.radians()`.
3. Calcula la diferencia elemento a elemento entre Tokio y las otras ciudades en radianes.

```{code-cell} ipython3

```

## Ejercicio 2: Operaciones con DataFrames de Pandas y datos geoespaciales

1. Carga el dataset de ciudades del mundo desde: https://github.com/opengeos/datasets/releases/download/world/world_cities.csv
2. Muestra las primeras 5 filas y revisa valores nulos.
3. Filtra solo ciudades con población mayor a 1 millón.
4. Agrupa por país y calcula la población total por país.
5. Ordena por población descendente y muestra las 10 ciudades más pobladas.

```{code-cell} ipython3

```

## Ejercicio 3: Creación y manipulación de GeoDataFrames con GeoPandas

Este ejercicio se enfoca en crear y manipular GeoDataFrames, realizar operaciones espaciales y visualizar los datos.

1. Carga el dataset de edificios de Nueva York desde el archivo GeoJSON utilizando GeoPandas: https://github.com/opengeos/datasets/releases/download/places/nyc_buildings.geojson
2. Crea un gráfico de las huellas de los edificios y colóralos basados en la altura del edificio (usa la columna `height_MS`).
3. Crea un mapa interactivo de las huellas de los edificios y colóralos basados en la altura del edificio (usa la columna `height_MS`).
4. Calcula la altura promedio del edificio (usa la columna `height_MS`).
5. Selecciona edificios con una altura mayor a la altura promedio.
6. Guarda el GeoDataFrame en un nuevo archivo GeoJSON.

```{code-cell} ipython3

```

## Ejercicio 4: Combinando NumPy, Pandas y GeoPandas

Este ejercicio requiere que combines el poder de NumPy, Pandas y GeoPandas para analizar y visualizar datos espaciales.

1. Usa Pandas para cargar el dataset de ciudades del mundo desde esta URL: https://github.com/opengeos/datasets/releases/download/world/world_cities.csv
2. Filtra el dataset para incluir solo ciudades con valores de latitud entre -40 y 60 (es decir, ciudades ubicadas en el Hemisferio Norte o cerca del ecuador).
3. Crea un GeoDataFrame desde el dataset filtrado convirtiendo la latitud y longitud en geometrías.
4. Reproyecta el GeoDataFrame a la proyección Mercator (EPSG:3857).
5. Calcula la distancia (en metros) entre cada ciudad y la ciudad de París.
6. Grafica las ciudades en un mapa mundial, coloreando los puntos por su distancia a París.

```{code-cell} ipython3

```
