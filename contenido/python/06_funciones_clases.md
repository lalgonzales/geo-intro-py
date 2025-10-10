
# Funciones y Clases en Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lalgonzales/geo-intro-py/blob/main/contenido/python/06_funciones_clases.ipynb)

## Descripción

Esta lección introduce los conceptos de funciones y clases en Python, enfocándose en su aplicación en la programación geoespacial. Las funciones permiten encapsular código en bloques reutilizables, haciendo que tus scripts sean más modulares y fáciles de mantener. Las clases proporcionan una forma de crear estructuras de datos complejas al agrupar datos y funcionalidad. Al comprender y aplicar estos conceptos, podrás construir herramientas de análisis geoespacial más sofisticadas y eficientes.

## Objetivos de aprendizaje

- Definir y usar funciones para tareas específicas y promover la reutilización de código en aplicaciones geoespaciales.
- Comprender e implementar clases para representar estructuras de datos geográficos complejos, como características geográficas.
- Combinar funciones y clases para crear herramientas modulares y escalables.
- Aplicar principios de programación orientada a objetos para organizar y gestionar datos y operaciones geoespaciales de manera efectiva.
- Desarrollar las habilidades para extender clases existentes y crear nuevas adaptadas a tareas geoespaciales específicas.

---

## Funciones

Las funciones son bloques de código que realizan una tarea específica y pueden reutilizarse varias veces. Permiten estructurar el código de manera eficiente y reducir la redundancia.

### Definición de una función simple

```{code-cell} ipython3
# Suma dos números
def sumar(a, b):
    return a + b

# Ejemplo de uso
resultado = sumar(5, 3)
print(f"Resultado: {resultado}")
```

Esta función toma dos parámetros `a` y `b`, y devuelve su suma. Puedes llamarla pasando dos valores como argumentos.

### Parámetros con valores por defecto

A veces, es posible que desees que una función tenga parámetros opcionales con valores por defecto. Puedes especificar un valor por defecto asignándolo en la definición de la función.

```{code-cell} ipython3
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("Alicia"))  # Usa el saludo por defecto
print(saludar("Roberto", "Buen día"))  # Sobrescribe el saludo
```

En este ejemplo, el parámetro `saludo` tiene un valor por defecto de `"Hola"`. Si no proporcionas un segundo argumento, la función usará este valor por defecto. Si proporcionas uno, sobrescribirá el valor por defecto.

### Llamando funciones

Para llamar a una función, simplemente usa su nombre seguido de paréntesis que contengan los argumentos que deseas pasar. Por ejemplo:

```{code-cell} ipython3
# Multiplica dos números
def multiplicar(a, b):
    return a * b

# Llamada a la función
resultado = multiplicar(4, 5)
print(f"Resultado de la multiplicación: {resultado}")
```

Puedes llamar a la función `multiplicar` con dos números, y devolverá su producto.

### Ejemplo geoespacial: función Haversine

La fórmula de Haversine calcula la distancia entre dos puntos en la superficie de la Tierra.

