# Genera una lista de tuplas (i,j) donde i y j son números entre 1 y 100, i<j, y el producto i*j es divisible entre 7. Usa una lista de comprensión.

list = [tuple((i,j)) for i in range(1, 101) for j in range(1, 100) if i<j and (i*j)%7==0]

print(list)
