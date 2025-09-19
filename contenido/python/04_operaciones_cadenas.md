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
Esta sección cubre diversas operaciones con cadenas de texto en Python, enfocándose en su aplicación en el contexto geoespacial. Las cadenas son fundamentales para manejar datos textuales, como nombres de lugares geográficos, coordenadas y datos extraídos de archivos. Dominar las operaciones con cadenas te permite manipular y analizar información geográfica de manera eficiente, lo cual es esencial para tareas como limpieza de datos, formateo, parsing y hasta geocodificación.

## Objetivos de aprendizaje
Al finalizar esta sección, deberías ser capaz de:
- Crear y manipular cadenas en Python, incluyendo concatenación y repetición.
- Aplicar métodos como `lower()`, `upper()`, `strip()`, `replace()`, `split()` para procesar datos geoespaciales.
- Formatear cadenas usando el método `format()` y f-strings para incluir datos variables.
- Extraer información específica de cadenas, como coordenadas o nombres de lugares.
- Utilizar operaciones con cadenas en tareas geoespaciales prácticas, mejorando tu capacidad para trabajar y gestionar datos geográficos.

+++

## Crear y manipular cadenas
Las cadenas en Python son secuencias de caracteres. Puedes crearlas con comillas simples o dobles.
```{code-cell} ipython3
nombre_ubicacion = "Monte Everest"  # Nombre de una ubicación
```
Concatenar cadenas:
```{code-cell} ipython3
nombre_ubicacion_completo = nombre_ubicacion + ", Nepal"
print(nombre_ubicacion_completo)
```
Repetir cadenas:
```{code-cell} ipython3
separador = "-" * 10
print(separador)
```

Construir una consulta SQL básica para seleccionar datos de una base geoespacial:
```{code-cell} ipython3
nombre_tabla = "ubicaciones"
condicion = "pais = 'Nepal'"
consulta_sql = f"SELECT * FROM {nombre_tabla} WHERE {condicion};"
print(consulta_sql)
```

En escenarios más complejos, podrías construir consultas dinámicamente según la entrada del usuario o múltiples condiciones.

## Métodos de cadenas para datos geoespaciales

Python ofrece varios métodos integrados para manipular cadenas. Algunos de los más usados son:

- `lower()`, `upper()`: Convierte cadenas a minúsculas o mayúsculas.
- `strip()`: Elimina espacios al inicio y final.
- `lstrip()`, `rstrip()`: Elimina espacios solo al inicio o solo al final.
- `replace()`: Reemplaza una subcadena por otra.
- `split()`: Divide una cadena en una lista de subcadenas usando un delimitador.
- `join()`: Une una lista de cadenas en una sola cadena usando un delimitador.



Convertir a mayúsculas:
```{code-cell} ipython3
nombre_ubicacion = "Ciudad de México"
nombre_ubicacion_mayus = nombre_ubicacion.upper()
print(nombre_ubicacion_mayus)  # Convertir a mayúsculas
```

Eliminar espacios al inicio y final:
```{code-cell} ipython3
nombre_ubicacion_limpio = nombre_ubicacion.strip()
print(nombre_ubicacion_limpio)  # Eliminar espacios
```

Reemplazar texto:
```{code-cell} ipython3
nombre_ubicacion_reemplazado = nombre_ubicacion.replace("México", "Lima")
print(nombre_ubicacion_reemplazado)  # Reemplazar 'México' por 'Lima'
```

Dividir cadenas:
```{code-cell} ipython3
nombre_ubicacion_completo = "Ciudad de México, Lima"
partes_ubicacion = nombre_ubicacion_completo.split(", ")
print(partes_ubicacion)  # Dividir la cadena en una lista
```

```{code-cell} ipython3
paises = [" nepal", "INDIA ", "china ", "Bhutan"]
paises_normalizados = [pais.strip().title() for pais in paises]
print(paises_normalizados)  # Elimina espacios y capitaliza
```
Esta operación elimina espacios y asegura capitalización consistente.

## Formateo de cadenas

El formateo de cadenas es esencial cuando preparas datos para mostrar o necesitas incluir valores variables en tus textos. Puedes usar el método `format()` o f-strings (a partir de Python 3.6) para insertar valores en cadenas de manera flexible y legible.

Formateo de coordenadas:
```{code-cell} ipython3
latitud = 27.9881
longitud = 86.9250
coordenadas_formateadas = "Coordenadas: ({}, {})".format(latitud, longitud)
print(coordenadas_formateadas)
coordenadas_fstring = f"Coordenadas: ({latitud}, {longitud})"
print(coordenadas_fstring)
```

Ejemplo adicional de formateo:
```{code-cell} ipython3
plantilla = "La ciudad de {} tiene una población de {} habitantes."
print(plantilla.format("Bogotá", 8000000))
ciudad = "Quito"
poblacion = 2800000
print(f"La ciudad de {ciudad} tiene una población de {poblacion} habitantes.")
```

Texto WKT (Well-Known Text) para geometría:
```{code-cell} ipython3
wkt_punto = f"POINT({longitud} {latitud})"
print(wkt_punto)
```

## Extraer información de cadenas

A menudo necesitarás extraer información específica de cadenas, especialmente con datos geográficos. Por ejemplo, puedes extraer coordenadas de una cadena formateada:

