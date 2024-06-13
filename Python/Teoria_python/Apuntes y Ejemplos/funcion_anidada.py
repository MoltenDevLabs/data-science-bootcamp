# Explicación de funciones anidadas
# Las funciones anidadas en Python son funciones definidas dentro de otra función. 
# Pueden acceder a variables locales de la función exterior y se utilizan para organizar y modular el código.

## Ejemplo 1 - Función exterior con función anidada

def exterior():
    print("Función exterior")

    def anidada():                      # Definición de una función anidada
        print("Función anidada")

    anidada()                           # Llamada a la función anidada dentro de la función exterior

exterior()                              # Llamada a la función exterior

## Ejemplo 2 - Función con retorno de función anidada

def exterior_con_retorno():
    print("Función exterior")

    def anidada():                      # Definición de una función anidada
        print("Función anidada")
    
    return anidada                      # Retorno de la función anidada

funcion_anidada = exterior_con_retorno() # Llamada a la función exterior que retorna la función anidada
funcion_anidada()                        # Llamada a la función anidada retornada

## Ejemplo 3 - Función anidada con acceso a variables locales de la función exterior

def exterior_con_variable():
    mensaje = "Hola desde la función exterior"

    def anidada():
        print(mensaje)                  # Acceso a la variable local mensaje de la función exterior

    anidada()

exterior_con_variable()

## Ejemplo 4 - Función anidada con argumentos de la función exterior

def exterior_con_argumento(x):
    def anidada():
        print(f"El argumento es {x}")  # Uso del argumento de la función exterior en la función anidada
    
    anidada()

exterior_con_argumento(5)

## Ejemplo 5 - Utilizando funciones anidadas para encapsular lógica compleja

def calcular_operacion(operacion):
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    if operacion == "suma":
        return suma
    elif operacion == "resta":
        return resta

operacion_elegida = calcular_operacion("suma")
resultado = operacion_elegida(3, 4)
print(f"Resultado de la suma: {resultado}")

operacion_elegida = calcular_operacion("resta")
resultado = operacion_elegida(7, 2)
print(f"Resultado de la resta: {resultado}")
