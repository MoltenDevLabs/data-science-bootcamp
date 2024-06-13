# Explicación de closures en Python
# Los closures en Python son funciones definidas dentro de otra función que capturan y mantienen el entorno (variables locales) en el cual fueron creadas.
# Permiten tener funciones con estado (memoria) y son útiles cuando queremos crear funciones especializadas que conserven información entre llamadas.

## Ejemplo 1 - Closure básico

def exterior(x):
    def interior(y):
        return x + y    # La función interior utiliza la variable x de la función exterior

    return interior     # La función exterior devuelve la función interior

closure = exterior(5)   # Llamada a la función exterior con x = 5, closure ahora es la función interior con x = 5
resultado = closure(3)  # Llamada a closure con y = 3, resultado será 5 + 3

print(f"Ejemplo 1: {resultado}")  # Se imprimirá 8, que es el resultado de 5 + 3

## Ejemplo 2 - Closure con estado (memoria)

def contador():
    count = 0            # Variable local dentro de la función exterior

    def incrementar():
        nonlocal count   # Uso de nonlocal para modificar la variable count de la función exterior
        count += 1       # Incremento de count en cada llamada

        return count     # Retorna el valor actual de count

    return incrementar   # Retorna la función incrementar

contador1 = contador()   # Llamada a contador, contador1 es ahora la función incrementar asociada
print(f"Ejemplo 2: {contador1()}")  # Se imprimirá 1, el primer incremento
print(f"Ejemplo 2: {contador1()}")  # Se imprimirá 2, el segundo incremento

contador2 = contador()   # Se crea una nueva instancia de contador, independiente de contador1
print(f"Ejemplo 2: {contador2()}")  # Se imprimirá 1, el primer incremento para contador2

## Ejemplo 3 - Closure con argumentos iniciales

def multiplicador(factor):
    def multiplicar(numero):
        return factor * numero   # La función interior utiliza el argumento factor de la función exterior

    return multiplicar           # La función exterior devuelve la función interior

por_dos = multiplicador(2)       # Llamada a multiplicador con factor = 2, por_dos ahora es la función multiplicar con factor = 2
print(f"Ejemplo 3: {por_dos(5)}")  # Se imprimirá 10, que es el resultado de 2 * 5

por_tres = multiplicador(3)      # Llamada a multiplicador con factor = 3, por_tres ahora es la función multiplicar con factor = 3
print(f"Ejemplo 3: {por_tres(5)}")  # Se imprimirá 15, que es el resultado de 3 * 5
