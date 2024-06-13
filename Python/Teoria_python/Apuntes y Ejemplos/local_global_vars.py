# Explicación de paso de variables locales a globales y uso de keywords como global y nonlocal en Python
# En Python, las variables locales se refieren a las variables definidas dentro de una función y son accesibles solo dentro de esa función.
# Las variables globales se definen fuera de cualquier función y son accesibles desde cualquier parte del código.
# Las keywords `global` y `nonlocal` permiten modificar variables globales y variables en funciones anidadas, respectivamente.

## Ejemplo 1 - Uso de la keyword global

variable_global = "Hola Global"         # Definición de una variable global

def modificar_global():
    global variable_global             # Uso de la keyword global para modificar la variable global
    variable_global = "Hola desde la función"

print(f"Antes de llamar a la función: {variable_global}")   # Se imprimirá "Hola Global"
modificar_global()
print(f"Después de llamar a la función: {variable_global}")  # Se imprimirá "Hola desde la función"

## Ejemplo 2 - Uso de la keyword nonlocal en funciones anidadas

def funcion_exterior():
    variable_exterior = "Exterior"     # Variable en el ámbito exterior

    def funcion_interior():
        nonlocal variable_exterior     # Uso de la keyword nonlocal para modificar la variable exterior
        variable_exterior = "Modificado en interior"
    
    print(f"Antes de llamar a la función interna: {variable_exterior}")  # Se imprimirá "Exterior"
    funcion_interior()
    print(f"Después de llamar a la función interna: {variable_exterior}")  # Se imprimirá "Modificado en interior"

funcion_exterior()

## Ejemplo 3 - Paso de variables locales a globales

def funcion_con_variable_local():
    variable_local = "Local"           # Definición de una variable local dentro de la función
    
    def funcion_con_global():
        nonlocal variable_local       # Uso de nonlocal para indicar que se está refiriendo a la variable local
        variable_local = "Modificado en local pero no global"

    print(f"Antes de llamar a la función interna: {variable_local}")  # Se imprimirá "Local"
    funcion_con_global()
    print(f"Después de llamar a la función interna: {variable_local}")  # Se imprimirá "Modificado en local pero no global"

funcion_con_variable_local()
