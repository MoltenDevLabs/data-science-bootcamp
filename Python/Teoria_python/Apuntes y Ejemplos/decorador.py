# Explicación funciones decorador
# Los decoradores en Python son funciones que modifican el comportamiento de otras funciones. 
# Se utilizan para añadir funcionalidad adicional a una función existente de una manera concisa y reutilizable.
# Un decorador es una función que recibe otra función como argumento y devuelve una nueva función.

## Ejemplo 1 - Decorador básico

def decorador(func):                         # Definición de un decorador básico
    def nueva_funcion(*args, **kwargs):      # Definición de la nueva función que envuelve a la original
        print("Antes de la función")
        resultado = func(*args, **kwargs)    # Llamada a la función original
        print("Después de la función")
        return resultado
    return nueva_funcion                     # Retorno de la nueva función

@decorador                                   # Aplicación del decorador
def saludar():
    print("Hola")

print("Ejemplo 1:")
saludar()                                     # Se imprimirá el mensaje antes y después de la función saludar

## Ejemplo 2 - Decorador con argumentos

def decorador_con_argumentos(texto):          # Definición de un decorador que acepta argumentos
    def decorador(func):
        def nueva_funcion(*args, **kwargs):
            print(f"{texto} - Antes de la función")
            resultado = func(*args, **kwargs)
            print(f"{texto} - Después de la función")
            return resultado
        return nueva_funcion
    return decorador

@decorador_con_argumentos("INFO")             # Aplicación del decorador con argumento
def despedirse():
    print("Adiós")

print("Ejemplo 2:")
despedirse()                                  # Se imprimirá el mensaje antes y después de la función despedirse con el texto "INFO"

## Ejemplo 3 - Decorador para medir tiempo de ejecución

import time

def medir_tiempo(func):
    def nueva_funcion(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return nueva_funcion

@medir_tiempo                                 # Aplicación del decorador para medir tiempo
def dormir():
    time.sleep(2)
    print("He dormido 2 segundos")

print("Ejemplo 3:")
dormir()                                      # Se imprimirá el tiempo de ejecución de la función dormir

## Ejemplo 4 - Decorador anidado

def decorador1(func):
    def nueva_funcion(*args, **kwargs):
        print("Decorador 1 - Antes")
        resultado = func(*args, **kwargs)
        print("Decorador 1 - Después")
        return resultado
    return nueva_funcion

def decorador2(func):
    def nueva_funcion(*args, **kwargs):
        print("Decorador 2 - Antes")
        resultado = func(*args, **kwargs)
        print("Decorador 2 - Después")
        return resultado
    return nueva_funcion

@decorador1
@decorador2                                  # Aplicación de múltiples decoradores
def hola():
    print("Hola a todos")

print("Ejemplo 4:")
hola()                                       # Se imprimirá el mensaje de los decoradores en orden anidado

## Ejemplo 5 - Decorador para validar entrada

def validar_positivo(func):
    def nueva_funcion(x):
        if x < 0:
            raise ValueError("El número debe ser positivo")
        return func(x)
    return nueva_funcion

@validar_positivo                            # Aplicación del decorador para validar entrada
def imprimir_cuadrado(x):
    print(f"El cuadrado de {x} es {x * x}")

print("Ejemplo 5:")
imprimir_cuadrado(3)                         # Se imprimirá el cuadrado del número
try:
    imprimir_cuadrado(-3)                    # Se lanzará una excepción
except ValueError as e:
    print(e)
