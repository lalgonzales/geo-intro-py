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


# GeoPandas

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

Las estructuras principales de GeoPandas son `GeoDataFrame` y `GeoSeries`. Un `GeoDataFrame` extiende la funcionalidad de un DataFrame de Pandas agregando una columna de geometría, lo que permite operaciones espaciales sobre formas geométricas. El `GeoSeries` maneja datos geométricos (puntos, polígonos, etc.).

Un `GeoDataFrame` puede tener múltiples columnas de geometría, pero solo una es considerada la geometría activa en cualquier momento. Todas las operaciones espaciales se aplican a esta geometría activa, accesible vía el atributo `.geometry`.

GeoPandas combina las funcionalidades de Pandas y Shapely, permitiendo operaciones geoespaciales como uniones espaciales, buffers, intersecciones y proyecciones con facilidad.

## Instalación e importación de GeoPandas

Antes de comenzar, asegúrate de tener instalado GeoPandas. Puedes instalarlo usando:

```{code-cell} ipython3
# %pip install geopandas
```

Una vez instalado, importa GeoPandas y otras librerías necesarias:

```{code-cell} ipython3
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
```

## Creación de GeoDataFrames

Un GeoDataFrame es una estructura tabular que contiene una columna `geometry`, que almacena las formas geométricas. Puedes crear un GeoDataFrame a partir de una lista de geometrías o desde un DataFrame de Pandas.

```{code-cell} ipython3
# Creando un GeoDataFrame desde cero
data = {
    "Ciudad": ["CDMX", "NYC", "Londres", "París"],
    "Latitud": [19.4, 40.7128, 51.5074, 48.8566],
    "Longitud": [-99.1, -74.0060, -0.1278, 2.3522],
}
df = pd.DataFrame(data)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitud, df.Latitud))
gdf
```

## Lectura y escritura de datos geoespaciales

GeoPandas permite leer y escribir múltiples formatos como Shapefile, GeoJSON y más.

### Lectura de un archivo GeoJSON

Cargaremos el dataset de boroughs de Nueva York desde un archivo GeoJSON alojado en línea.

```{code-cell} ipython3
url = "https://github.com/lalgonzales/datasets/blob/main/vector/departamentos_hn.geojson?raw=true"
gdf = gpd.read_file(url)
gdf.head()
```

Este `GeoDataFrame` contiene varias columnas, incluyendo `depto`, que representa los nombres de los departamentos, y `geometry`, que almacena los polígonos para cada departamento.

### Escritura de un archivo GeoJSON

GeoPandas también soporta guardar datos geoespaciales en disco. Por ejemplo, podemos guardar el GeoDataFrame como un nuevo archivo GeoJSON:

```{code-cell} ipython3
output_file = "deptos_hn.geojson"
gdf.to_file(output_file, driver="GeoJSON")
print(f"GeoDataFrame guardado en {output_file}")
```

De manera similar, puedes escribir GeoDataFrames a otros formatos, como Shapefiles, GeoPackage y más.

```{code-cell} ipython3
output_file = "deptos_hn.shp"
gdf.to_file(output_file, driver="ESRI Shapefile")
```

```{code-cell} ipython3
output_file = "deptos_hn.gpkg"
gdf.to_file(output_file, driver="GPKG")
```

---

## Accesores y métodos simples

Ahora que tenemos los datos, exploremos algunos métodos simples de GeoPandas para manipular y analizar los datos geométricos.

### Medición de área

Podemos calcular el área de cada departamento. GeoPandas calcula automáticamente el área de cada polígono:

```{code-cell} ipython3
# Establecer depto como índice para referencia más fácil
gdf = gdf.set_index("depto")

# Calcular el área
gdf["area"] = gdf.area
gdf
```

### Obtención de boundaries y centroides de polígonos

Para obtener el boundary (líneas) y centroide (punto central) de cada polígono:

```{code-cell} ipython3
# Obtener el boundary de cada polígono
gdf["boundary"] = gdf.boundary

# Obtener el centroide de cada polígono
gdf["centroid"] = gdf.centroid

gdf[["boundary", "centroid"]]
```

### Medición de distancias

También podemos medir la distancia desde el centroide de cada departamento a un punto de referencia, como el centroide de Francisco Morazán.

```{code-cell} ipython3
# Usar el centroide de Francisco Morazán como punto de referencia
fm_centroid = gdf.loc["Francisco Morazán", "centroid"]

# Calcular la distancia desde cada centroide al centroide de Francisco Morazán
gdf["distancia_a_fm"] = gdf["centroid"].distance(fm_centroid)
gdf[["centroid", "distancia_a_fm"]]
```

### Cálculo de distancia media

Podemos calcular la distancia media entre los centroides de los departamentos y Francisco Morazán:

```{code-cell} ipython3
distancia_media = gdf["distancia_a_fm"].mean()
print(f"Distancia media a Francisco Morazán: {distancia_media} unidades")
```

---

## Visualización de datos geoespaciales

GeoPandas se integra con Matplotlib para graficar fácilmente datos geoespaciales. Creemos algunos mapas para visualizar los datos.

### Graficando el área de cada departamento

Podemos colorear los departamentos basados en su área y mostrar una leyenda:

```{code-cell} ipython3
gdf.plot("area", legend=True, figsize=(10, 6))
plt.title("Departamentos de Honduras por área")
plt.show()
```

