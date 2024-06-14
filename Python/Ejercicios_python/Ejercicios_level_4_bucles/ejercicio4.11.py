# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última

p = input("Pon una palabra: ")  # El usuario introduce una palabra

for i in p[::-1]:               # Se recorren las letras de la palabra al revés
  print(i)                      # Se imprimen las letras una a una


# Solución profe

for k in range(len(p) -1, -1, -1):
  print(f"Solución profe: {p[k]}")