Si tienes una lista de direcciones en el formato "Calle, Ciudad, País", puedes extraer cada componente:
```{code-cell} ipython3
direccion = "123 Everest Rd, Kathmandu, Nepal"
calle, ciudad, pais = direccion.split(", ")
print(f"Calle: {calle}, Ciudad: {ciudad}, País: {pais}")
```

## Parsing y extracción de información

Ejemplo de parsing de coordenadas:
```{code-cell} ipython3
cadena_coordenadas = "40.7128N, 74.0060W"
lat_str, lon_str = cadena_coordenadas.split(", ")
latitud = float(lat_str[:-1])  # Convierte a float y elimina la 'N'
longitud = float(lon_str[:-1])  # Convierte a float y elimina la 'W'
print(f"Coordenadas extraídas: ({latitud}, {longitud})")
```

## Aplicación geoespacial: construir consulta SQL

## Ejercicios
1. Crea una cadena con el nombre de una ciudad. Convierte la cadena a minúsculas y luego a mayúsculas.
2. Toma una cadena con el formato 'latitud, longitud' (ejemplo: '19.4N, 99.1W') y extrae los valores numéricos de latitud y longitud.
3. Crea una cadena formateada que incluya el nombre de una ubicación y sus coordenadas. Usa tanto el método `format()` como f-strings.
4. Reemplaza una subcadena en el nombre de un lugar (por ejemplo, cambia 'San Francisco' por 'San Diego') y muestra el resultado.
5. Dada una lista de direcciones en el formato "Calle, Ciudad, País", escribe una función que devuelva un diccionario con las claves `calle`, `ciudad` y `país`.
6. Escribe una función que convierta un par de coordenadas de latitud y longitud en una cadena WKT `POINT`.

## Resumen

Las operaciones con cadenas son fundamentales en la programación geoespacial, especialmente al trabajar con datos geográficos en formato texto. Dominar estas operaciones te permitirá manipular, limpiar y analizar información geográfica de manera eficiente en tus proyectos, ya sea para formatear salidas, analizar entradas o integrar con bases de datos geoespaciales.

```{code-cell} ipython3
nombre_tabla = "ubicaciones"
condicion = "pais = 'Nepal'"
consulta_sql = f"SELECT * FROM {nombre_tabla} WHERE {condicion}"
print(consulta_sql)
```

## Métodos útiles para cadenas

Algunos métodos comunes para procesar texto en Python:
```{code-cell} ipython3
texto = "  Ciudad de México  "
print(texto.lower())      # Convierte a minúsculas
print(texto.upper())      # Convierte a mayúsculas
print(texto.strip())      # Elimina espacios al inicio y final
print(texto.lstrip())     # Elimina solo al inicio
print(texto.rstrip())     # Elimina solo al final
print(texto.replace("México", "CDMX")) # Reemplaza 'México' por 'CDMX'
print(texto.split())      # Divide la cadena en una lista de palabras
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

Parsing avanzado de coordenadas con sufijos:
```{code-cell} ipython3
cadena_coordenadas = "27.9881N, 86.9250E"
lat_str, lon_str = cadena_coordenadas.split(", ")
latitud = float(lat_str[:-1])  # Elimina 'N'
longitud = float(lon_str[:-1]) # Elimina 'E'
print(f"Coordenadas extraídas: ({latitud}, {longitud})")
```

Parsing de direcciones y función para diccionario:
```{code-cell} ipython3
def parsear_direccion(direccion):
    calle, ciudad, pais = direccion.split(", ")
    return {"calle": calle, "ciudad": ciudad, "pais": pais}

direccion = "Av. Principal 123, Quito, Ecuador"
print(parsear_direccion(direccion))
```

## Ejercicios

1. Crea una cadena con el nombre de una ciudad. Convierte la cadena a minúsculas y luego a mayúsculas.
2. Toma una cadena con el formato 'latitud, longitud' (ejemplo: '19.4N, 99.1W') y extrae los valores numéricos de latitud y longitud.
3. Crea una cadena formateada que incluya el nombre de una ubicación y sus coordenadas. Usa tanto el método `format()` como f-strings.
4. Reemplaza una subcadena en el nombre de un lugar (por ejemplo, cambia 'Ciudad de México' por 'CDMX') y muestra el resultado.
5. Dada una lista de direcciones en el formato "Calle, Ciudad, País", escribe una función que devuelva un diccionario con las claves `calle`, `ciudad` y `país`.
6. Escribe una función que convierta un par de coordenadas de latitud y longitud en una cadena WKT `POINT`.
7. Normaliza una lista de países eliminando espacios y capitalizando los nombres.
8. Une una lista de palabras en una sola cadena usando un delimitador.

```{code-cell} ipython3
# Ejemplo de función para WKT

def coordenadas_a_wkt(latitud, longitud):
  return f"POINT({longitud} {latitud})"

print(coordenadas_a_wkt(19.4, -99.1))
```

## Resumen

Las operaciones con cadenas son esenciales en la programación geoespacial, especialmente al trabajar con datos textuales como nombres de lugares, coordenadas y atributos. Dominar estas técnicas te permitirá manipular y analizar información geográfica de manera eficiente en tus proyectos.

Las cadenas son fundamentales para limpiar, formatear, extraer y preparar datos geográficos. Practica con tus propios ejemplos y explora más métodos en la documentación oficial de Python. Estas habilidades te ayudarán a trabajar con bases de datos, archivos de texto y APIs geoespaciales de manera profesional.
