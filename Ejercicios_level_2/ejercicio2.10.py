# Escribir un programa que pregunte por consola los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("Pon los productos de una cesta de la compra: ")

lista = productos.split(',')

for producto in lista:
  print(producto)
  