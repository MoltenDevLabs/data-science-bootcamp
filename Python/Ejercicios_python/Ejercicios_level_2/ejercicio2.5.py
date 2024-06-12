# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida

frase = input("Escribe una frase: ")
x = []

for char in frase:
  x.append(char)

x_rev = x[::-1]
frase_invertida = ''.join(x_rev)

print(frase_invertida)