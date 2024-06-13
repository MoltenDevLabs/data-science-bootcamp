# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar
# El producto escalar es la suma de los productos de cada par de elementos. En este caso es (1·-1)+(2·0)+(3·2) = -1 + 0 + 6 = 5

v1 = [1, 2, 3]            # Se inicializa el vector 1 como lista
v2 = [-1, 0, 2]           # Se inicializa el vector 2 como lista
prod = 0                  # Se inicializa el producto escalar en 0

for i in range(len(v1)):  # Se itera por los indices del vector 1
  prod += v1[i]*v2[i]     # Se suma el producto de los indices de v1 y v2

print(prod)               # Se imprime el resultado