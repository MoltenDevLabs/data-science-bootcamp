# Explicación de expresiones regulares (regex) en Python
# Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda.
# Permiten realizar búsquedas y manipulaciones complejas de cadenas de texto.

import re  # Importar el módulo re (regex)

## Ejemplo 1 - Búsqueda básica

texto = "Hola, mi número de teléfono es 123-456-7890."

patron = r'\d{3}-\d{3}-\d{4}'  # Definir un patrón regex para buscar números de teléfono en formato XXX-XXX-XXXX

resultado = re.search(patron, texto)  # Buscar el patrón en el texto

if resultado:
    print(f"Ejemplo 1: Número de teléfono encontrado: {resultado.group()}")  # Se imprimirá el número encontrado
else:
    print("Ejemplo 1: No se encontró ningún número de teléfono.")

## Ejemplo 2 - Extracción de información

texto = "Mi dirección de correo electrónico es usuario@example.com."

patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Patrón regex para buscar direcciones de correo electrónico

resultado_email = re.search(patron_email, texto)  # Buscar el patrón de correo electrónico en el texto

if resultado_email:
    print(f"Ejemplo 2: Correo electrónico encontrado: {resultado_email.group()}")  # Se imprimirá el correo electrónico encontrado
else:
    print("Ejemplo 2: No se encontró ninguna dirección de correo electrónico.")

## Ejemplo 3 - Sustitución de texto

texto = "Mi número de teléfono antiguo era 987-654-3210."

nuevo_numero = re.sub(r'\d{3}-\d{3}-\d{4}', '555-123-4567', texto)  # Sustituir el número de teléfono por uno nuevo

print(f"Ejemplo 3: Texto con número de teléfono actualizado: {nuevo_numero}")

## Ejemplo 4 - Validación de formato

def validar_tarjeta_credito(numero):
    patron_tarjeta = r'^\d{4}-\d{4}-\d{4}-\d{4}$'  # Patrón regex para validar números de tarjeta de crédito en formato XXXX-XXXX-XXXX-XXXX

    if re.match(patron_tarjeta, numero):
        return True
    else:
        return False

numero_tarjeta = '1234-5678-9876-5432'

if validar_tarjeta_credito(numero_tarjeta):
    print(f"Ejemplo 4: El número de tarjeta '{numero_tarjeta}' es válido.")
else:
    print(f"Ejemplo 4: El número de tarjeta '{numero_tarjeta}' no es válido.")

## Ejemplo 5 - División de texto

texto = "Python es un lenguaje de programación."

palabras = re.split(r'\s', texto)  # Dividir el texto en palabras usando espacios como delimitadores

print(f"Ejemplo 5: Palabras encontradas: {palabras}")  # Se imprimirán las palabras divididas

