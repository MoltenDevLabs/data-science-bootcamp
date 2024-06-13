# Explicación funciones lambda
# Las funciones lambda en Python son funciones anónimas, es decir, funciones que no tienen un nombre explícito. 
# Se utilizan para crear funciones pequeñas y de una sola línea de forma concisa. La sintaxis básica de una función lambda es:
# lambda argumentos: expresión

## Ejemplo 1 - Uso básico

cuadrado = lambda x: x * x          # Definición de una función lambda que calcula el cuadrado de un número

print(f"Ejemplo 1: {cuadrado(5)}")  # Se imprimirá 25, que es el cuadrado de 5

## Ejemplo 2 - Múltiples argumentos

suma = lambda x, y: x + y          # Definición de una función lambda que suma dos números

print(f"Ejemplo 2: {suma(3, 7)}")  # Se imprimirá 10, que es la suma de 3 y 7

## Ejemplo 3 - Uso con map() *** IMPORTANTE ***

numeros = [1, 2, 3, 4]                     # Definición de una lista de números
cuadrados = map(lambda x: x * x, numeros)  # Uso de la función lambda con map() para calcular el cuadrado de cada número

print(f"Ejemplo 3: {list(cuadrados)}")     # Se imprimirá una lista con los cuadrados de cada número

## Ejemplo 4 - Uso con filter()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # Definición de una lista de números

pares = filter(lambda x: x % 2 == 0, numeros) # Uso de la función lambda con filter() para obtener solo los números pares

print(f"Ejemplo 4: {list(pares)}")            # Se imprimirá una lista con los números pares [2, 4, 6, 8, 10]

## Ejemplo 5 - Uso con sorted()

tuplas = [(1, 'uno'), (3, 'tres'), (2, 'dos')]  # Definición de una lista de tuplas

ordenado = sorted(tuplas, key=lambda x: x[1])   # Uso de la función lambda con sorted() para ordenar por el segundo elemento de cada tupla

print(f"Ejemplo 5: {ordenado}")                 # Se imprimirá la lista ordenada: [(2, 'dos'), (1, 'uno'), (3, 'tres')]

## Ejemplo 6 - Usando lambda en una función

def hacer_incrementador(n):             # Definición de una función que devuelve una función lambda
    return lambda x: x + n

incrementar = hacer_incrementador(5)    # Crear una función lambda que incrementa por 5

print(f"Ejemplo 6: {incrementar(10)}")  # Se imprimirá 15, que es el resultado de incrementar 10 en 5
