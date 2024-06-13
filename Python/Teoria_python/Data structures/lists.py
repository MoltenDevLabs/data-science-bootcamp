# Explicación de listas y sus métodos en Python
# Las listas en Python son colecciones ordenadas y mutables de elementos.
# Permiten almacenar cualquier tipo de dato y tienen numerosos métodos integrados para facilitar operaciones comunes.

## Ejemplo 1 - Creación y acceso a listas

lista = [1, 2, 3, 4, 5]                     # Definición de una lista básica de números

print(f"Ejemplo 1: {lista}")                # Se imprimirá la lista completa [1, 2, 3, 4, 5]
print(f"Longitud de la lista: {len(lista)}") # Se imprimirá la longitud de la lista, que es 5

print(f"Primer elemento: {lista[0]}")       # Acceso al primer elemento, se imprimirá 1
print(f"Último elemento: {lista[-1]}")      # Acceso al último elemento, se imprimirá 5

## Ejemplo 2 - Modificación de listas

lista.append(6)                             # append() añade un elemento al final de la lista

print(f"Ejemplo 2: {lista}")                # Se imprimirá la lista actualizada [1, 2, 3, 4, 5, 6]

lista.extend([7, 8, 9])                      # extend() añade múltiples elementos al final de la lista

print(f"Ejemplo 2: {lista}")                # Se imprimirá la lista actualizada [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(3, 'nuevo')                    # insert() inserta un elemento en una posición específica

print(f"Ejemplo 2: {lista}")                # Se imprimirá la lista actualizada [1, 2, 3, 'nuevo', 4, 5, 6, 7, 8, 9]

## Ejemplo 3 - Métodos de listas

lista.remove('nuevo')                       # remove() elimina el primer elemento encontrado con el valor especificado

print(f"Ejemplo 3: {lista}")                # Se imprimirá la lista sin 'nuevo': [1, 2, 3, 4, 5, 6, 7, 8, 9]

elemento = lista.pop()                      # pop() elimina y retorna el último elemento de la lista, o el especificado por índice

print(f"Ejemplo 3: Elemento eliminado: {elemento}, Lista resultante: {lista}")

lista.reverse()                            # reverse() invierte el orden de los elementos en la lista

print(f"Ejemplo 3: {lista}")               # Se imprimirá la lista invertida: [9, 8, 7, 6, 5, 4, 3, 2, 1]

## Ejemplo 4 - Búsqueda y ordenamiento

lista_numeros = [5, 2, 8, 1, 3, 9, 4, 7, 6]

print(f"Ejemplo 4: Índice de '3': {lista_numeros.index(3)}")    # index() encuentra el índice de un elemento

lista_numeros.sort()                       # sort() ordena la lista de menor a mayor

print(f"Ejemplo 4: Lista ordenada: {lista_numeros}")             # Se imprimirá la lista ordenada

## Ejemplo 5 - Operaciones con listas

suma = sum(lista_numeros)                  # sum() suma todos los elementos de la lista

print(f"Ejemplo 5: Suma de elementos: {suma}")                  # Se imprimirá la suma de los elementos de lista_numeros

cuadrados = [x ** 2 for x in lista_numeros]  # Listas de compresión para calcular cuadrados

print(f"Ejemplo 5: Cuadrados de los elementos: {cuadrados}")   # Se imprimirá la lista con los cuadrados de lista_numeros
