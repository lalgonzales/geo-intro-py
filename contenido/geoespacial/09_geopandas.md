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


# GeoPandas en Python

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/geoespacial/09_geopandas.ipynb)

## Descripción

[GeoPandas](https://geopandas.org) es una librería de código abierto que extiende las estructuras de datos de Pandas para facilitar el trabajo con datos geoespaciales. Permite manipular y analizar geometrías (puntos, líneas, polígonos) de forma sencilla, integrando operaciones espaciales como uniones, buffers, intersecciones y reproyecciones.

## Objetivos de aprendizaje

- Comprender las estructuras básicas de GeoPandas: `GeoDataFrame` y `GeoSeries`.
- Crear `GeoDataFrames` a partir de datos tabulares y formas geométricas.
- Leer y escribir formatos geoespaciales como Shapefile y GeoJSON.
- Realizar operaciones espaciales comunes: áreas, distancias, relaciones espaciales.
- Visualizar datos geoespaciales con Matplotlib y GeoPandas.
- Trabajar con diferentes sistemas de referencia de coordenadas (CRS).

---

## Conceptos clave

Las estructuras principales de GeoPandas son `GeoDataFrame` y `GeoSeries`. Un `GeoDataFrame` es como un DataFrame de Pandas pero con una columna de geometría, lo que permite operaciones espaciales sobre los datos. Un `GeoDataFrame` puede tener varias columnas de geometría, pero solo una es la activa para operaciones espaciales (accesible con `.geometry`).

---

gdf = gpd.read_file(url)

## Instalación e importación de GeoPandas

Antes de comenzar, asegúrate de tener instalado GeoPandas:

```{code-cell} ipython3
# %pip install geopandas
```

Importa las librerías necesarias:

```{code-cell} ipython3
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
```

## Creación de un GeoDataFrame desde cero

```{code-cell} ipython3
data = {
    "Ciudad": ["CDMX", "NYC", "Londres", "París"],
    "Latitud": [19.4, 40.7128, 51.5074, 48.8566],
    "Longitud": [-99.1, -74.0060, -0.1278, 2.3522],
}
df = pd.DataFrame(data)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitud, df.Latitud))
print(gdf)
```

## Lectura y escritura de datos geoespaciales

GeoPandas permite leer y escribir múltiples formatos como Shapefile, GeoJSON y más.

### Lectura de un archivo GeoJSON

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/vector/nybb.geojson"
gdf = gpd.read_file(url)
print(gdf.head())
```

### Escritura de un archivo GeoJSON

```{code-cell} ipython3
output_file = "nyc_boroughs.geojson"
gdf.to_file(output_file, driver="GeoJSON")
print(f"GeoDataFrame guardado en {output_file}")
```

### Escritura de otros formatos

```{code-cell} ipython3
output_file = "nyc_boroughs.shp"
gdf.to_file(output_file)
output_file = "nyc_boroughs.gpkg"
gdf.to_file(output_file, driver="GPKG")
```

---

# Filtrado y selección de datos espaciales
```{code-cell} ipython3
mexico = gdf[gdf["country"] == "Mexico"]
print(mexico)
```

# Operaciones espaciales: cálculo de centroides
```{code-cell} ipython3
mexico["centroide"] = mexico.geometry.centroid
print(mexico[["name", "centroide"]])
```

# Visualización de datos espaciales
```{code-cell} ipython3
mexico.plot(column="population", legend=True)
```

---

## Métodos y operaciones espaciales avanzadas

### Medición de área, boundaries y centroides
```{code-cell} ipython3
gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["boundary"] = gdf.boundary
gdf["centroide"] = gdf.centroid
print(gdf[["area", "boundary", "centroide"]])
```

### Medición de distancias
```{code-cell} ipython3
manhattan_centroid = gdf.loc["Manhattan", "centroide"]
gdf["distancia_a_manhattan"] = gdf["centroide"].distance(manhattan_centroid)
print(gdf[["centroide", "distancia_a_manhattan"]])
```

### Buffer y convex hull
```{code-cell} ipython3
# Buffer de 10000 unidades
gdf["buffered"] = gdf.buffer(10000)
gdf["convex_hull"] = gdf.convex_hull
```

### Visualización avanzada
```{code-cell} ipython3
# Mapa coloreado por área
gdf.plot("area", legend=True, figsize=(10, 6))
plt.title("Boroughs de NYC por área")
plt.show()

# Centroides y boundaries
a = gdf.plot(edgecolor="black", facecolor="none")
gdf["centroide"].plot(ax=a, color="red", marker="o", label="Centroides")
gdf["boundary"].plot(ax=a, color="blue", label="Boundaries")
plt.legend()
plt.show()

# Buffer y convex hull
gdf["buffered"].plot(alpha=0.5, edgecolor="black")
plt.title("Buffer de boroughs (10,000 unidades)")
plt.show()
gdf["convex_hull"].plot(alpha=0.5, color="lightblue", edgecolor="black")
plt.title("Convex hull de boroughs")
plt.show()
```

### Consultas espaciales
```{code-cell} ipython3
# Intersección de buffers con Manhattan
manhattan_geom = gdf.loc["Manhattan", "geometry"]
gdf["intersecta_manhattan"] = gdf["buffered"].intersects(manhattan_geom)
print(gdf[["intersecta_manhattan"]])

# Centroides dentro del polígono
gdf["centroide_en_borough"] = gdf["centroide"].within(gdf["geometry"])
print(gdf[["centroide_en_borough"]])
```

### Proyecciones y CRS
```{code-cell} ipython3
print(gdf.crs)
gdf_4326 = gdf.to_crs(epsg=4326)
gdf_4326.plot(figsize=(10, 6), edgecolor="black")
plt.title("Boroughs de NYC en WGS84 (EPSG:4326)")
plt.show()
```

---

## Ejercicios
1. Crea un GeoDataFrame con una lista de países y sus capitales. Agrega una columna de geometría con la ubicación de las capitales.
2. Carga un shapefile de tu elección, filtra los datos para incluir solo una región o país, y guarda el resultado en un nuevo archivo.
3. Realiza un join espacial entre dos GeoDataFrames: uno con polígonos (ej. países) y otro con puntos (ej. ciudades). Determina qué puntos caen dentro de qué polígonos.
4. Muestra un mapa con la distribución de un atributo (ej. población) en diferentes regiones.

---

## Resumen

GeoPandas permite leer, manipular, analizar y visualizar datos geoespaciales de manera eficiente en Python. Incluye operaciones espaciales como buffers, hulls, consultas espaciales y reproyección de sistemas de coordenadas. Practica leyendo, filtrando y visualizando datos espaciales en tus propios proyectos para dominar el análisis geoespacial en Python.

## Ejercicios
1. Lee un archivo GeoJSON de ciudades y filtra solo las de México.
2. Calcula el centroide de cada ciudad y agrégalo como columna.
3. Visualiza el resultado usando GeoPandas.

## Resumen
GeoPandas permite manipular, analizar y visualizar datos geoespaciales de manera eficiente en Python. Practica leyendo, filtrando y visualizando datos espaciales en tus propios proyectos.
