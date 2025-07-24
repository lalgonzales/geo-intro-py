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

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/08_numpy_pandas.ipynb)


# Introducción a Numpy y Pandas

<!-- Enlace Colab se agregará tras subir el notebook adaptado -->

## Descripción

Esta sección introduce las librerías [NumPy](https://numpy.org) y [Pandas](https://pandas.pydata.org), fundamentales para la manipulación y análisis de datos en Python, con aplicaciones en programación geoespacial. NumPy es esencial para operaciones numéricas y manejo de arrays, mientras que Pandas ofrece herramientas poderosas para el análisis de datos tabulares. Dominar estas librerías te permitirá realizar operaciones complejas de datos de manera eficiente en contextos geográficos.

## Objetivos de aprendizaje

- Comprender los conceptos básicos de arrays en NumPy y realizar operaciones sobre ellos.
- Utilizar DataFrames de Pandas para organizar, analizar y manipular datos tabulares.
- Aplicar NumPy y Pandas en programación geoespacial para procesar y analizar conjuntos de datos.
- Combinar NumPy y Pandas para optimizar flujos de trabajo de procesamiento de datos.
- Realizar operaciones complejas como filtrado, agregación y transformación de datos geoespaciales.

---

## Introducción a NumPy

NumPy (Numerical Python) es una librería para computación científica. Proporciona soporte para arrays y matrices multidimensionales, junto con funciones matemáticas para operar sobre ellos.

### Creación de arrays en NumPy

```{code-cell} ipython3
import numpy as np

# Crear un array 1D
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {arr_1d}")

# Crear un array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 2D:\n{arr_2d}")

# Array de ceros
zeros = np.zeros((3, 3))
print(f"Array de ceros:\n{zeros}")

# Array de unos
ones = np.ones((2, 4))
print(f"Array de unos:\n{ones}")

# Array con rango de valores
range_arr = np.arange(0, 10, 2)
print(f"Array rango: {range_arr}")
```

### Operaciones básicas con arrays

```{code-cell} ipython3
# Suma y multiplicación escalar
arr_sum = arr_1d + 10
print(f"Array tras suma: {arr_sum}")
arr_product = arr_1d * 2
print(f"Array tras multiplicación: {arr_product}")

# Multiplicación elemento a elemento
arr_2d_product = arr_2d * np.array([1, 2, 3])
print(f"Multiplicación elemento a elemento en 2D:\n{arr_2d_product}")
```

### Cambio de forma (reshaping)

```{code-cell} ipython3
# Cambiar la forma de un array 1D a 2D
arr_reshaped = np.arange(12).reshape((3, 4))
print(f"Array 1D reestructurado a 2D:\n{arr_reshaped}")
print(f"Forma del array: {arr_reshaped.shape}")
```

## Ejemplo básico

```{code-cell} ipython3
import numpy as np
import pandas as pd
# Ejemplo de array
arr = np.array([1, 2, 3])
print(arr)
```

# Ejemplo de arrays y operaciones básicas con Numpy
```{code-cell} ipython3
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {arr_1d}")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 2D:\n{arr_2d}")
zeros = np.zeros((3, 3))
print(f"Array de ceros:\n{zeros}")
ones = np.ones((2, 4))
print(f"Array de unos:\n{ones}")
range_arr = np.arange(0, 10, 2)
print(f"Array rango: {range_arr}")
```


### Funciones matemáticas sobre arrays

```{code-cell} ipython3
# Raíz cuadrada y logaritmo
arr = np.arange(1, 10)
sqrt_array = np.sqrt(arr)
print(f"Raíz cuadrada: {sqrt_array}")
log_array = np.log1p(arr)
print(f"Logaritmo natural: {log_array}")
```

### Operaciones estadísticas

```{code-cell} ipython3
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Media: {np.mean(arr)}")
print(f"Mediana: {np.median(arr)}")
print(f"Desviación estándar: {np.std(arr):.4f}")
```

### Generación de datos aleatorios

```{code-cell} ipython3
# Generar coordenadas aleatorias
random_coords = np.random.uniform(low=-90, high=90, size=(5, 2))
print(f"Coordenadas aleatorias:\n{random_coords}")
```

### Indexación, slicing y filtrado

```{code-cell} ipython3
arr = np.array([10, 20, 30, 40, 50])
print(f"Primer elemento: {arr[0]}")
print(f"Último elemento: {arr[-1]}")
print(f"Slice 1-3: {arr[1:4]}")
print(f"Filtrado >25: {arr[arr > 25]}")
```

### Ejemplo geoespacial: conversión de grados a radianes

```{code-cell} ipython3
coords = np.array([[19.4, -99.1], [40.7128, -74.0060], [34.0522, -118.2437]])
coords_rad = np.radians(coords)
print(f"Coordenadas en radianes:\n{coords_rad}")
```

# Generación de coordenadas aleatorias
```{code-cell} ipython3
random_coords = np.random.uniform(low=-90, high=90, size=(5, 2))
print(f"Coordenadas aleatorias:\n{random_coords}")
```

# Indexación, slicing y filtrado
```{code-cell} ipython3
arr = np.array([10, 20, 30, 40, 50])
print(f"Primer elemento: {arr[0]}")
print(f"Último elemento: {arr[-1]}")
print(f"Slice 1-3: {arr[1:4]}")
print(f"Filtrado >25: {arr[arr > 25]}")
```

# Ejemplo geoespacial: conversión de grados a radianes
```{code-cell} ipython3
coords = np.array([[19.4, -99.1], [40.7128, -74.0060], [34.0522, -118.2437]])
coords_rad = np.radians(coords)
print(f"Coordenadas en radianes:\n{coords_rad}")
```


## Introducción a Pandas

Pandas es una librería para análisis de datos tabulares. Permite organizar, filtrar, transformar y analizar datos de manera eficiente.

### Ejemplo básico de DataFrame

```{code-cell} ipython3
import pandas as pd
data = {
    "Ciudad": ["CDMX", "NYC", "LA"],
    "Latitud": [19.4, 40.7128, 34.0522],
    "Longitud": [-99.1, -74.0060, -118.2437],
}
df = pd.DataFrame(data)
print(df)
```

### Operaciones con DataFrames

```{code-cell} ipython3
print(df["Latitud"])
print(df[df["Longitud"] < 0])
df["Lat_Radianes"] = np.radians(df["Latitud"])
print(df)
```

### Agrupación y agregación

```{code-cell} ipython3
data = {
    "Ciudad": ["CDMX", "NYC", "LA", "Paris"],
    "País": ["México", "EEUU", "EEUU", "Francia"],
    "Poblacion": [9000000, 8000000, 4000000, 2000000],
}
df2 = pd.DataFrame(data)
print(df2.groupby("País")["Poblacion"].sum())
```

### Manejo de datos faltantes

```{code-cell} ipython3
data_nan = {
    "Ciudad": ["CDMX", "NYC", "LA", "Paris"],
    "Poblacion": [9000000, 8000000, None, 2000000],
}
df_nan = pd.DataFrame(data_nan)
print(df_nan.fillna(df_nan["Poblacion"].mean()))
```

### Lectura de CSV desde URL

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.csv"
df_csv = pd.read_csv(url)
print(df_csv.head())
print(np.sum(df_csv["population"]))
```


### Ejemplo de análisis geoespacial: distancia entre ciudades

```{code-cell} ipython3
def haversine_np(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distancia = R * c
    return distancia

city_pairs = pd.DataFrame({
    "Ciudad1": ["CDMX", "CDMX", "NYC"],
    "Ciudad2": ["NYC", "LA", "LA"],
    "Lat1": [19.4, 19.4, 40.7128],
    "Lon1": [-99.1, -99.1, -74.0060],
    "Lat2": [40.7128, 34.0522, 34.0522],
    "Lon2": [-74.0060, -118.2437, -118.2437],
})
city_pairs["Distancia_km"] = haversine_np(
    city_pairs["Lat1"], city_pairs["Lon1"], city_pairs["Lat2"], city_pairs["Lon2"])
print(city_pairs)
```

---

## Ejercicios
1. Crea un array de Numpy con elevaciones y normalízalo, calculando media y desviación estándar.
2. Crea un DataFrame de Pandas con datos geoespaciales y filtra solo ciudades del hemisferio norte, calculando la latitud media.
3. Usando coordenadas, crea un DataFrame y calcula las distancias entre todos los puntos usando Numpy, guardando los resultados en otro DataFrame.

---

## Resumen

Numpy y Pandas son herramientas esenciales para el análisis y manipulación de datos geoespaciales. Dominar estas librerías te permitirá procesar grandes volúmenes de información y realizar análisis avanzados en tus proyectos.
