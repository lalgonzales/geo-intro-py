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

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/05_looping.ipynb)

# Bucles y Sentencias de Control en Python

## Descripción

Esta sección introduce los bucles y sentencias de control en Python, con énfasis en aplicaciones geoespaciales. Aprenderás a automatizar tareas repetitivas y tomar decisiones basadas en condiciones de datos, fundamentales para procesar grandes volúmenes de información geográfica.

## Objetivos de aprendizaje

- Implementar bucles `for` para iterar sobre secuencias como listas y tuplas.
- Usar bucles `while` para ejecutar tareas hasta que se cumpla una condición.
- Aplicar sentencias de control (`if`, `elif`, `else`) para ejecutar bloques de código según condiciones.
- Combinar bucles y sentencias de control para filtrar y analizar datos geoespaciales.
- Automatizar tareas repetitivas en flujos de trabajo geográficos.

+++

## Ejemplo básico de bucle for

```{code-cell} ipython3
coordenadas = [
    (19.4, -99.1),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
]  # Lista de tuplas (latitud, longitud)

for lat, lon in coordenadas:
    print(f"Latitud: {lat}, Longitud: {lon}")
```

## Ejemplo de cálculo en bucle

```{code-cell} ipython3
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula simplificada (Euclídea)
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

referencia = (0, 0)

for lat, lon in coordenadas:
    distancia = calcular_distancia(referencia[0], referencia[1], lat, lon)
    print(f"Distancia desde {referencia} a ({lat}, {lon}): {distancia:.2f}")
```

## Uso de bucle while

```{code-cell} ipython3
contador = 0
while contador < 3:
    print(f"Iteración {contador}")
    contador += 1
```

## Sentencias de control

```{code-cell} ipython3
valor = 15
if valor < 10:
    print("Menor que 10")
elif valor < 20:
    print("Entre 10 y 20")
else:
    print("20 o más")
```

## Ejercicios

1. Itera sobre una lista de nombres de ciudades y muestra cada una en mayúsculas.
2. Calcula la distancia entre un punto de referencia y una lista de coordenadas usando un bucle.
3. Usa un bucle `while` para sumar números hasta superar 100.
4. Filtra una lista de ubicaciones y muestra solo las que están en México usando sentencias de control.
5. Escribe una función que reciba una lista de coordenadas y devuelva otra lista con las cadenas WKT `POINT` correspondientes.

## Resumen

Los bucles y sentencias de control son herramientas clave para automatizar y analizar datos geoespaciales en Python. Dominar estos conceptos te permitirá procesar grandes volúmenes de información y tomar decisiones programáticas en tus proyectos geográficos.
