# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

n = input("Pon una palabra: ")   # El usuario pone una palabra

for n in range(10):              # Se itera la palabra en un rango de 10
  print(n)                       # Se imprime la palabra introducida para cada iteracion


## Solución profe

p = input("Pon una palabra: ")
# opcion for
for k in range(10):
  print(p)

# opcion while
c = 1
while c <= 10:
  print(p)
  c += 1
