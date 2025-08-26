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


# Lab 1: Variables, Estructuras de Datos y Operaciones Básicas

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/labs/lab_01.ipynb)

**Lecciones relacionadas:**
- [Introducción](../python/01_introduccion.md)
- [Variables y Tipos de Datos](../python/02_variables.md)
- [Estructuras de Datos en Python](../python/03_estructuras_datos.md)

+++

## Ejercicio 1: Asignación de variables y operaciones básicas

Crea variables para almacenar los siguientes datos geoespaciales:

- Latitud y longitud de Nueva York: 40.7128, -74.0060.
- Población de Nueva York: 8,336,817.
- Área de Nueva York en km²: 783.8.

Realiza lo siguiente:

1. Calcula e imprime la densidad de población (hab/km²).
2. Imprime las coordenadas en el formato "Latitud: [lat], Longitud: [lon]".

```{code-cell} ipython3

```

## Ejercicio 2: Operaciones con cadenas

Crea una variable string con el nombre de una ciudad, por ejemplo "San Francisco". Realiza:

1. Convierte la cadena a minúsculas e imprímela.
2. Convierte la cadena a mayúsculas e imprímela.
3. Reemplaza "San" por "Los" e imprime el nuevo nombre.

```{code-cell} ipython3

```

## Ejercicio 3: Uso de listas

Crea una lista de tuplas, cada una con el nombre de una ciudad y su latitud y longitud:

- Nueva York: (40.7128, -74.0060)
- Los Ángeles: (34.0522, -118.2437)
- Chicago: (41.8781, -87.6298)

Realiza:

1. Agrega Miami: (25.7617, -80.1918).
2. Imprime la lista completa.
3. Imprime solo las dos primeras ciudades.

```{code-cell} ipython3

```

## Ejercicio 4: Uso de tuplas

Crea una tupla con las coordenadas de la Torre Eiffel: (48.8584, 2.2945). Realiza:

1. Accede e imprime latitud y longitud.
2. Intenta cambiar la latitud a 48.8585. ¿Qué sucede? Explica.

```{code-cell} ipython3

```

## Ejercicio 5: Uso de sets

Crea un set de países visitados, por ejemplo {"USA", "Francia", "Alemania"}. Realiza:

1. Agrega un país nuevo.
2. Intenta agregar el mismo país otra vez. ¿Qué sucede?
3. Imprime el set actualizado.

```{code-cell} ipython3

```

## Ejercicio 6: Uso de diccionarios

Crea un diccionario con información de un río:

- Nombre: "Amazonas"
- Longitud: 6400 km
- Países: ["Brasil", "Perú", "Colombia"]

Realiza:

1. Agrega el caudal promedio (ej. 209,000 m³/s).
2. Actualiza la longitud a 6992 km.
3. Imprime el diccionario.

```{code-cell} ipython3

```

## Ejercicio 7: Estructuras anidadas

Crea un diccionario para una ciudad con nombre, población y coordenadas:

- Nombre: "Tokio"
- Población: 13,515,271
- Coordenadas: (35.6895, 139.6917)

Realiza:

1. Imprime la población.
2. Imprime la latitud.
3. Actualiza la población a 14,000,000 e imprime el diccionario.

```{code-cell} ipython3

```

## Ejercicio 8: Operaciones con listas

Usando la lista de ciudades del Ejercicio 3:

1. Ordena la lista alfabéticamente por nombre.
2. Crea una lista solo con los nombres de las ciudades.
3. Elimina la última ciudad e imprime la lista actualizada.

```{code-cell} ipython3

```

## Ejercicio 9: Operaciones con diccionarios

Usando el diccionario del Ejercicio 6:

1. Verifica si la clave "Longitud" existe.
2. Imprime todas las claves.
3. Imprime todos los valores.

```{code-cell} ipython3

```

## Ejercicio 10: Aplicación práctica

Dada una lista de tuplas con nombre, latitud y longitud:

```{code-cell} ipython3
locations = [
    ("Monte Everest", 27.9881, 86.9250),
    ("K2", 35.8808, 76.5155),
    ("Kangchenjunga", 27.7025, 88.1475)
]
```

Realiza:

1. Crea una lista solo con los nombres.
2. Crea un diccionario con nombre como clave y coordenadas como valor.
3. Imprime la latitud de "K2" usando el diccionario.

```{code-cell} ipython3

```
