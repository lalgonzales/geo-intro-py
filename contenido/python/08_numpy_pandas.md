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
```

```{code-cell} ipython3
# Crear un array 1D
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {arr_1d}")
```

```{code-cell} ipython3
# Crear un array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 2D:\n{arr_2d}")
```

```{code-cell} ipython3
# Array de ceros
zeros = np.zeros((3, 3))
print(f"Array de ceros:\n{zeros}")
```

```{code-cell} ipython3
# Array de unos
ones = np.ones((2, 4))
print(f"Array de unos:\n{ones}")
```

```{code-cell} ipython3
# Array con rango de valores
range_arr = np.arange(0, 10, 2)
print(f"Array rango: {range_arr}")
```

### Operaciones básicas con arrays

```{code-cell} ipython3
# Suma y multiplicación escalar
arr_sum = arr_1d + 10
print(f"Array tras suma: {arr_sum}")
```

```{code-cell} ipython3
# Array multiplication
arr_product = arr_1d * 2
print(f"Array tras multiplicación: {arr_product}")
```

```{code-cell} ipython3
# Multiplicación elemento a elemento
arr_2d_product = arr_2d * np.array([1, 2, 3])
print(f"Multiplicación elemento a elemento en 2D:\n{arr_2d_product}")
```

### Cambio de forma (reshaping)

```{code-cell} ipython3
# Cambiar la forma de un array 1D a 2D
arr_reshaped = np.arange(12).reshape((3, 4))
print(f"Array 1D reestructurado a 2D:\n{arr_reshaped}")
```

```{code-cell} ipython3
arr_reshaped.shape
```

### Funciones matemáticas sobre arrays

```{code-cell} ipython3
# Raíz cuadrada
sqrt_array = np.sqrt(arr_reshaped)
print(f"Raíz cuadrada:\n{sqrt_array}")
```

```{code-cell} ipython3
# Logaritmo natural
log_array = np.log1p(arr_reshaped)
print(f"Logaritmo natural:\n{log_array}")
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

#### Indexación en NumPy

```{code-cell} ipython3
# Crear un array 1D
arr = np.array([10, 20, 30, 40, 50])

# Primer elemento
print(f"Primer elemento: {arr[0]}")

# Último elemento
print(f"Último elemento: {arr[-1]}")
```

```{code-cell} ipython3
# Crear un array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_2d
```

```{code-cell} ipython3
# Elemento en primera fila, segunda columna
print(f"Elemento en fila 1, columna 2: {arr_2d[0, 1]}")

# Elemento en última fila, última columna
print(f"Elemento en última fila, última columna: {arr_2d[-1, -1]}")
```

#### Slicing en NumPy

```{code-cell} ipython3
# Slice elementos del índice 1 al 3
print(f"Slice 1-3: {arr[1:4]}")

# Slice desde índice 2 en adelante
print(f"Slice desde 2: {arr[2:]}")
```

```{code-cell} ipython3
# Slice primeras dos filas, todas las columnas
slice_2d = arr_2d[:2, :]
print(f"Slice 2D primeras dos filas:\n{slice_2d}")

# Slice últimas dos filas, primeras dos columnas
slice_2d_partial = arr_2d[1:, :2]
print(f"Slice 2D últimas dos filas, primeras dos columnas:\n{slice_2d_partial}")
```

#### Indexación booleana

```{code-cell} ipython3
# Filtrar elementos >25
condition = arr > 25
print(f"Condición booleana: {condition}")

filtered_arr = arr[condition]
print(f"Array filtrado (>25): {filtered_arr}")
```

#### Iterando sobre arrays

Puedes iterar sobre arrays de NumPy para acceder o modificar elementos. Para arrays 1D, puedes simplemente recorrer los elementos. Para arrays multidimensionales, puedes iterar sobre filas o columnas.

**Ejemplo: Iterando sobre un array 1D**

```{code-cell} ipython3
# Crear un array 1D
arr = np.array([10, 20, 30, 40, 50])

# Iterando sobre el array
for element in arr:
    print(f"Elemento: {element}")
```

**Ejemplo: Iterando sobre un array 2D**

