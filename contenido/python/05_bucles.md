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


[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/05_bucles.ipynb)

# Bucles y Sentencias de Control en Python

## Descripción
Esta sección introduce bucles y sentencias de control en Python, enfocándose en sus aplicaciones en la programación geoespacial. Los bucles y sentencias de control son herramientas esenciales para automatizar tareas repetitivas, tomar decisiones basadas en condiciones de datos y procesar eficientemente grandes conjuntos de datos geoespaciales. Al dominar estos conceptos, podrás manejar tareas de análisis geoespacial complejas con mayor eficiencia y precisión.

## Objetivos de aprendizaje
- Utilizar bucles for y while para procesar listas y colecciones de datos.
- Aplicar sentencias de control para tomar decisiones en el flujo del programa.
- Combinar bucles y control de flujo para filtrar, procesar y analizar datos geoespaciales.
- Automatizar tareas repetitivas en flujos de trabajo geográficos.
- Desarrollar la capacidad para automatizar tareas repetitivas geoespaciales, haciendo que tus flujos de trabajo de procesamiento de datos sean más eficientes.

+++

## Bucles for
Los bucles for permiten iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código para cada elemento de la secuencia. Esto es particularmente útil en la programación geoespacial cuando necesitas procesar múltiples características o coordenadas.
```{code-cell} ipython3
coordenadas = [
    (35.6895, 139.6917),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]
for lat, lon in coordenadas:
    print(f"Latitud: {lat}, Longitud: {lon}")
```

Asumiendo que tienes una función para calcular distancias, puedes usar un bucle para calcular distancias desde un punto de referencia.
```{code-cell} ipython3
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Placeholder para lógica de cálculo de distancia
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

punto_ref = (0, 0)
for lat, lon in coordenadas:
    distancia = calcular_distancia(punto_ref[0], punto_ref[1], lat, lon)
    print(f"Distancia desde {punto_ref} a ({lat}, {lon}): {distancia:.2f}")
```

## Bucles while
Los bucles while continúan ejecutando un bloque de código mientras se cumpla una condición especificada. Son útiles cuando el número de iteraciones no se conoce de antemano, como cuando se procesan datos hasta que se cumple una cierta condición.
```{code-cell} ipython3
contador = 0
while contador < len(coordenadas):
    lat, lon = coordenadas[contador]
    print(f"Procesando coordenada: ({lat}, {lon})")
    contador += 1
```

## Sentencias de control: if, elif, else
Las sentencias de control permiten ejecutar diferentes bloques de código basados en ciertas condiciones. En la programación geoespacial, esto es útil para manejar diferentes tipos de datos o condiciones.
```{code-cell} ipython3
for lat, lon in coordenadas:
    if lat > 0:
        print(f"{lat}, {lon} está en el hemisferio norte")
    elif lat < 0:
        print(f"{lat}, {lon} está en el hemisferio sur")
    else:
        print(f"{lat}, {lon} está cerca del ecuador")
```

### Clasificación adicional por longitud
```{code-cell} ipython3
for lat, lon in coordenadas:
    if lat > 0:
        hemisferio = "Norte"
    else:
        hemisferio = "Sur"
    if lon > 0:
        direccion = "Este"
    else:
        direccion = "Oeste"
    print(f"La coordenada ({lat}, {lon}) está en el hemisferio {hemisferio} y {direccion}.")
```

## Combinando bucles y control de flujo
Puedes combinar bucles y sentencias de control para realizar operaciones más complejas, como filtrar datos o aplicar condiciones durante la iteración.
```{code-cell} ipython3
coordenadas_filtradas = []
for lat, lon in coordenadas:
    if lon > 0:
        coordenadas_filtradas.append((lat, lon))
print(f"Coordenadas filtradas (solo con longitud positiva): {coordenadas_filtradas}")
```

```{code-cell} ipython3
conteo_sur = 0
for lat, lon in coordenadas:
    if lat < 0:
        conteo_sur += 1
print(f"Número de coordenadas en el hemisferio sur: {conteo_sur}")
```

## Ejercicios
1. Crea una lista de ciudades con sus coordenadas. Usa un for para imprimir solo las que están en el hemisferio norte.
2. Escribe un while que imprima coordenadas hasta encontrar una con latitud menor a 0.
3. Usa un for para indicar si cada coordenada está en el hemisferio este u oeste según la longitud.
4. Combina un for y if para contar cuántas coordenadas están en el hemisferio sur.
5. Escribe un programa que genere coordenadas aleatorias (latitud y longitud) y las imprima hasta que ambas sean mayores a 50.

## Resumen
Los bucles y sentencias de control son herramientas fundamentales en la programación geoespacial. Permiten procesar y analizar datos geográficos de manera eficiente automatizando tareas repetitivas y aplicando lógica basada en condiciones de datos. Practica estos conceptos aplicándolos a tus conjuntos de datos y análisis geoespaciales.
