# Explicación de tuplas en Python
# Las tuplas en Python son colecciones ordenadas e inmutables de elementos.
# Permiten almacenar cualquier tipo de dato y son útiles cuando necesitas datos que no deben cambiar.

## Ejemplo 1 - Creación y acceso a tuplas

tupla = (1, 2, 3, 4, 5)                     # Definición de una tupla básica de números

print(f"Ejemplo 1: {tupla}")                # Se imprimirá la tupla completa (1, 2, 3, 4, 5)
print(f"Longitud de la tupla: {len(tupla)}") # Se imprimirá la longitud de la tupla, que es 5

print(f"Primer elemento: {tupla[0]}")       # Acceso al primer elemento, se imprimirá 1
print(f"Último elemento: {tupla[-1]}")      # Acceso al último elemento, se imprimirá 5

## Ejemplo 2 - Iteración sobre tuplas

for elemento in tupla:                      # Iteración sobre los elementos de la tupla
    print(f"Ejemplo 2: {elemento}")

## Ejemplo 3 - Concatenación y repetición de tuplas

tupla2 = ('a', 'b', 'c')

tupla_concatenada = tupla + tupla2          # Concatenación de dos tuplas

print(f"Ejemplo 3: {tupla_concatenada}")    # Se imprimirá la tupla concatenada (1, 2, 3, 4, 5, 'a', 'b', 'c')

tupla_repetida = tupla * 2                  # Repetición de una tupla

print(f"Ejemplo 3: {tupla_repetida}")       # Se imprimirá la tupla repetida (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

## Ejemplo 4 - Desempaquetado de tuplas

tupla3 = ('Juan', 30, 'Ingeniero')

nombre, edad, profesion = tupla3            # Desempaquetado de la tupla en variables individuales

print(f"Ejemplo 4: Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}")

## Ejemplo 5 - Métodos de tuplas

print(f"Ejemplo 5: {'a' in tupla2}")        # Verificación de la existencia de un elemento en la tupla, se imprimirá True

print(f"Ejemplo 5: {tupla.index(3)}")       # index() encuentra el índice de un elemento, se imprimirá 2

print(f"Ejemplo 5: {tupla.count(4)}")       # count() cuenta cuántas veces aparece un elemento, se imprimirá 1
