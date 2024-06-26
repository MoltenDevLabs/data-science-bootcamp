# Ejercicio 108

import numpy as np

A = np.array([[3,4,-1],[2,-1,3],[5,2,2]]) # Matriz de coeficientes
B = np.array([1,4,-1])  # Matriz de valores constantes

X = np.linalg.solve(A, B)

print(X)
print(f"x = {X[0]}, y = {X[1]}, z = {X[2]}")

