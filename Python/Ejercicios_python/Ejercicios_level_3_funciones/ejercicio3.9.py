# Escribir una función que calcule el módulo de un vector.

from functools import reduce

def cuadrado(i, j):
  return i + j**2

def modulo_v1(v):           # Solución con lista de compresión
  l = [x**2 for x in v]
  c = 0
  for k in l:
    c += k
  return c**0.5

def modulo_v2(v):           # Solución con reduce()
  return reduce(cuadrado, v, 0) ** 0.5

print(f"modulo_v1: {modulo_v1((1, 2, 3))}")  # Raiz cuadrada de 1**2 + 2**2 + 3**2
print(f"modulo_v2: {modulo_v2((1, 2, 3))}") 
