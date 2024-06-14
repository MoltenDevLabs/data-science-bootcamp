## GESTIÓN DE ERRORES

# En Python, la gestión de errores se maneja mediante el uso de excepciones. 
# Las excepciones permiten capturar y manejar errores en el código de una manera controlada.

# Sintaxis básica:
# try:
#     # Código que puede causar una excepción
# except <<TipoDeExcepcion>>:
#     # Código para manejar la excepción
# else:
#     # Código a ejecutar si no ocurre una excepción
# finally:
#     # Código a ejecutar siempre, ocurra o no una excepción

## Ejemplo 1 - Manejo básico de excepciones

try:
    resultado = 10 / 0              # Esto causará una excepción ZeroDivisionError
except ZeroDivisionError:
    print("Ejemplo 1: Error - División por cero")
finally:
    print("Ejemplo 1: Bloque finally ejecutado")

## Ejemplo 2 - Captura de múltiples excepciones

try:
    lista = [1, 2, 3]
    print(lista[5])                 # Esto causará una excepción IndexError
except (IndexError, ZeroDivisionError) as e:
    print(f"Ejemplo 2: Error - {e}")
finally:
    print("Ejemplo 2: Bloque finally ejecutado")

## Ejemplo 3 - Uso del bloque else

try:
    numero = int(input("Introduce un número: "))  # Esto puede causar una excepción ValueError
except ValueError:
    print("Ejemplo 3: Error - No es un número válido")
else:
    print(f"Ejemplo 3: El número introducido es {numero}")
finally:
    print("Ejemplo 3: Bloque finally ejecutado")

## Ejemplo 4 - Definir y lanzar excepciones personalizadas

class ErrorPersonalizado(Exception):
    pass

def comprobar_positivo(numero):
    if numero < 0:
        raise ErrorPersonalizado("El número no es positivo")
    return numero

try:
    print(comprobar_positivo(-1))  # Esto causará una excepción ErrorPersonalizado
except ErrorPersonalizado as e:
    print(f"Ejemplo 4: Error - {e}")
finally:
    print("Ejemplo 4: Bloque finally ejecutado")

## Ejemplo 5 - Uso del bloque finally para liberar recursos

try:
    archivo = open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\texto.txt', 'r', encoding='UTF-8')
    for linea in archivo:
        print(f"Ejemplo 5_try: {linea.strip()}")
except FileNotFoundError:
    print("Ejemplo 5_except: Error - No se encuentra el archivo")
finally:
    archivo.close()
    print("Ejemplo 5_finally: Archivo cerrado correctamente")

