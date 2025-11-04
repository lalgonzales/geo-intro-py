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

# Lab 3

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/labs/lab_03.ipynb)

Este notebook contiene ejercicios basados en las lecciones sobre [**Funciones y Clases**](../python/06_funciones_clases.md) y [**Archivos y Manejo de Excepciones**](../python/07_archivos.md). Estos ejercicios ayudarán a reforzar los conceptos de funciones, clases, manejo de archivos y gestión de excepciones en contextos geoespaciales.

+++

## Ejercicio 1: Calcular distancias con funciones

- Define una función `calcular_distancia` que reciba dos coordenadas geográficas (latitud y longitud) y retorne la distancia entre ellas usando la fórmula de Haversine.
- Usa esta función para calcular la distancia entre múltiples pares de coordenadas.

```{code-cell} ipython3

```

## Ejercicio 2: Cálculo por lotes de distancias

- Crea una función `calculo_lote_distancias` que acepte una lista de pares de coordenadas y retorne una lista de distancias entre pares consecutivos.
- Prueba la función con una lista de coordenadas que representen varias ciudades.

```{code-cell} ipython3

```

## Ejercicio 3: Crear y usar una clase Punto

- Define una clase `Punto` para representar un punto geográfico con atributos `latitud`, `longitud` y `nombre`.
- Agrega un método `distancia_a` que calcule la distancia desde un punto a otro.
- Instancia varios objetos `Punto` y calcula la distancia entre ellos.

```{code-cell} ipython3

```

## Ejercicio 4: Lectura y escritura de archivos

- Escribe una función `leer_coordenadas` que lea un archivo que contenga una lista de coordenadas (latitud, longitud) y las retorne como lista de tuplas.
- Escribe otra función `escribir_coordenadas` que reciba una lista de coordenadas y las escriba en un archivo nuevo.
- Asegúrate de que ambas funciones manejen excepciones, como archivos faltantes o datos mal formateados.

```{code-cell} ipython3

```

## Ejercicio 5: Procesar coordenadas desde archivo

- Crea una función que lea coordenadas de un archivo y use la clase `Punto` para crear objetos `Punto`.
- Calcula la distancia entre cada par consecutivo de puntos y escribe los resultados en un archivo nuevo.
- Asegúrate de que la función maneje excepciones relacionadas con archivos y líneas mal formateadas de manera elegante.

```{code-cell} ipython3
# Crear un archivo de coordenadas de ejemplo
datos_ejemplo = """19.4,-99.1
40.7128,-74.0060
34.0522,-118.2437
-33.8688,151.2093
51.5074,-0.1278"""

archivo_salida = "coordenadas.txt"

try:
    with open(archivo_salida, "w") as archivo:
        archivo.write(datos_ejemplo)
    print(f"Archivo de ejemplo '{archivo_salida}' creado correctamente.")
except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")
```

```{code-cell} ipython3

```

## Ejercicio 6: Manejo de excepciones en procesamiento de datos

- Modifica la función `calculo_lote_distancias` para manejar excepciones que puedan ocurrir durante el cálculo, como coordenadas inválidas.
- Asegúrate de que la función salte los datos inválidos y continúe procesando los datos restantes.

```{code-cell} ipython3

```
