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
# Variables y Tipos de Datos

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/02_variables.ipynb)

## Descripción
Esta sección introduce los conceptos fundamentales de variables y tipos de datos en Python, con ejemplos aplicados a programación geoespacial. Aprenderás cómo declarar variables, buenas prácticas de nombres y los tipos de datos más usados en Python para datos geográficos.

## Objetivos de aprendizaje
- Definir y usar variables en Python siguiendo buenas prácticas de nombres y asignación.
- Identificar y utilizar los tipos de datos principales: enteros, flotantes, cadenas, booleanos, listas y diccionarios.
- Comprender cómo se usan los tipos de datos en el contexto geoespacial (coordenadas, atributos, etc.).
- Realizar operaciones básicas y manipulaciones sobre los tipos de datos.
- Aplicar estos conceptos en problemas geoespaciales reales, como calcular centroides y manejar atributos.

+++

## Variables en Python
En Python, una variable es un nombre simbólico que referencia un objeto. Una vez asignado, puedes manipular ese objeto usando el nombre de la variable.

Por ejemplo, para representar el número de puntos espaciales en un dataset:
```{code-cell} ipython3
num_puntos = 120
```

Para ver el valor de la variable:
```{code-cell} ipython3
print(num_puntos)
```

También puedes simplemente escribir el nombre de la variable en una celda para ver su valor:
```{code-cell} ipython3
num_puntos
```

## Buenas prácticas para nombres de variables
- Deben comenzar con una letra o guion bajo (`_`).
- El resto puede contener letras, números y guiones bajos.
- Son sensibles a mayúsculas/minúsculas (`num_puntos` ≠ `Num_Puntos`).
- Usa nombres descriptivos y significativos, por ejemplo `num_puntos` en vez de `n`.
- Evita palabras reservadas de Python y funciones integradas como `print`, `sum`, `list`, `dict`, etc.

Ejemplo:
```{code-cell} ipython3
nombre_capa = "puntos_geograficos"
_numero = 5
print(nombre_capa, _numero)
```

## Tipos de datos principales en Python

### Enteros (int)
```{code-cell} ipython3
num_features = 500  # Número de features en un dataset geoespacial
```

### Flotantes (float)
```{code-cell} ipython3
latitud = 19.4      # Latitud de un punto
longitud = -99.1    # Longitud de un punto
```

### Cadenas (str)
```{code-cell} ipython3
nombre_ciudad = "Ciudad de México"  # Nombre de una ciudad
```

Las cadenas pueden ir entre comillas simples ('') o dobles ("").

### Booleanos (bool)
```{code-cell} ipython3
es_capital = True   # Indica si es capital
```

### Listas
```{code-cell} ipython3
coordenadas = [19.4, -99.1]  # Lista de latitud y longitud
```

### Diccionarios
```{code-cell} ipython3
atributos = {"nombre": "CDMX", "poblacion": 9000000, "coords": [19.4, -99.1]}
```

## Caracteres de escape
Los caracteres de escape permiten insertar caracteres especiales en cadenas. Por ejemplo, `\n` para salto de línea y `\t` para tabulación.
```{code-cell} ipython3
print("Hola Mundo!\nEsto es un script de Python.")
print("Primera línea.\n\tSegunda línea con sangría.")
print("¿Cuál es tu nombre?")
```

## Comentarios
Los comentarios sirven para explicar el código y mejorar su legibilidad. En Python, comienzan con `#`.
```{code-cell} ipython3
# Esto es un comentario
num_puntos = 120  # Comentario en línea
```

## Operaciones con variables y tipos de datos
Suma a una variable:
```{code-cell} ipython3
num_features += 20
print("Número de features actualizado:", num_features)
```

Conversión de grados a radianes (útil en geoespacial):
```{code-cell} ipython3
import math
latitud_rad = math.radians(latitud)
print("Latitud en radianes:", latitud_rad)
```

Agregar coordenadas a una lista:
```{code-cell} ipython3
coordenadas.append(40.7128)
coordenadas.append(-74.0060)
print("Coordenadas actualizadas:", coordenadas)
```

Acceso a elementos de un diccionario:
```{code-cell} ipython3
nombre = atributos["nombre"]

## Ejercicios
```

## Ejemplo geoespacial: cálculo de centroide
Supón que tienes una lista de coordenadas y quieres calcular el centroide (punto promedio):
```{code-cell} ipython3
puntos = [
    [19.4, -99.1],
    [40.7128, -74.0060],
    [34.0522, -118.2437],
    [51.5074, -0.1278],
]
centroide_lat = sum([p[0] for p in puntos]) / len(puntos)
centroide_lon = sum([p[1] for p in puntos]) / len(puntos)
centroide = [centroide_lat, centroide_lon]
print("Centroide de los puntos:", centroide)
```

## Ejercicios
1. Crea una lista de tuplas con coordenadas de ciudades que hayas visitado.
2. Calcula el centroide de esas coordenadas.
3. Crea un diccionario para almacenar la latitud y longitud del centroide.

## Resumen
Comprender variables y tipos de datos en Python es esencial para la programación geoespacial. Practica creando y manipulando estos tipos en tus propios ejemplos y proyectos.
1. Crea una lista de tuplas con coordenadas de ciudades que hayas visitado.
2. Calcula el centroide de esas coordenadas.
3. Crea un diccionario para almacenar la latitud y longitud del centroide.

Comprender variables y tipos de datos en Python es esencial para la programación geoespacial. Practica creando y manipulando estos tipos en tus propios ejemplos y proyectos.
