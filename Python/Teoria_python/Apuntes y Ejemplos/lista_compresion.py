# Explicación listas de comprensión
# Las listas de comprensión en Python son una manera concisa de crear listas. 
# Permiten generar nuevas listas aplicando una expresión a cada elemento de una secuencia existente.
# La sintaxis básica es: [expresión for elemento in iterable if condición]

## Ejemplo 1 - Uso básico

numeros = [1, 2, 3, 4]                 # Definición de una lista de números
cuadrados = [x * x for x in numeros]   # Uso de una lista de comprensión para calcular el cuadrado de cada número

print(f"Ejemplo 1: {cuadrados}")       # Se imprimirá [1, 4, 9, 16], los cuadrados de los números en la lista original

## Ejemplo 2 - Filtrado con condición

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # Definición de una lista de números
pares = [x for x in numeros if x % 2 == 0]     # Uso de una lista de comprensión para filtrar solo los números pares

print(f"Ejemplo 2: {pares}")                   # Se imprimirá [2, 4, 6, 8, 10], los números pares de la lista original

## Ejemplo 3 - Combinación de elementos

letras = ['a', 'b', 'c']                        # Definición de una lista de letras
numeros = [1, 2, 3]                             # Definición de una lista de números
combinaciones = [(letra, numero) for letra in letras for numero in numeros]  # Uso de una lista de comprensión para combinar elementos

print(f"Ejemplo 3: {combinaciones}")            # Se imprimirá una lista de tuplas con todas las combinaciones de letras y números

## Ejemplo 4 - Aplicar una función a cada elemento

def cuadrado(x):                                # Definición de la función cuadrado
    return x * x

numeros = [1, 2, 3, 4]                          # Definición de una lista de números
cuadrados = [cuadrado(x) for x in numeros]      # Uso de una lista de comprensión para aplicar la función cuadrado a cada número

print(f"Ejemplo 4: {cuadrados}")                # Se imprimirá [1, 4, 9, 16], los cuadrados de los números en la lista original

## Ejemplo 5 - Anidación de listas de comprensión

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]              # Definición de una matriz (lista de listas)
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]  # Uso de listas de comprensión para transponer la matriz

print(f"Ejemplo 5: {transpuesta}")                      # Se imprimirá [[1, 4, 7], [2, 5, 8], [3, 6, 9]], la matriz transpuesta

## Ejemplo 6 - Diccionario de comprensión

letras = ['a', 'b', 'c', 'd']                     # Definición de una lista de letras
numeros = [1, 2, 3, 4]                            # Definición de una lista de números
diccionario = {letra: numero for letra, numero in zip(letras, numeros)}  # Uso de comprensión de diccionario

print(f"Ejemplo 6: {diccionario}")                # Se imprimirá {'a': 1, 'b': 2, 'c': 3, 'd': 4}, un diccionario con letras como claves y números como valores

## Ejemplo 7 - Conjuntos de comprensión

numeros = [1, 2, 3, 4, 1, 2, 3, 4]                # Definición de una lista con números repetidos
conjunto = {x for x in numeros}                   # Uso de un conjunto de comprensión para eliminar duplicados

print(f"Ejemplo 7: {conjunto}")                   # Se imprimirá {1, 2, 3, 4}, un conjunto con elementos únicos
