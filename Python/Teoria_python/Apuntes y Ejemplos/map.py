# Explicación función map()
# La función map() en Python se utiliza para aplicar una función a cada uno de los elementos de un iterable (como una lista o una tupla) y 
# devolver un nuevo iterable con los resultados. 
# Es especialmente útil para realizar transformaciones o cálculos sobre colecciones de datos sin la necesidad de escribir bucles explícitos.

## Ejemplo 1 - Uso básico

def cuadrado(n):                       # Definición de la función cuadrado
    return n * n

numeros = [1, 2, 3, 4]                 # Definición de una lista de números
resultado = map(cuadrado, numeros)     # Uso de la función map() para aplicar 'cuadrado' a cada elemento de 'numeros'

print(f"Ejemplo 1: {list(resultado)}") # Se imprimirá una lista con los cuadrados de cada número

## Ejemplo 2 - Uso con lambda

numeros = [1, 2, 3, 4]                     # Definición de una lista de números
resultado = map(lambda x: x * x, numeros)  # Uso de la función map() con una función lambda para calcular el cuadrado

print(f"Ejemplo 2: {list(resultado)}")     # Se imprimirá una lista con los cuadrados de cada número

## Ejemplo 3 - Uso con múltiples iterables

lista1 = [1, 2, 3]                                  # Definición de dos listas de números
lista2 = [4, 5, 6]

resultado = map(lambda x, y: x + y, lista1, lista2) # Uso de la función map() con una función lambda para sumar elementos de las listas

print(f"Ejemplo 3: {list(resultado)}")              # Se imprimirá una lista con las sumas de los elementos correspondientes de lista1 y lista2

## Ejemplo 4 - Convertir tipos de datos

numeros_str = ['1', '2', '3', '4']         # Definición de una lista de números como cadenas de texto
numeros = map(int, numeros_str)            # Uso de la función map() para convertir cada cadena a entero

print(f"Ejemplo 4: {list(numeros)}")       # Se imprimirá una lista de enteros

## Ejemplo 5 - Filtrar valores con map() y lambda

numeros = [1, 2, 3, 4, 5, 6]                                  # Definición de una lista de números

resultado = map(lambda x: x if x % 2 == 0 else None, numeros) # Uso de la función map() para transformar cada número en sí mismo si es par, o en None si es impar

print(f"Ejemplo 5: {list(resultado)}")                        # Se imprimirá una lista donde los números impares son reemplazados por None
