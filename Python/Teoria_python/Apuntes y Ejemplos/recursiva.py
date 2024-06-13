# Explicación funciones recursivas
# Las funciones recursivas son funciones que se llaman a sí mismas durante su ejecución. 
# La recursión se utiliza para resolver problemas que pueden dividirse en subproblemas más pequeños del mismo tipo.
# Es importante definir un caso base para evitar recursiones infinitas.

## Ejemplo 1 - Factorial de un número

def factorial(n):                           # Definición de la función factorial
    if n == 0:                              # Caso base: el factorial de 0 es 1
        return 1
    else:
        return n * factorial(n - 1)         # Llamada recursiva

print(f"Ejemplo 1: {factorial(5)}")         # Se imprimirá 120, que es el factorial de 5

## Ejemplo 2 - Fibonacci

def fibonacci(n):                           # Definición de la función fibonacci
    if n <= 1:                              # Caso base: fibonacci de 0 es 0, y de 1 es 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamadas recursivas

print(f"Ejemplo 2: {fibonacci(6)}")         # Se imprimirá 8, que es el sexto número de Fibonacci

## Ejemplo 3 - Suma de una lista

def suma_lista(lista):                      # Definición de la función suma_lista
    if len(lista) == 0:                     # Caso base: la suma de una lista vacía es 0
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])  # Llamada recursiva

print(f"Ejemplo 3: {suma_lista([1, 2, 3, 4])}")  # Se imprimirá 10, que es la suma de los elementos de la lista

## Ejemplo 4 - Potencia de un número

def potencia(base, exponente):              # Definición de la función potencia
    if exponente == 0:                      # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva

print(f"Ejemplo 4: {potencia(2, 3)}")       # Se imprimirá 8, que es 2 elevado a la 3

## Ejemplo 5 - Invertir una cadena

def invertir_cadena(cadena):                # Definición de la función invertir_cadena
    if len(cadena) == 0:                    # Caso base: la cadena vacía se queda igual
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]  # Llamada recursiva

print(f"Ejemplo 5: {invertir_cadena('hola')}")  # Se imprimirá 'aloh', que es la cadena invertida

## Ejemplo 6 - Contar elementos en una lista

def contar_elementos(lista):                # Definición de la función contar_elementos
    if not lista:                           # Caso base: lista vacía
        return 0
    else:
        return 1 + contar_elementos(lista[1:])  # Llamada recursiva

print(f"Ejemplo 6: {contar_elementos([1, 2, 3, 4])}")  # Se imprimirá 4, que es el número de elementos en la lista