```{code-cell} ipython3
# Crear un array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Iterando sobre filas del array 2D
print("Iterando sobre filas:")
for row in arr_2d:
    print(row)

# Iterando sobre cada elemento del array 2D
print("\nIterando sobre cada elemento:")
for row in arr_2d:
    for element in row:
        print(element, end=" ")
```

#### Modificando elementos del array

Puedes usar indexación y slicing para modificar elementos del array.

**Ejemplo: Modificando elementos**

```{code-cell} ipython3
# Crear un array 1D
arr = np.array([10, 20, 30, 40, 50])

# Modificar el elemento en índice 1
arr[1] = 25
print(f"Array modificado: {arr}")

# Modificar múltiples elementos usando slicing
arr[2:4] = [35, 45]
print(f"Array modificado con slicing: {arr}")
```

### Trabajando con coordenadas geoespaciales

Puedes usar NumPy para realizar cálculos en arrays de coordenadas geoespaciales, como convertir de grados a radianes.

```{code-cell} ipython3
# Array de latitudes y longitudes
coords = np.array([[35.6895, 139.6917], [34.0522, -118.2437], [51.5074, -0.1278]])

# Convertir grados a radianes
coords_radians = np.radians(coords)
print(f"Coordenadas en radianes:\n{coords_radians}")
```

## Introducción a Pandas

Pandas es una librería para análisis de datos tabulares. Permite organizar, filtrar, transformar y analizar datos de manera eficiente.

### Ejemplo básico de DataFrame

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
# Crear una Serie
city_series = pd.Series(["CDMX", "NYC", "LA"], name="Ciudad")
print(f"Serie de Pandas:\n{city_series}\n")
```

```{code-cell} ipython3
# Crear un DataFrame
data = {
    "Ciudad": ["CDMX", "NYC", "LA"],
    "Latitud": [19.4, 40.7128, 34.0522],
    "Longitud": [-99.1, -74.0060, -118.2437],
}
df = pd.DataFrame(data)
print(f"DataFrame de Pandas:\n{df}")
```

```{code-cell} ipython3
df
```

### Operaciones con DataFrames

```{code-cell} ipython3
# Seleccionar una columna específica
latitudes = df["Latitud"]
print(f"Latitudes:\n{latitudes}\n")
```

```{code-cell} ipython3
# Filtrar filas basadas en condición
df_filtered = df[df["Longitud"] < 0]
df_filtered
```

```{code-cell} ipython3
# Agregar nueva columna con cálculo
df["Lat_Radianes"] = np.radians(df["Latitud"])
df
```

### Agrupación y agregación

```{code-cell} ipython3
data = {
    "Ciudad": ["CDMX", "NYC", "LA", "Paris"],
    "País": ["México", "EEUU", "EEUU", "Francia"],
    "Poblacion": [9000000, 8000000, 4000000, 2000000],
}
df2 = pd.DataFrame(data)
df2
```

```{code-cell} ipython3
# Agrupar por 'País' y calcular población total
df_grouped = df2.groupby("País")["Poblacion"].sum()
print(f"Población total por País:\n{df_grouped}")
```

### Fusionando DataFrames

Fusionar datasets es esencial cuando combinas diferentes datasets geoespaciales, como unir datos de ciudades con información demográfica.

```{code-cell} ipython3
# Crear dos DataFrames para fusionar
df1 = pd.DataFrame(
    {"Ciudad": ["CDMX", "NYC", "LA"], "País": ["México", "EEUU", "EEUU"]}
)
df2 = pd.DataFrame(
    {
        "Ciudad": ["CDMX", "NYC", "LA"],
        "Poblacion": [9000000, 8000000, 4000000],
    }
)
```

```{code-cell} ipython3
df1
```

```{code-cell} ipython3
df2
```

```{code-cell} ipython3
# Fusionar los dos DataFrames en la columna 'Ciudad'
df_merged = pd.merge(df1, df2, on="Ciudad")
df_merged
```

### Manejo de datos faltantes

En datasets del mundo real, los datos faltantes son comunes. Pandas proporciona herramientas para manejar datos faltantes, como rellenar o eliminar valores faltantes.

```{code-cell} ipython3
# Crear un DataFrame con valores faltantes
data_with_nan = {
    "Ciudad": ["CDMX", "NYC", "LA", "Paris"],
    "Poblacion": [9000000, 8000000, None, 2000000],
}
df_nan = pd.DataFrame(data_with_nan)
df_nan
```

```{code-cell} ipython3
# Rellenar valores faltantes con la media de población
df_filled = df_nan.fillna(df_nan["Poblacion"].mean())
df_filled
```

### Leyendo datos geoespaciales desde un archivo CSV

Pandas puede leer y escribir datos en varios formatos, como CSV, Excel y bases de datos SQL. Esto facilita cargar y guardar datos desde diferentes fuentes. Por ejemplo, puedes leer un archivo CSV en un DataFrame de Pandas y luego realizar operaciones en los datos.

Leamos un archivo CSV desde una URL HTTP en un DataFrame de Pandas y mostremos las primeras filas de los datos.

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.csv"
df = pd.read_csv(url)
df.head()
```