![](https://upload.wikimedia.org/wikipedia/commons/c/cb/Illustration_of_great-circle_distance.svg)

```{code-cell} ipython3
from math import radians, sin, cos, sqrt, atan2
```

```{code-cell} ipython3
def haversine(lat1, lon1, lat2, lon2):
    radio = 6371.0  # Radio de la Tierra en kilómetros
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = radio * c
    return distancia

# Ejemplo de uso
distancia = haversine(19.4, -99.1, 40.7128, -74.0060)
print(f"Distancia: {distancia:.2f} km")
```

### Función con valores por defecto y aplicación geoespacial

Ahora modifiquemos la función haversine para aceptar un parámetro opcional del radio de la Tierra, que tiene un valor por defecto para kilómetros pero puede configurarse para otras unidades como millas.

```{code-cell} ipython3
def haversine(lat1, lon1, lat2, lon2, radio=6371.0):
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = radio * c
    return distancia

# Ejemplo de uso en kilómetros
distancia_km = haversine(19.4, -99.1, 40.7128, -74.0060)
print(f"Distancia en kilómetros: {distancia_km:.2f} km")

# Ejemplo de uso en millas (radio de la Tierra ≈ 3958.8 millas)
distancia_millas = haversine(19.4, -99.1, 40.7128, -74.0060, radio=3958.8)
print(f"Distancia en millas: {distancia_millas:.2f} millas")
```

En este ejemplo, el parámetro `radio` tiene un valor por defecto de 6371.0 para kilómetros, pero puedes especificar 3958.8 si quieres la distancia en millas.

Ahora, creemos una función que tome una lista de pares de coordenadas y devuelva una lista de distancias entre puntos consecutivos.

### Procesamiento por lotes: lista de distancias

```{code-cell} ipython3
def batch_haversine(lista_coords):
    distancias = []
    for i in range(len(lista_coords) - 1):
        lat1, lon1 = lista_coords[i]
        lat2, lon2 = lista_coords[i + 1]
        distancia = haversine(lat1, lon1, lat2, lon2)
        distancias.append(distancia)
    return distancias

# Ejemplo de uso
coordenadas = [(19.4, -99.1), (40.7128, -74.0060), (34.0522, -118.2437)]
print(f"Distancias: {batch_haversine(coordenadas)}")
```

### Función con argumentos variables

También puedes crear funciones que acepten un número variable de argumentos usando `*args`.

```{code-cell} ipython3
def promedio(*numeros):
    return sum(numeros) / len(numeros)

print(promedio(10, 20, 30))
print(promedio(5, 15, 25, 35))
```

En Python, puedes usar `**kwargs` (abreviatura de "keyword arguments") en las definiciones de funciones para pasar un número variable de argumentos nombrados. Esto te permite manejar un conjunto flexible de parámetros en una función.

Vamos a crear un ejemplo que demuestra cómo usar `**kwargs` en una función:

```{code-cell} ipython3
def describir_punto(latitud, longitud, **kwargs):
    descripcion = f"Punto en ({latitud}, {longitud})"
    for clave, valor in kwargs.items():
        descripcion += f", {clave}: {valor}"
    return descripcion

print(describir_punto(19.4, -99.1, nombre="CDMX", poblacion=9000000))
print(describir_punto(40.7128, -74.0060, nombre="NYC", estado="NY"))
```

---

## Clases

Las clases son plantillas para crear objetos, que pueden tener atributos (datos) y métodos (funciones). Ayudan a representar estructuras de datos más complejas.

### Definición de una clase simple

```{code-cell} ipython3
class Punto:
    def __init__(self, latitud, longitud, nombre=None):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre or 'Punto'} ({self.latitud}, {self.longitud})"

# Ejemplo de uso
p1 = Punto(19.4, -99.1, "CDMX")
print(p1)
```

### Agregando métodos a la clase

Puedes agregar métodos a la clase para realizar operaciones en los atributos.

```{code-cell} ipython3
class Punto:
    def __init__(self, latitud, longitud, nombre=None):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre

    def distancia_a(self, otro_punto):
        return haversine(self.latitud, self.longitud, otro_punto.latitud, otro_punto.longitud)

# Ejemplo de uso
p1 = Punto(19.4, -99.1, "CDMX")
p2 = Punto(40.7128, -74.0060, "NYC")
print(f"Distancia de {p1.nombre} a {p2.nombre}: {p1.distancia_a(p2):.2f} km")
```

### Constructor con valores por defecto

También puedes usar valores por defecto en el constructor de una clase.

```{code-cell} ipython3
class Punto:
    def __init__(self, latitud, longitud, nombre="Sin nombre"):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
```

## Combinando funciones y clases

Puedes usar funciones dentro de clases para crear herramientas geoespaciales más potentes y flexibles. Por ejemplo, al incorporar cálculos de distancia, podemos hacer que la clase `Punto` sea mucho más versátil.

Vamos a crear un método en la clase `Punto` que calcula la distancia total al viajar a través de una serie de puntos.

```{code-cell} ipython3
class Ruta:
    def __init__(self, puntos):
        self.puntos = puntos

    def distancia_total(self):
        total = 0
        for i in range(len(self.puntos) - 1):
            total += self.puntos[i].distancia_a(self.puntos[i + 1])
        return total

# Ejemplo de uso
ruta = Ruta([p1, p2])
print(f"Distancia total: {ruta.distancia_total():.2f} km")
```

---

## Ejercicios
1. Escribe una función `convertir_distancia` que convierta distancias de kilómetros a millas y viceversa. La función debe aceptar dos parámetros: `distancia` y `unidad`, donde `unidad` tiene valor por defecto "km". Si la unidad es "km", convierte a millas; si es "millas", convierte a kilómetros.
2. Escribe una función `sumar_coordenadas` que acepte varios pares de coordenadas (tuplas) y devuelva la suma de todas las latitudes y longitudes.
3. Extiende la clase `Punto` para incluir un método `mover` que ajuste la latitud y longitud por una cantidad dada. Por ejemplo, si llamas `mover(1, -1)`, debe aumentar la latitud en 1 y disminuir la longitud en 1.
4. Crea una clase `Rectangulo` que acepte dos objetos `Punto` como esquinas y calcule el área. La clase debe incluir un método `area` que devuelva el área del rectángulo, asumiendo que las coordenadas están en el mismo sistema.

## Resumen

Las funciones y clases permiten estructurar y reutilizar código en proyectos geoespaciales. Dominar estos conceptos te ayudará a crear herramientas modulares y eficientes para el análisis y procesamiento de datos geográficos.
