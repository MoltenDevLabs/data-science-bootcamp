# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pàntalla la misma frase pero con la vocal introducida en mayúscula

frase = input("Pon una frase: ")
vocal = input("Pon una vocal: ")

frase_may = ''

for char in frase:
  if char == vocal:
    frase_may += char.upper()
  else:
    frase_may += char

print(frase_may)