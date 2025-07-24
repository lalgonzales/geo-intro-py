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
Esta sección explica el uso de bucles `for` y `while`, y sentencias de control (`if`, `elif`, `else`) en Python, con ejemplos aplicados a la iteración y procesamiento de datos geográficos.

## Objetivos de aprendizaje
- Utilizar bucles for y while para procesar listas y colecciones de datos.
- Aplicar sentencias de control para tomar decisiones en el flujo del programa.
- Combinar bucles y control de flujo para filtrar, procesar y analizar datos geoespaciales.
- Automatizar tareas repetitivas en flujos de trabajo geográficos.

+++

## Bucles for
Permiten iterar sobre secuencias (listas, tuplas, cadenas) y ejecutar un bloque de código para cada elemento.
```{code-cell} ipython3
coordenadas = [
    (19.4, -99.1),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
]
for lat, lon in coordenadas:
    print(f"Latitud: {lat}, Longitud: {lon}")
```

## Funciones y bucles
Puedes usar funciones dentro de bucles para cálculos repetitivos.
```{code-cell} ipython3
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Ejemplo simple (no geodésico)
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

punto_ref = (0, 0)
for lat, lon in coordenadas:
    distancia = calcular_distancia(punto_ref[0], punto_ref[1], lat, lon)
    print(f"Distancia desde {punto_ref} a ({lat}, {lon}): {distancia:.2f}")
```


## Bucles while
Permiten ejecutar un bloque de código mientras se cumpla una condición. Útiles cuando no sabes cuántas iteraciones serán necesarias.
```{code-cell} ipython3
contador = 0
while contador < len(coordenadas):
    lat, lon = coordenadas[contador]
    print(f"Procesando coordenada: ({lat}, {lon})")
    contador += 1
```

## Sentencias de control: if, elif, else
Permiten tomar decisiones dentro de bucles o funciones.
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
Filtrar datos o aplicar condiciones durante la iteración.
```{code-cell} ipython3
coordenadas = [
    (19.4, -99.1),
    (-34.6, -58.4),
    (40.7128, -74.0060),
    (51.5074, -0.1278),
]
coordenadas_este = []
for lat, lon in coordenadas:
    if lon > 0:
        coordenadas_este.append((lat, lon))
print(f"Coordenadas con longitud positiva: {coordenadas_este}")
```

Contar cuántas coordenadas están en el hemisferio sur:
```{code-cell} ipython3
conteo_sur = 0
for lat, lon in coordenadas:
    if lat < 0:
        conteo_sur += 1
print(f"Cantidad de coordenadas en el hemisferio sur: {conteo_sur}")
```

## Ejercicios
1. Crea una lista de ciudades con sus coordenadas. Usa un for para imprimir solo las que están en el hemisferio norte.
2. Escribe un while que imprima coordenadas hasta encontrar una con latitud menor a 0.
3. Usa un for para indicar si cada coordenada está en el hemisferio este u oeste según la longitud.
4. Combina un for y if para contar cuántas coordenadas están en el hemisferio sur.
5. Escribe un programa que genere coordenadas aleatorias (latitud y longitud) y las imprima hasta que ambas sean mayores a 50.

## Resumen
Dominar bucles y sentencias de control te permitirá automatizar y analizar grandes volúmenes de datos geográficos en Python. Practica combinando estas herramientas en tus propios proyectos.
