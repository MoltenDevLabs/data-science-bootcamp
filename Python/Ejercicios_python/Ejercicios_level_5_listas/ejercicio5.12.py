# Escribir un programa que almacene las matrices
# A = (1 2 3) y B = (-1 0)
#     (4 5 6)       (0 1)
#                   (1 1)

# Definición de matrices A y B
A = ((1, 2, 3), (4, 5, 6))  # Matriz A
B = ((-1, 0), (0, 1), (1, 1))  # Matriz B

# Inicialización de la matriz resultante R con ceros
R = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]  # Estructura de datos resultante [[0, 0], [0, 0]]

# Multiplicación de matrices
for i in range(len(A)):  # Itera sobre las filas de A
  for j in range(len(B[0])):  # Itera sobre las columnas de B
    for k in range(len(B)):  # Itera sobre las filas de B y columnas de A
      R[i][j] += A[i][k] * B[k][j]  # Acumula el producto de A y B en R[i][j]

# Convertir los elementos internos de R en una tupla
for z in range(len(R)):
  R[z] = tuple(R[z])

# Convertir R en una tupla de tuplas
R = tuple(R)

# Imprimir la matriz resultante
print(R)
