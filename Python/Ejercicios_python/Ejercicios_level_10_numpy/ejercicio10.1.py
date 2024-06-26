# Ejercicio 106

import numpy as np

matriz_aleatoria = np.random.random((4,3,24))
print(f"Matriz aleatoria:\n{matriz_aleatoria}")

media_total = np.mean(matriz_aleatoria)
print(f"\nMedia: {media_total}")

media_dimension_0 = np.mean(matriz_aleatoria, axis=0)
print(f"\nMedia_dimension_0:\n{media_dimension_0}")
media_dimension_1 = np.mean(matriz_aleatoria, axis=1)
print(f"\nMedia_dimension_1:\n{media_dimension_1}")
media_dimension_2 = np.mean(matriz_aleatoria, axis=2)
print(f"\nMedia_dimension_2:\n{media_dimension_2}")

matriz_resta = matriz_aleatoria - media_total
print(f"\nMatriz_resta:\n{matriz_resta}")

norma_frobenius = np.linalg.norm(matriz_resta)
print(f"\nNomra de Forbenius: {norma_frobenius}")
