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


[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/04_operaciones_cadenas.ipynb)

# Operaciones con Cadenas en Python

## Descripción
Esta sección cubre operaciones básicas y avanzadas con cadenas de texto en Python, útiles para el manejo de atributos y datos geográficos.

## Objetivos de aprendizaje
- Crear y manipular cadenas en Python, incluyendo concatenación y repetición.
- Aplicar métodos como `lower()`, `upper()`, `strip()`, `replace()`, `split()` para procesar datos geoespaciales.
- Formatear cadenas usando `format()` y f-strings.
- Extraer información de cadenas (parsing) y aplicar operaciones en tareas geoespaciales.

+++

## Crear y manipular cadenas
Las cadenas en Python son secuencias de caracteres. Puedes crearlas con comillas simples o dobles.
```{code-cell} ipython3
location_name = "Monte Everest"  # Nombre de una ubicación
```
Concatenar cadenas:
```{code-cell} ipython3
location_name_full = location_name + ", Nepal"
print(location_name_full)
```
Repetir cadenas:
```{code-cell} ipython3
separador = "-" * 10
print(separador)
```

## Métodos comunes de cadenas
Convertir a minúsculas y mayúsculas:
```{code-cell} ipython3
nombre = "Ciudad de México"
print(nombre.lower())
print(nombre.upper())
```
Eliminar espacios al inicio y final:
```{code-cell} ipython3
ciudad = "  Lima  "
print(ciudad.strip())
```
Reemplazar texto:
```{code-cell} ipython3
pais = "Estados Unidos"
print(pais.replace("Estados", "EEUU"))
```
Dividir cadenas:
```{code-cell} ipython3
coordenadas = "19.4,-99.1"
lat, lon = coordenadas.split(",")
print(lat, lon)
```

## Formateo de cadenas
Usando `format()`:
```{code-cell} ipython3
template = "La ciudad de {} tiene una población de {} habitantes."
print(template.format("Bogotá", 8000000))
```
Usando f-strings:
```{code-cell} ipython3
ciudad = "Quito"
poblacion = 2800000
print(f"La ciudad de {ciudad} tiene una población de {poblacion} habitantes.")
```

## Parsing y extracción de información
Extraer nombre y país de una cadena:
```{code-cell} ipython3
ubicacion = "Cusco, Perú"
nombre_ciudad, pais = ubicacion.split(", ")
print(nombre_ciudad, pais)
```

## Aplicación geoespacial: construir consulta SQL
```{code-cell} ipython3
tabla = "ubicaciones"
condicion = "pais = 'Perú'"
consulta = f"SELECT * FROM {tabla} WHERE {condicion};"
print(consulta)
```

## Ejercicios
1. Crea una cadena con el nombre de una ciudad y conviértela a mayúsculas.
2. Dada una cadena con formato "latitud,longitud", extrae ambos valores y conviértelos a float.
3. Usa `replace()` para cambiar el nombre de un país en una cadena.
4. Construye una consulta SQL para seleccionar ciudades de un país específico usando f-strings.

## Resumen
Dominar las operaciones con cadenas te permitirá limpiar, transformar y analizar datos geográficos de manera eficiente en Python. Practica con tus propios ejemplos y explora más métodos de cadenas en la documentación oficial.

Ejemplo de construcción de una cadena para una consulta SQL geoespacial:

```{code-cell} ipython3
table_name = "locations"
condition = "country = 'Nepal'"
query = f"SELECT * FROM {table_name} WHERE {condition}"
print(query)
```

## Métodos útiles para cadenas

Algunos métodos comunes para procesar texto en Python:

```{code-cell} ipython3
texto = "  Ciudad de México  "
print(texto.lower())      # minúsculas
print(texto.upper())      # mayúsculas
print(texto.strip())      # eliminar espacios
print(texto.replace("México", "CDMX")) # reemplazar
print(texto.split())      # dividir en palabras
```

## Formateo de cadenas

Puedes insertar variables en cadenas usando f-strings:

```{code-cell} ipython3
ciudad = "Puebla"
pais = "México"
frase = f"La ciudad de {ciudad} está en {pais}."
print(frase)
```

## Extracción y parsing de información

Las operaciones con cadenas permiten extraer datos útiles, por ejemplo, coordenadas de un texto:

```{code-cell} ipython3
coordenadas = "19.4,-99.1"
lat, lon = coordenadas.split(",")
print(f"Latitud: {lat}, Longitud: {lon}")
```

## Ejercicios

1. Crea una cadena con el nombre de una ciudad. Convierte la cadena a minúsculas y luego a mayúsculas.
2. Toma una cadena con el formato 'latitud, longitud' (ejemplo: '19.4N, 99.1W') y extrae los valores numéricos de latitud y longitud.
3. Crea una cadena formateada que incluya el nombre de una ubicación y sus coordenadas. Usa tanto el método `format()` como f-strings.
4. Reemplaza una subcadena en el nombre de un lugar (por ejemplo, cambia 'Ciudad de México' por 'CDMX') y muestra el resultado.
5. Dada una lista de direcciones en el formato "Calle, Ciudad, País", escribe una función que devuelva un diccionario con las claves `calle`, `ciudad` y `país`.
6. Escribe una función que convierta un par de coordenadas de latitud y longitud en una cadena WKT `POINT`.

```{code-cell} ipython3
# Ejemplo de función para WKT

def coordenadas_a_wkt(lat, lon):
    return f"POINT({lon} {lat})"

print(coordenadas_a_wkt(19.4, -99.1))
```

## Resumen

Las operaciones con cadenas son esenciales en la programación geoespacial, especialmente al trabajar con datos textuales como nombres de lugares, coordenadas y atributos. Dominar estas técnicas te permitirá manipular y analizar información geográfica de manera eficiente en tus proyectos.
