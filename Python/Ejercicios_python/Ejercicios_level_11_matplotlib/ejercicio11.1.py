# Ejercicio 124

import matplotlib.pyplot as plt

años = [1, 2, 3, 4, 5]
ventas = []
i = 0

while i < len(años):
  venta = int(input(f"Numero de ventas para el año {años[i]}: "))
  ventas.append(venta)
  i+=1

fig, ax = plt.subplots()
ax.plot(años, ventas, marker = '*')
ax.set_xlabel('Años')
ax.set_ylabel('Ventas')
ax.set_title('Ventas por año')

plt.show()
