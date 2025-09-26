---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Lab 2: Manipulación de Cadenas y Control de Flujo en Python

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/labs/lab_02.ipynb)

Este notebook contiene ejercicios basados en las lecciones sobre [**Operaciones con Cadenas en Python**](../python/04_operaciones_cadenas.md) y [**Bucles y Sentencias de Control en Python**](../python/05_bucles.md). Estos ejercicios ayudarán a reforzar los conceptos de manipulación de cadenas, bucles y condicionales en contextos geoespaciales.

+++

## Ejercicio 1: Manipulación de cadenas geográficas

- Crea una cadena con el nombre de un elemento geográfico (ejemplo: `"Río Ulúa"`).
- Convierte la cadena a minúsculas y luego a mayúsculas.
- Concatenar la cadena con el país (ejemplo: `"Honduras"`) para formar el nombre completo.
- Repite la cadena tres veces, separando cada repetición con un guion (`-`).

```{code-cell} ipython3

```

## Ejercicio 2: Extracción y formato de coordenadas

- Dada una cadena con el formato "latitud, longitud" (ejemplo: "14.0650N, 87.1715W"), extrae los valores numéricos.
- Convierte los valores a float y elimina los indicadores de dirección (N, S, E, W).
- Formatea las coordenadas en una cadena WKT tipo `POINT` (ejemplo: "POINT(-87.1715 14.0650)").

```{code-cell} ipython3

```

## Ejercicio 3: Construcción dinámica de consultas SQL

- Dado un nombre de tabla y una condición, construye dinámicamente una consulta SQL.
- Ejemplo: Si `tabla = "ciudades"` y `condicion = "poblacion > 1000000"`, la consulta debe ser `SELECT * FROM ciudades WHERE poblacion > 1000000;`.
- Agrega condiciones adicionales dinámicamente usando `AND`.

```{code-cell} ipython3

```

## Ejercicio 4: Normalización y limpieza de cadenas

- Dada una lista de nombres de ciudades con formato inconsistente (ejemplo: `[" tegucigalpa ", "SAN PEDRO SULA", "   LA CEIBA"]`), normaliza los nombres:
  - Elimina espacios al inicio y final.
  - Convierte a formato título ("Tegucigalpa", "San Pedro Sula", "La Ceiba").
- El resultado debe ser una lista limpia de nombres de ciudades.

```{code-cell} ipython3

```

## Ejercicio 5: Parseo y extracción de direcciones

- Dada una cadena con el formato "Calle, Ciudad, País" (ejemplo: "Calle Real, Tegucigalpa, Honduras"), escribe una función que la convierta en un diccionario con claves `calle`, `ciudad` y `pais`.
- El resultado debe ser: `{"calle": "Calle Real", "ciudad": "Tegucigalpa", "pais": "Honduras"}`.

```{code-cell} ipython3

```

## Ejercicio 6: Uso de for para procesar coordenadas

- Crea una lista de tuplas con coordenadas (latitud, longitud).
- Usa un bucle `for` para imprimir cada coordenada e indicar si está en el hemisferio norte o sur según la latitud.

```{code-cell} ipython3

```

## Ejercicio 7: Uso de while para procesamiento iterativo

- Crea una lista de coordenadas (latitud, longitud).
- Usa un bucle `while` que imprima cada coordenada hasta encontrar una con latitud negativa. Detén el bucle en ese punto.

```{code-cell} ipython3

```

## Ejercicio 8: Lógica condicional en bucles

- Crea una lista de coordenadas y recórrela con un `for`.
- Usa un `if-elif-else` para clasificar cada coordenada según la longitud:
  - Imprime "Hemisferio Este" si la longitud es mayor a 0.
  - Imprime "Hemisferio Oeste" si la longitud es menor a 0.

```{code-cell} ipython3

```

## Ejercicio 9: Filtrado de datos con bucles y condicionales

- Dada una lista de coordenadas, filtra y almacena solo las que estén en el hemisferio sur (latitud < 0).
- Cuenta cuántas cumplen la condición e imprime el resultado.

```{code-cell} ipython3

```

## Ejercicio 10: Generación y análisis de coordenadas aleatorias

- Escribe un programa que genere coordenadas aleatorias (latitud entre [-90, 90], longitud entre [-180, 180]).
- Usa un bucle `while` para seguir generando hasta obtener una coordenada donde latitud y longitud sean mayores a 50.
- Imprime cada coordenada generada y la final que cumple la condición.

```{code-cell} ipython3

```
