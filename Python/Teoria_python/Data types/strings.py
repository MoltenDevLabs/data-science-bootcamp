# Explicación de strings y sus métodos en Python
# Los strings en Python son secuencias inmutables de caracteres Unicode.
# Permiten manipular texto de diversas formas y tienen numerosos métodos integrados para facilitar operaciones comunes.

## Ejemplo 1 - Creación y acceso a strings

mensaje = "Hola Mundo"                    # Definición de un string básico

print(f"Ejemplo 1: {mensaje}")            # Se imprimirá "Hola Mundo"
print(f"Longitud del string: {len(mensaje)}")  # Se imprimirá la longitud del string, que es 10

print(f"Primer caracter: {mensaje[0]}")   # Acceso al primer caracter, se imprimirá "H"
print(f"Último caracter: {mensaje[-1]}")  # Acceso al último caracter, se imprimirá "o"

## Ejemplo 2 - Concatenación y formateo de strings

nombre = "Juan"
edad = 30

saludo = "Hola, " + nombre + ". Tienes " + str(edad) + " años."  # Concatenación de strings

print(f"Ejemplo 2: {saludo}")             # Se imprimirá "Hola, Juan. Tienes 30 años."

saludo_formato = f"Hola, {nombre}. Tienes {edad} años."  # Formateo de strings con f-strings

print(f"Ejemplo 2: {saludo_formato}")     # Se imprimirá "Hola, Juan. Tienes 30 años."

## Ejemplo 3 - Métodos de strings

mensaje = "   Hola Mundo!   "             # String con espacios al principio y al final

print(f"Ejemplo 3: {mensaje.strip()}")    # strip() elimina los espacios en blanco al inicio y al final

print(f"Ejemplo 3: {mensaje.lower()}")    # lower() convierte todo a minúsculas
print(f"Ejemplo 3: {mensaje.upper()}")    # upper() convierte todo a mayúsculas

print(f"Ejemplo 3: {mensaje.startswith('Hola')}")   # startswith() verifica si el string empieza con "Hola"
print(f"Ejemplo 3: {mensaje.endswith('!')}")       # endswith() verifica si el string termina con "!"

print(f"Ejemplo 3: {mensaje.replace('Mundo', 'Python')}")  # replace() reemplaza "Mundo" por "Python"

palabras = mensaje.split()               # split() divide el string en una lista de palabras
print(f"Ejemplo 3: {palabras}")          # Se imprimirá la lista de palabras ['Hola', 'Mundo!']

## Ejemplo 4 - Búsqueda y conteo

mensaje = "Hola Mundo! Hola Python!"

print(f"Ejemplo 4: {mensaje.find('Hola')}")      # find() encuentra la primera ocurrencia de "Hola"
print(f"Ejemplo 4: {mensaje.count('Hola')}")     # count() cuenta cuántas veces aparece "Hola"
print(f"Ejemplo 4: {mensaje.index('Python')}")   # index() encuentra la posición de "Python"

## Ejemplo 5 - Verificación y formato

print(f"Ejemplo 5: {'123'.isdigit()}")       # isdigit() verifica si todos los caracteres son dígitos
print(f"Ejemplo 5: {'Hola123'.isalpha()}")   # isalpha() verifica si todos los caracteres son letras

numero = 123
print(f"Ejemplo 5: {'Número: {:04d}'.format(numero)}")  # Formateo de número con format()

