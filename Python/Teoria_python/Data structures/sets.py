# Explicación de sets en Python
# Los sets en Python son colecciones desordenadas y mutables de elementos únicos.
# Permiten realizar operaciones de conjuntos como intersección, unión, diferencia, etc.

## Ejemplo 1 - Creación y acceso a sets

set1 = {1, 2, 3, 4, 5}                     # Definición de un set básico de números

print(f"Ejemplo 1: {set1}")                # Se imprimirá el set completo {1, 2, 3, 4, 5}
print(f"Longitud del set: {len(set1)}")     # Se imprimirá la longitud del set, que es 5

## Ejemplo 2 - Operaciones de sets

set2 = {3, 4, 5, 6, 7}

union = set1 | set2                        # Unión de sets usando el operador |
print(f"Ejemplo 2: Unión: {union}")        # Se imprimirá la unión de set1 y set2

interseccion = set1 & set2                # Intersección de sets usando el operador &
print(f"Ejemplo 2: Intersección: {interseccion}")  # Se imprimirá la intersección de set1 y set2

diferencia = set1 - set2                  # Diferencia de sets usando el operador -
print(f"Ejemplo 2: Diferencia: {diferencia}")      # Se imprimirá la diferencia entre set1 y set2

## Ejemplo 3 - Métodos de sets

set3 = {1, 2, 3}
set4 = {2, 3, 4}

print(f"Ejemplo 3: {set3.union(set4)}")       # union() devuelve la unión de dos sets
print(f"Ejemplo 3: {set3.intersection(set4)}")  # intersection() devuelve la intersección de dos sets
print(f"Ejemplo 3: {set3.difference(set4)}")    # difference() devuelve la diferencia entre dos sets
print(f"Ejemplo 3: {set3.symmetric_difference(set4)}")  # symmetric_difference() devuelve la diferencia simétrica entre dos sets

set3.add(4)                                # add() añade un elemento al set

print(f"Ejemplo 3: {set3}")                # Se imprimirá el set3 actualizado {1, 2, 3, 4}

set3.remove(2)                             # remove() elimina un elemento del set

print(f"Ejemplo 3: {set3}")                # Se imprimirá el set3 actualizado {1, 3, 4}

## Ejemplo 4 - Verificación y comprobación

print(f"Ejemplo 4: {'a' in set1}")         # Verificación de la existencia de un elemento en el set, se imprimirá False

## Ejemplo 5 - Conversión y manejo de elementos únicos

lista = [1, 2, 3, 4, 3, 2, 1]
set_from_list = set(lista)                 # Convertir una lista en un set para obtener elementos únicos

print(f"Ejemplo 5: {set_from_list}")       # Se imprimirá el set con elementos únicos {1, 2, 3, 4}
