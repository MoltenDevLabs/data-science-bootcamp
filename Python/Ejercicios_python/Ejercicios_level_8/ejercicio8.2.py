# Genera una matriz de 10x10 donde cada elemento es un número primo. Usa una lista de comprensión anidada.

def generar_primos(n):  # Función para generar numeros primos
  primos = []
  es_primo = [True] * (n + 1)
  for p in range(2, n + 1):
    if es_primo[p]:
      primos.append(p)
      for i in range(p * p, n + 1, p):
        es_primo[i] = False
  return primos

primos = generar_primos(1000) # Genera una lista de números primos para llenar 10x10 espacios

matriz_primos = [[primos[i * 10 + j] for j in range(10)] for i in range(10)]  # Crear la matriz 10x10 usando los números primos generados

for fila in matriz_primos:
    print(fila)
