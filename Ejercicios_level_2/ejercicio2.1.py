# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido

nombre = input("Como te llamas? ")
numero = int(input("Pon un número: "))

for n in range(0, numero):
  print(f"{nombre}")