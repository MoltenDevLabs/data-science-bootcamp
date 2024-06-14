## GENERADORES

# Los generadores en Python son una forma especial de iteradores que permiten crear iterables de manera eficiente y perezosa. 
# Se utilizan para generar secuencias de valores sobre la marcha, sin necesidad de almacenar toda la secuencia en memoria.

# Sintaxis básica:
# - Los generadores se definen usando funciones y la palabra clave 'yield' en lugar de 'return'.
# - Cada vez que 'yield' se encuentra, la ejecución de la función se pausa y se retorna el valor.

## Ejemplo 1 - Generador básico

def generador_basico():
    yield 1
    yield 2
    yield 3

gen = generador_basico()
print(f"Ejemplo 1: {list(gen)}")  # Se imprimirá [1, 2, 3]

## Ejemplo 2 - Generador con un bucle

def generador_con_bucle(n):
    for i in range(n):
        yield i

gen = generador_con_bucle(5)
print(f"Ejemplo 2: {list(gen)}")  # Se imprimirá [0, 1, 2, 3, 4]

## Ejemplo 3 - Generador infinito

def generador_infinito():
    i = 0
    while True:
        yield i
        i += 1

gen = generador_infinito()

print("Ejemplo 3: Primeros 5 valores del generador infinito:")
for _ in range(5):
    print(next(gen))  # Se imprimirá 0, 1, 2, 3, 4

## Ejemplo 4 - Generador para lectura de archivos línea por línea

def leer_archivo_linea_por_linea(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        for linea in archivo:
            yield linea.strip()

nombre_archivo = 'C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\texto.txt'
gen = leer_archivo_linea_por_linea(nombre_archivo)

print("Ejemplo 4: Lectura de archivo línea por línea:")
for linea in gen:
    print(linea)  # Se imprimirá cada línea del archivo

## Ejemplo 5 - Expresiones generadoras

gen_expr = (x * x for x in range(5))
print(f"Ejemplo 5: {list(gen_expr)}")  # Se imprimirá [0, 1, 4, 9, 16]

## Ejemplo 6 - Generador para la secuencia de Fibonacci

def generador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = generador_fibonacci()

print("Ejemplo 6: Primeros 10 números de Fibonacci:")
for _ in range(10):
    print(next(gen))  # Se imprimirá la secuencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

