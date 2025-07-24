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


# Estructuras de Datos en Python

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/03_estructuras_datos.ipynb)

## Descripción
Esta sección presenta las estructuras de datos más utilizadas en Python: tuplas, listas, conjuntos y diccionarios, con ejemplos aplicados a datos geoespaciales.

## Objetivos de aprendizaje
- Comprender y utilizar tuplas, listas, conjuntos y diccionarios en Python.
- Aplicar estas estructuras en la manipulación de datos geográficos (coordenadas, trayectorias, atributos, regiones únicas).
- Diferenciar entre estructuras mutables e inmutables y elegir la adecuada para cada tarea.
- Realizar operaciones comunes: indexado, slicing, agregar/eliminar elementos, actualizar valores.
- Usar diccionarios para gestionar atributos de entidades geográficas.

+++

## Tuplas
Las tuplas son secuencias inmutables, útiles para almacenar colecciones fijas como coordenadas.
```{code-cell} ipython3
punto = (
    19.4,
    -99.1,
)  # Tupla representando un punto geográfico (latitud, longitud)
```
Acceso por índice:
```{code-cell} ipython3
latitud = punto[0]
longitud = punto[1]
print(f"Latitud: {latitud}, Longitud: {longitud}")
```

## Listas
Las listas son secuencias ordenadas y mutables. Permiten almacenar trayectorias, límites, o colecciones de puntos.
```{code-cell} ipython3
trayectoria = [
    (19.4, -99.1),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
]
```
Agregar elementos:
```{code-cell} ipython3
trayectoria.append((51.5074, -0.1278))
print("Trayectoria actualizada:", trayectoria)
```
Slicing (sublistas):
```{code-cell} ipython3
print("Subtrayectoria:", trayectoria[:2])
```

## Conjuntos
Los conjuntos son colecciones no ordenadas de elementos únicos. Útiles para regiones o categorías sin duplicados.
```{code-cell} ipython3
regiones = set(["México", "EEUU", "Europa"])
regiones.add("Asia")
regiones.add("Europa")  # No se duplica
print("Regiones:", regiones)
```

## Diccionarios
Los diccionarios almacenan pares clave-valor, ideales para atributos de entidades geográficas.
```{code-cell} ipython3
atributos = {
    "nombre": "Ciudad de México",
    "poblacion": 9000000,
    "coords": [19.4, -99.1],
}
print(atributos)
```
Acceso y actualización de valores:
```{code-cell} ipython3
print(atributos["nombre"])
atributos["poblacion"] = 9500000
print(atributos)
```

## Ejemplo práctico: manipulación de estructuras
Supón que tienes una lista de puntos y quieres obtener solo las latitudes:
```{code-cell} ipython3
puntos = [
    (19.4, -99.1),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]
latitudes = [p[0] for p in puntos]
print(latitudes)
```

## Ejercicios
1. Crea una tupla con las coordenadas de tu ciudad favorita.
2. Crea una lista de trayectorias entre varias ciudades y agrega una más.
3. Usa un conjunto para almacenar países visitados y agrega uno nuevo.
4. Crea un diccionario con atributos de una ciudad y actualiza su población.

## Resumen
Dominar las estructuras de datos de Python es clave para manipular información geoespacial de forma eficiente. Practica con tus propios ejemplos y explora operaciones adicionales como eliminar elementos, comprobar pertenencia (`in`), y combinar estructuras.
