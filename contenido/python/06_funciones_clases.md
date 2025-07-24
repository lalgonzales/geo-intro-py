
# Funciones y Clases en Python

<!-- Enlace Colab se agregará tras subir el notebook adaptado -->

## Descripción

Esta sección introduce los conceptos de funciones y clases en Python, enfocándose en su aplicación en la programación geoespacial. Las funciones permiten encapsular código reutilizable y las clases ayudan a organizar datos y operaciones complejas.

## Objetivos de aprendizaje

- Definir y usar funciones para tareas específicas y promover la reutilización de código en aplicaciones geoespaciales.
- Comprender e implementar clases para representar estructuras de datos geográficos complejos.
- Combinar funciones y clases para crear herramientas modulares y escalables.
- Aplicar principios de programación orientada a objetos para organizar y gestionar datos y operaciones geoespaciales.

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

### Parámetros con valores por defecto

```{code-cell} ipython3
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("Alicia"))  # Usa el saludo por defecto
print(saludar("Roberto", "Buen día"))  # Sobrescribe el saludo
```

### Llamando funciones

```{code-cell} ipython3
# Multiplica dos números
def multiplicar(a, b):
    return a * b

# Llamada a la función
resultado = multiplicar(4, 5)
print(f"Resultado de la multiplicación: {resultado}")
```

### Ejemplo geoespacial: función Haversine

La fórmula de Haversine calcula la distancia entre dos puntos en la superficie de la Tierra.

```{code-cell} ipython3
from math import radians, sin, cos, sqrt, atan2

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
print(f"Distancia: {haversine(19.4, -99.1, 40.7128, -74.0060):.2f} km")
# Ejemplo de uso en millas (radio ≈ 3958.8)
print(f"Distancia: {haversine(19.4, -99.1, 40.7128, -74.0060, radio=3958.8):.2f} millas")
```

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

```{code-cell} ipython3
def promedio(*numeros):
    return sum(numeros) / len(numeros)

print(promedio(10, 20, 30))
print(promedio(5, 15, 25, 35))
```

### Función con argumentos nombrados

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

```{code-cell} ipython3
class Punto:
    def __init__(self, latitud, longitud, nombre="Sin nombre"):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
```

## Combinando funciones y clases

Puedes usar funciones dentro de clases para crear herramientas geoespaciales más potentes y flexibles. Por ejemplo, una clase Ruta que calcula la distancia total al recorrer una serie de puntos:

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
            total += self.puntos[i].distancia_a(self.puntos[i + 1])
        return total

ruta = Ruta([p1, p2])
print(f"Distancia total: {ruta.distancia_total():.2f} km")
```

## Ejercicios
1. Escribe una función `convertir_distancia` que convierta distancias de kilómetros a millas y viceversa. El parámetro `unidad` debe tener valor por defecto "km".
2. Escribe una función `sumar_coordenadas` que acepte varios pares de coordenadas y devuelva la suma de todas las latitudes y longitudes.
3. Extiende la clase `Punto` para incluir un método `mover` que ajuste la latitud y longitud por una cantidad dada.
4. Crea una clase `Rectangulo` que acepte dos objetos `Punto` como esquinas y calcule el área.

## Resumen
Las funciones y clases permiten estructurar y reutilizar código en proyectos geoespaciales. Dominar estos conceptos te ayudará a crear herramientas modulares y eficientes para el análisis y procesamiento de datos geográficos.
