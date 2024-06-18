## FUNCIONES DE PYTHON

# Funciones para cualquier tipo de dato:
# Estas funciones son aplicables a todos los tipos de datos, incluidos números, cadenas, listas, tuplas, diccionarios, etc.

## Ejemplo 1 - len()

# La función len() devuelve el número de elementos de un objeto.
elemento = [1, 2, 3, 4, 5]  # Definición de una lista
print(f"Ejemplo 1: {len(elemento)}")  # Se imprimirá 5

## Ejemplo 2 - type()

# La función type() devuelve el tipo del objeto.
variable = "Hola, mundo!"  # Definición de una cadena
print(f"Ejemplo 2: {type(variable)}")  # Se imprimirá <class 'str'>

## Ejemplo 3 - sorted()

# La función sorted() devuelve una lista ordenada de los elementos de cualquier iterable.
numeros = [3, 1, 4, 1, 5, 9]  # Definición de una lista de números
print(f"Ejemplo 3: {sorted(numeros)}")  # Se imprimirá [1, 1, 3, 4, 5, 9]

## Ejemplo 4 - reversed()

# La función reversed() devuelve un iterador que invierte el orden de los elementos de cualquier secuencia.
cadena = "Python"  # Definición de una cadena
print(f"Ejemplo 4: {''.join(reversed(cadena))}")  # Se imprimirá nohtyP

# Funciones específicas para listas:
# Estas funciones son específicas para listas y no se pueden usar directamente con otros tipos de datos.

## Ejemplo 5 - append()

# La función append() añade un elemento al final de una lista.
lista = [1, 2, 3]  # Definición de una lista
lista.append(4)  # Añadir un elemento a la lista
print(f"Ejemplo 5: {lista}")  # Se imprimirá [1, 2, 3, 4]

## Ejemplo 6 - extend()

# La función extend() añade todos los elementos de un iterable al final de la lista.
lista = [1, 2, 3]  # Definición de una lista
lista.extend([4, 5, 6])  # Añadir múltiples elementos a la lista
print(f"Ejemplo 6: {lista}")  # Se imprimirá [1, 2, 3, 4, 5, 6]

## Ejemplo 7 - pop()

# La función pop() elimina y devuelve el último elemento de una lista.
lista = [1, 2, 3, 4]  # Definición de una lista
ultimo_elemento = lista.pop()  # Eliminar y devolver el último elemento
print(f"Ejemplo 7: {ultimo_elemento}")  # Se imprimirá 4
print(f"Ejemplo 7: {lista}")  # Se imprimirá [1, 2, 3]

# Funciones específicas para cadenas:
# Estas funciones son específicas para cadenas y no se pueden usar directamente con otros tipos de datos.

## Ejemplo 8 - upper()

# La función upper() devuelve una cadena con todos los caracteres en mayúsculas.
cadena = "hola, mundo!"  # Definición de una cadena
print(f"Ejemplo 8: {cadena.upper()}")  # Se imprimirá HOLA, MUNDO!

## Ejemplo 9 - lower()

# La función lower() devuelve una cadena con todos los caracteres en minúsculas.
cadena = "HOLA, MUNDO!"  # Definición de una cadena
print(f"Ejemplo 9: {cadena.lower()}")  # Se imprimirá hola, mundo!

## Ejemplo 10 - split()

# La función split() divide una cadena en una lista de subcadenas utilizando un separador.
cadena = "uno,dos,tres"  # Definición de una cadena
print(f"Ejemplo 10: {cadena.split(',')}")  # Se imprimirá ['uno', 'dos', 'tres']

## Ejemplo 11 - join()

# La función join() une una lista de cadenas en una sola cadena, utilizando un separador.
lista_cadenas = ['uno', 'dos', 'tres']  # Definición de una lista de cadenas
print(f"Ejemplo 11: {','.join(lista_cadenas)}")  # Se imprimirá uno,dos,tres

## Ejemplo 12 - replace()

# La función replace() devuelve una nueva cadena en la que se han reemplazado todas las apariciones de una subcadena por otra.
cadena = "Hola, mundo!"  # Definición de una cadena
print(f"Ejemplo 12: {cadena.replace('mundo', 'Python')}")  # Se imprimirá Hola, Python!

# Funciones específicas para diccionarios:
# Estas funciones son específicas para diccionarios y no se pueden usar directamente con otros tipos de datos.

## Ejemplo 13 - keys()

# La función keys() devuelve una vista de los elementos clave de un diccionario.
diccionario = {'nombre': 'Juan', 'edad': 30}  # Definición de un diccionario
print(f"Ejemplo 13: {diccionario.keys()}")  # Se imprimirá dict_keys(['nombre', 'edad'])

## Ejemplo 14 - values()

# La función values() devuelve una vista de los valores de un diccionario.
print(f"Ejemplo 14: {diccionario.values()}")  # Se imprimirá dict_values(['Juan', 30])

## Ejemplo 15 - items()

# La función items() devuelve una vista de los pares clave-valor de un diccionario.
print(f"Ejemplo 15: {diccionario.items()}")  # Se imprimirá dict_items([('nombre', 'Juan'), ('edad', 30)])

# Funciones específicas para conjuntos (sets):
# Estas funciones son específicas para conjuntos y no se pueden usar directamente con otros tipos de datos.

## Ejemplo 16 - add()

# La función add() añade un elemento a un conjunto.
conjunto = {1, 2, 3}  # Definición de un conjunto
conjunto.add(4)  # Añadir un elemento al conjunto
print(f"Ejemplo 16: {conjunto}")  # Se imprimirá {1, 2, 3, 4}

## Ejemplo 17 - remove()

# La función remove() elimina un elemento específico de un conjunto.
conjunto.remove(2)  # Eliminar un elemento del conjunto
print(f"Ejemplo 17: {conjunto}")  # Se imprimirá {1, 3, 4}

## Ejemplo 18 - union()

# La función union() devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos.
conjunto1 = {1, 2, 3}  # Definición de un conjunto
conjunto2 = {3, 4, 5}  # Definición de otro conjunto
print(f"Ejemplo 18: {conjunto1.union(conjunto2)}")  # Se imprimirá {1, 2, 3, 4, 5}

## Ejemplo 19 - intersection()

# La función intersection() devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.
print(f"Ejemplo 19: {conjunto1.intersection(conjunto2)}")  # Se imprimirá {3}
