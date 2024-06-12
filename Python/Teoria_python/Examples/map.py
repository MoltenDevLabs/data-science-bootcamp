# Función map
# Para mas ejemplo mirar ejercicio3.6

n = [1, 2, 3, 4]
r = map(lambda x: x+x, n)

print(list(r))

m, M = [1, 2, 3, 4], [5, 6, 7, 8]
rr = map(lambda x,y: x+y, m, M)

print(list(rr))