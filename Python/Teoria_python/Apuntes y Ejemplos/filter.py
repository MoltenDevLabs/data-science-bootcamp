# Explicación de la función filter() en Python
# La función filter() se utiliza para filtrar elementos de una secuencia (como listas, tuplas, etc.) según una función condicional.

## Ejemplo 1 - Filtrado básico de números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(numero):
    return numero % 2 == 0

pares = filter(es_par, numeros)  # Filtrar números pares usando la función es_par

print(f"Ejemplo 1: Números pares: {list(pares)}")  # Se imprimirá una lista con los números pares [2, 4, 6, 8, 10]

## Ejemplo 2 - Filtrado de cadenas según longitud

palabras = ["hola", "python", "es", "genial", "y", "poderoso"]

def longitud_mayor_a_cinco(palabra):
    return len(palabra) > 5

filtradas = filter(longitud_mayor_a_cinco, palabras)  # Filtrar palabras con longitud mayor a 5

print(f"Ejemplo 2: Palabras filtradas: {list(filtradas)}")  # Se imprimirá una lista con las palabras filtradas ["python", "genial", "poderoso"]

## Ejemplo 3 - Filtrado de objetos según atributos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"{self.nombre} ({self.edad})"

personas = [
    Persona("Juan", 30),
    Persona("María", 25),
    Persona("Carlos", 40),
    Persona("Elena", 35)
]

def mayor_de_treinta(persona):
    return persona.edad > 30

mayores = filter(mayor_de_treinta, personas)  # Filtrar personas mayores de 30 años

print(f"Ejemplo 3: Personas mayores de 30 años: {list(mayores)}")  # Se imprimirá una lista con las personas filtradas