El DataFrame contiene información sobre ciudades del mundo, incluyendo sus nombres, países, poblaciones y coordenadas geográficas. Podemos calcular la población total de todas las ciudades en el dataset usando NumPy y Pandas de la siguiente manera.

```{code-cell} ipython3
np.sum(df["population"])
```

### Creando gráficos con Pandas

Pandas proporciona capacidades de gráficos integradas que te permiten crear varios tipos de gráficos directamente desde DataFrames.

```{code-cell} ipython3
# Cargar el dataset desde una fuente en línea
url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv"
air_quality = pd.read_csv(url, index_col=0, parse_dates=True)

# Mostrar las primeras filas del dataset
air_quality.head()
```

Para hacer una verificación visual rápida de los datos.

```{code-cell} ipython3
air_quality.plot()
```

Para graficar solo las columnas del conjunto de datos con los datos de Paris.

```{code-cell} ipython3
air_quality["station_paris"].plot()
```

Para comparar visualmente los valores medidos en Londres versus Paris.

```{code-cell} ipython3
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
```

Para visualizar cada una de las columnas en un subplot separado.

```{code-cell} ipython3
air_quality.plot.area(figsize=(12, 4), subplots=True)
```

### Analizando datos geoespaciales

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
city_pairs
```

```{code-cell} ipython3
city_pairs["Distancia_km"] = haversine_np(
    city_pairs["Lat1"], city_pairs["Lon1"], city_pairs["Lat2"], city_pairs["Lon2"])
city_pairs
```

## Combinando NumPy y Pandas

Puedes combinar NumPy y Pandas para realizar manipulaciones complejas de datos. Por ejemplo, aplicar funciones de NumPy a un DataFrame de Pandas o usar Pandas para organizar y visualizar los resultados de operaciones de NumPy.

```{code-cell} ipython3
# Función para calcular distancia promedio desde una ciudad a todas las demás
def calculate_average_distance(df):
    lat1 = df["Latitud"].values
    lon1 = df["Longitud"].values
    lat2, lon2 = np.meshgrid(lat1, lon1)
    distances = haversine_np(lat1, lon1, lat2, lon2)
    avg_distances = np.mean(distances, axis=1)
    return avg_distances

# Crear DataFrame
data = {
    "Ciudad": ["CDMX", "NYC", "LA"],
    "Latitud": [19.4, 40.7128, 34.0522],
    "Longitud": [139.6917, -118.2437, -0.1278],
}
df = pd.DataFrame(data)

# Aplicar función para calcular distancias promedio
df["Distancia_Promedio_km"] = calculate_average_distance(df)
df
```

---

## Ejercicios
1. Crea un array de Numpy con elevaciones y normalízalo, calculando media y desviación estándar.
2. Crea un DataFrame de Pandas con datos geoespaciales y filtra solo ciudades del hemisferio norte, calculando la latitud media.
3. Usando coordenadas, crea un DataFrame y calcula las distancias entre todos los puntos usando Numpy, guardando los resultados en otro DataFrame.

---

## Resumen

Numpy y Pandas son herramientas esenciales para el análisis y manipulación de datos geoespaciales. Dominar estas librerías te permitirá procesar grandes volúmenes de información y realizar análisis avanzados en tus proyectos.
