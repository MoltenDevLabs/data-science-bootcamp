# Explicación función zip()
# Sirve para combinar 2 o más iterables (listas, tuplas, etc) en 1 solo iterable
# Empareja los elementos de la misma posición de los distintos iterables
# Si los iterables tienen distintos largos, se truncará al más corto

## Ejemplo 1 - Uso básico

lista1 = [1, 2, 3]            # Definción de lista1
lista2 = ['a', 'b', 'c']      # Definición de lista2

zipped = zip(lista1, lista2)  # Uso de la función zip() para unir lista1 y lista2
print(f"Ejemplo 1: {list(zipped)}")           # Se imprimira una lista de tuplas con los elementos emparejados

## Ejemplo 2 - Bucle for con zip()

matematicas, lengua, personas = [3, 8, 3, 9, 0], [8, 5, 3, 7, 5], ['pol', 'merchu', 'roc', 'lluna', 'guiu'] # Definición de 3 listas

for i, j, k in zip(personas, matematicas, lengua):                                                          # Iteración y compresión de las listas i-personas, j-matematicas, k-lengua
  print(f"Ejemplo 2: {i}, {j}, {k}")                                                                        # Impresión de cada iteración

## Ejemplo 3 - Crear diccionarios combinando listas *** IMPORTANTE ***

keys = ['Nombre', 'Edad', 'Sexo']                   # Definición de lista keys
values = ['John', 30, 'M']                          # Definición de lista values

diccionario = {i: j for i, j in zip(keys, values)}  # Definición de un diccionario de compresión; se itera con i para las keys y j para los values

print(f"Ejemplo 3: {diccionario}")                  # Impresión del diccionario

## Ejemplo 4 - Descompresión

list_zipped = [(1, 'a'), (2, 'b'), (3, 'c')]  # Definición de una lista de tuplas

list3, list4 = zip(*list_zipped)              # Descomprimir usando *

print(f"Ejemplo 4: {list3}")                  # Impresión de list3 con los primeros valores de cada tupla
print(f"Ejemplo 4: {list4}")                  # Impresión de list4 con los segundos valores de cada tupla
