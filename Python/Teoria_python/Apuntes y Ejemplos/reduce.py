# Explicación de la función reduce() en Python
# La función reduce() se utiliza para aplicar una función de manera acumulativa a los elementos de una secuencia (como listas, tuplas, etc.),
# reduciendo la secuencia a un solo valor.

from functools import reduce  # Importar reduce desde functools en Python 3

## Ejemplo 1 - Suma acumulativa

numeros = [1, 2, 3, 4, 5]

suma_total = reduce(lambda x, y: x + y, numeros)  # Sumar todos los números de la lista de manera acumulativa

print(f"Ejemplo 1: Suma total: {suma_total}")  # Se imprimirá la suma acumulativa de los números, que es 15

## Ejemplo 2 - Producto acumulativo

def multiplicar(x, y):
    return x * y

productos = [2, 3, 4, 5]

producto_total = reduce(multiplicar, productos)  # Multiplicar todos los números de la lista de manera acumulativa

print(f"Ejemplo 2: Producto total: {producto_total}")  # Se imprimirá el producto acumulativo de los números, que es 120

## Ejemplo 3 - Concatenación acumulativa de cadenas

palabras = ["Python", "es", "genial"]

concatenacion = reduce(lambda x, y: x + " " + y, palabras)  # Concatenar todas las palabras de la lista de manera acumulativa

print(f"Ejemplo 3: Concatenación: {concatenacion}")  # Se imprimirá la cadena resultante de la concatenación, "Python es genial"

## Ejemplo 4 - Encontrar el máximo de una lista

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

maximo = reduce(lambda x, y: x if x > y else y, numeros)  # Encontrar el máximo número de la lista de manera acumulativa

print(f"Ejemplo 4: Máximo número: {maximo}")  # Se imprimirá el número máximo de la lista, que es 9

