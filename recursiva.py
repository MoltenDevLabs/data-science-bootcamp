def facotial(n):
  if n == 1:
    return 1
  else:
    return n * facotial(n - 1)

print(facotial(int(input('Escribe un numero: '))))