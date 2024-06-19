# Explicación diccionarios de comprensión
# Los diccionarios de comprensión en Python son una forma concisa de crear diccionarios.
# Permiten generar nuevos diccionarios aplicando una expresión a cada par clave-valor de una secuencia existente.
# La sintaxis básica es: {clave: valor for elemento in iterable if condición}

## Ejemplo 1 - Uso básico

numeros = [1, 2, 3, 4]                           # Definición de una lista de números
cuadrados = {x: x * x for x in numeros}          # Uso de un diccionario de comprensión para calcular el cuadrado de cada número

print(f"Ejemplo 1: {cuadrados}")                # Se imprimirá {1: 1, 2: 4, 3: 9, 4: 16}, los cuadrados de los números con los números como claves

## Ejemplo 2 - Filtrado con condición

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]        # Definición de una lista de números
pares_cuadrados = {x: x * x for x in numeros if x % 2 == 0}  # Uso de un diccionario de comprensión para calcular el cuadrado solo de los números pares

print(f"Ejemplo 2: {pares_cuadrados}")           # Se imprimirá {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}, los cuadrados de los números pares con los números como claves

## Ejemplo 3 - Transformación de claves y valores

frutas = {'manzana': 1, 'banana': 2, 'cereza': 3}   # Definición de un diccionario de frutas con cantidades
doble_frutas = {k: v * 2 for k, v in frutas.items()}  # Uso de un diccionario de comprensión para duplicar las cantidades

print(f"Ejemplo 3: {doble_frutas}")               # Se imprimirá {'manzana': 2, 'banana': 4, 'cereza': 6}, las cantidades duplicadas

## Ejemplo 4 - Condiciones adicionales

numeros = [1, 2, 3, 4, 5]                        # Definición de una lista de números
cuadrados_pares = {x: x * x for x in numeros if x % 2 == 0 if x != 4}  # Uso de un diccionario de comprensión con condiciones adicionales

print(f"Ejemplo 4: {cuadrados_pares}")           # Se imprimirá {2: 4, 4: 16}, los cuadrados de los números pares distintos de 4

## Ejemplo 5 - Uso de funciones en la comprensión

def calcular_cuadrado(x):                        # Definición de la función para calcular el cuadrado
    return x * x

numeros = [1, 2, 3, 4]                           # Definición de una lista de números
cuadrados_funcion = {x: calcular_cuadrado(x) for x in numeros}  # Uso de un diccionario de comprensión con función

print(f"Ejemplo 5: {cuadrados_funcion}")         # Se imprimirá {1: 1, 2: 4, 3: 9, 4: 16}, los cuadrados de los números con los números como claves

## Ejemplo 6 - Diccionario donde las claves son los números del 1 al 100 y los valores son una tupla con el cuadrado y la raíz cuadrada del número

cuadrado_y_raiz = {i: tuple((i**2, i**0.5)) for i in range(1, 100)}

print(f"Ejemplo 6: {cuadrado_y_raiz}")

## Ejemplo 7 - Dada una lista de palabras, generar un nuevo diccionario que contenga como claves las palabras originales y como valores las palabras invertidas, pero sólo si la palabra original tiene más de 5 caracteres y no contiene ninguna vocal

palabras = ['anchoa', 'atún', 'salmón', 'ba', 'tib', 'zxcvb', 'zx', 'bcdfghjklm', 'qrstvwxyz', 'fghjklmnp', 'bcdflnprstv']
vocales = ['a', 'e', 'i', 'o', 'u']

diccionario_condiciones = {i: i[::-1] for i in palabras if len(i) >= 5 and not any(letra in i for letra in vocales)}

print(f"Ejemplo 7: {diccionario_condiciones}")