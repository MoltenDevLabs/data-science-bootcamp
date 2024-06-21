# Genera una lista de tuplas (i,j,k) donde i y j son números entre 1 y 50, y k es un número entre 1 y 100, tales que i+j=k. Usa una lista de comprensión.

# Solución sin comprensión de listas
""" list = []
for i in range(1,51):
  for j in range(1,51):
    k = i + j
    if k < 100:
      list.append((i, j, k))

for l in list:
  print(l) """

# Solución con comprensión de listas
comp_list = [tuple((i, j, i+j)) for i in range(1,51) for j in range(1,51) if i+j < 100]

for tup in comp_list:
  print(tup)