# Genera una matriz de 10x10 donde cada elemento es un número primo. Usa una lista de comprensión anidada.

matriz = [[fila[i] for fila in range(10)] for i in range(10) if i % range(9) != 0]

print(matriz)