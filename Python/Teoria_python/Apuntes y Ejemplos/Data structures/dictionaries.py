# Explicación de diccionarios y sus métodos en Python
# Los diccionarios en Python son colecciones no ordenadas de pares clave-valor.
# Permiten almacenar cualquier tipo de dato como valor y tienen numerosos métodos integrados para facilitar operaciones comunes.

## Ejemplo 1 - Creación y acceso a diccionarios

persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Barcelona'}   # Definición de un diccionario básico

print(f"Ejemplo 1: {persona}")                 # Se imprimirá el diccionario completo {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Barcelona'}
print(f"Claves del diccionario: {persona.keys()}")   # Se imprimirán las claves del diccionario
print(f"Valores del diccionario: {persona.values()}") # Se imprimirán los valores del diccionario

print(f"Nombre: {persona['nombre']}")          # Acceso al valor de una clave específica, se imprimirá "Juan"

## Ejemplo 2 - Modificación de diccionarios

persona['edad'] = 31                          # Modificación de un valor existente

print(f"Ejemplo 2: {persona}")                 # Se imprimirá el diccionario actualizado {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Barcelona'}

persona['profesion'] = 'Ingeniero'            # Añadir una nueva clave-valor

print(f"Ejemplo 2: {persona}")                 # Se imprimirá el diccionario con la nueva entrada {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Barcelona', 'profesion': 'Ingeniero'}

## Ejemplo 3 - Métodos de diccionarios

print(f"Ejemplo 3: {len(persona)}")            # len() devuelve el número de elementos en el diccionario, se imprimirá 4

persona.pop('ciudad')                         # pop() elimina un elemento con la clave especificada y devuelve su valor

print(f"Ejemplo 3: {persona}")                 # Se imprimirá el diccionario sin la clave 'ciudad': {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}

persona.clear()                               # clear() elimina todos los elementos del diccionario

print(f"Ejemplo 3: {persona}")                 # Se imprimirá el diccionario vacío {}

## Ejemplo 4 - Iteración y verificación

persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

for clave, valor in persona.items():           # Iteración sobre claves y valores del diccionario
    print(f"Ejemplo 4: {clave}: {valor}")

print(f"Ejemplo 4: {'nombre' in persona}")     # Verificación de la existencia de una clave en el diccionario, se imprimirá True

## Ejemplo 5 - Asignación y comprensión de diccionarios

claves = ['a', 'b', 'c']
valores = [1, 2, 3]

diccionario = {clave: valor for clave, valor in zip(claves, valores)}  # Creación de un diccionario con comprensión

print(f"Ejemplo 5: {diccionario}")             # Se imprimirá el diccionario {'a': 1, 'b': 2, 'c': 3}
