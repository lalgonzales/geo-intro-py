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
En esta lección exploraremos las estructuras de datos fundamentales de Python: tuplas, listas, conjuntos y diccionarios. Estas estructuras son herramientas esenciales en la programación geoespacial, ya que permiten almacenar, gestionar y manipular distintos tipos de datos de manera eficiente. Al dominar estas estructuras, podrás trabajar con conjuntos de datos geoespaciales complejos y realizar análisis avanzados.

## Objetivos de aprendizaje
- Comprender las características y casos de uso de tuplas, listas, conjuntos y diccionarios en Python.
- Aplicar estas estructuras para almacenar y manipular datos geográficos, como coordenadas, trayectorias y atributos.
- Diferenciar entre estructuras mutables e inmutables y elegir la adecuada para cada tarea geoespacial.
- Realizar operaciones comunes: indexado, slicing, agregar/eliminar elementos y actualizar valores.
- Utilizar diccionarios para gestionar atributos de entidades geográficas y entender la importancia de los pares clave-valor.

+++


## Tuplas

Las tuplas son secuencias inmutables, es decir, una vez creadas no se pueden modificar. Son útiles para almacenar colecciones fijas de elementos, como las coordenadas de un punto geográfico (latitud, longitud).

```{code-cell} ipython3
punto = (
    19.4,
    -99.1,
)  # Tupla representando un punto geográfico (latitud, longitud)
```

Puedes acceder a los elementos de una tupla usando índices:

```{code-cell} ipython3
latitud = punto[0]
longitud = punto[1]
print(f"Latitud: {latitud}, Longitud: {longitud}")
```


## Listas

Las listas son secuencias ordenadas y mutables, lo que significa que puedes cambiar, agregar o eliminar elementos después de su creación. Son muy flexibles y pueden almacenar distintos tipos de datos, por ejemplo, una lista de coordenadas que representa una trayectoria o límite.

```{code-cell} ipython3
trayectoria = [
    (19.4, -99.1),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
]
```

Puedes agregar un nuevo punto a la trayectoria:

```{code-cell} ipython3
trayectoria.append((51.5074, -0.1278))
print("Trayectoria actualizada:", trayectoria)
```

Las listas permiten realizar operaciones como slicing, que te permite acceder a una sublista:

```{code-cell} ipython3
subtrayectoria = trayectoria[:2]
print("Subtrayectoria:", subtrayectoria)
```


## Conjuntos

Los conjuntos son colecciones no ordenadas de elementos únicos. Son útiles cuando necesitas almacenar elementos sin duplicados, por ejemplo, regiones geográficas visitadas en una encuesta.

```{code-cell} ipython3
regiones = ["México", "EEUU", "Europa"]
regiones = set(regiones)
```

Puedes agregar una nueva región al conjunto:

```{code-cell} ipython3
regiones.add("Asia")
print("Regiones actualizadas:", regiones)
```

Si intentas agregar una región que ya existe, el conjunto no cambiará:

```{code-cell} ipython3
regiones.add("Europa")  # Intento de duplicado
print("Regiones tras intentar duplicado:", regiones)
```


## Diccionarios

Los diccionarios son colecciones de pares clave-valor, donde cada clave es única. Son muy útiles para almacenar datos asociados a identificadores específicos, como los atributos de una ciudad.

```{code-cell} ipython3
atributos_ciudad = {
    "nombre": "Ciudad de México",
    "poblacion": 9000000,
    "coordenadas": (19.4, -99.1),
}  # Diccionario con atributos de una ciudad
print(atributos_ciudad)
```

Puedes acceder a los valores asociados a una clave:

```{code-cell} ipython3
nombre_ciudad = atributos_ciudad["nombre"]
poblacion_ciudad = atributos_ciudad["poblacion"]
print(f"Ciudad: {nombre_ciudad}, Población: {poblacion_ciudad}")
```

También puedes agregar o actualizar pares clave-valor:

```{code-cell} ipython3
atributos_ciudad["area_km2"] = 1485  # Ejemplo: área de la ciudad en km²
print("Atributos de la ciudad actualizados:", atributos_ciudad)
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
5. Crea un diccionario para almacenar atributos de una entidad geográfica (por ejemplo, un río o una montaña). Incluye claves para el nombre, longitud y ubicación. Luego, agrega un atributo adicional (por ejemplo, la fuente del río o la altura de la montaña) y muestra el diccionario.

```{code-cell} ipython3
# Ejemplo de ejercicio adicional
rio = {
    "nombre": "Río Bravo",
    "longitud_km": 3034,
    "ubicacion": "Norte de México y sur de EEUU",
}
rio["fuente"] = "Montañas de San Juan"
print(rio)
```

## Resumen

Dominar y utilizar las estructuras de datos de Python como tuplas, listas, conjuntos y diccionarios es fundamental en la programación geoespacial. Estas estructuras ofrecen flexibilidad y funcionalidad para gestionar y manipular datos espaciales de manera eficiente.

Continúa explorando estas estructuras aplicándolas en tus propios proyectos y análisis geoespaciales.