### Graficando centroides y boundaries

También podemos graficar los centroides y boundaries:

```{code-cell} ipython3
# Graficar los boundaries y centroides
ax = gdf["geometry"].plot(figsize=(10, 6), edgecolor="black")
gdf["centroid"].plot(ax=ax, color="red", markersize=50)
plt.title("Límites y centroides de departamentos de Honduras")
plt.show()
```

También puedes explorar tus datos de manera interactiva usando `GeoDataFrame.explore()`, que se comporta igual que `plot()` pero devuelve un mapa interactivo en su lugar.

```{code-cell} ipython3
gdf.explore("area", legend=False)
```

## Manipulaciones de geometría

GeoPandas proporciona varios métodos para manipular geometrías, como buffering (crear una zona buffer alrededor de geometrías) y calcular convex hulls (la forma convexa más pequeña que encierra las geometrías).

### Buffering de geometrías

Podemos crear una zona buffer alrededor de cada borough:

```{code-cell} ipython3
# Buffer de los departamentos por 10000 metros
gdf["buffered"] = gdf.buffer(10000)

# Graficar las geometrías bufferadas
gdf["buffered"].plot(alpha=0.5, edgecolor="black")
plt.title("Departamentos de Honduras bufferados (10000 metros)")
plt.show()
```

### Convex Hulls

El convex hull es la forma convexa más pequeña que puede encerrar una geometría. Calculemos el convex hull para cada borough:

```{code-cell} ipython3
# Calcular convex hull
gdf["convex_hull"] = gdf.convex_hull

# Graficar los convex hulls
gdf["convex_hull"].plot(alpha=0.5, color="lightblue", edgecolor="black")
plt.title("Convex hull de departamentos de Honduras")
plt.show()
```

## Consultas espaciales y relaciones

También podemos realizar consultas espaciales para examinar relaciones entre geometrías. Por ejemplo, podemos verificar qué boroughs están dentro de cierta distancia de Francisco Morazán.

### Verificando intersecciones

Podemos encontrar qué boroughs bufferados intersectan con la geometría original de Francisco Morazán:
```{code-cell} ipython3
# Obtener la geometría de Francisco Morazán
fm_geom = gdf.loc["Francisco Morazán", "geometry"]

# Verificar qué departamentos bufferados intersectan con la geometría de Francisco Morazán
gdf["intersecta_fm"] = gdf["buffered"].intersects(fm_geom)
gdf[["intersecta_fm"]]
```

### Verificando contención

De manera similar, podemos verificar si los centroides están contenidos dentro de los boundaries de los boroughs:

```{code-cell} ipython3
# Verificar si los centroides están dentro de las geometrías originales de los departamentos
gdf["centroide_en_departamento"] = gdf["centroid"].within(gdf["geometry"])
gdf[["centroide_en_departamento"]]
```

### Proyecciones y sistemas de referencia de coordenadas (CRS)

GeoPandas facilita el manejo de proyecciones. Cada GeoSeries y GeoDataFrame tiene un atributo crs que define su CRS.

### Verificando el CRS

Verifiquemos el CRS del dataset de departamentos de Honduras:

```{code-cell} ipython3
print(gdf.crs)
```

El CRS para este dataset es [`EPSG:32616`](https://epsg.io/32616) (WS84 / UTM zone 16N). Podemos reproyectar las geometrías a WGS84 ([`EPSG:4326`](https://epsg.io/4326)), que usa coordenadas de latitud y longitud.

[EPSG](https://epsg.io) significa European Petroleum Survey Group, que fue una organización científica que estandarizó sistemas de referencia geodésicos y de coordenadas. Los códigos EPSG son identificadores únicos que representan sistemas de coordenadas y otras propiedades geodésicas.

### Reproyectando a WGS84

```{code-cell} ipython3
# Reproyectar el GeoDataFrame a WGS84 (EPSG:4326)
gdf_4326 = gdf.to_crs(epsg=4326)

# Graficar las geometrías reproyectadas
gdf_4326.plot(figsize=(10, 6), edgecolor="black")
plt.title("Departamentos de Honduras en WGS84 (EPSG:4326)")
plt.show()
```

Nota cómo las coordenadas han cambiado de metros a grados.

## Ejercicios

1. Crea un GeoDataFrame que contenga una lista de países y sus capitales. Agrega una columna de geometría con las ubicaciones de las capitales.
2. Carga un shapefile de tu elección, filtra los datos para incluir solo una región o país específico, y guarda el GeoDataFrame filtrado en un nuevo archivo.
3. Realiza una unión espacial entre dos GeoDataFrames: uno conteniendo polígonos (ej. fronteras de países) y uno conteniendo puntos (ej. ciudades). Determina qué puntos caen dentro de qué polígonos.
4. Grafica un mapa mostrando la distribución de un atributo particular (ej. población) a través de diferentes regiones.

```{code-cell} ipython3

```

## Resumen

Esta lección proporcionó una introducción al trabajo con datos geoespaciales usando GeoPandas. Cubrimos conceptos básicos como leer/escribir datos geoespaciales, realizar operaciones espaciales (ej. buffering, intersecciones) y visualizar datos geoespaciales usando mapas. GeoPandas, construido sobre Pandas y Shapely, permite análisis geoespacial eficiente e intuitivo en Python.
