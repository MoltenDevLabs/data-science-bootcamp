# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir", que terminará

x = input("Introduce algo: ")
while x != 'salir':
  print(x)
  x = input("Introduce otra cosa: ")

print("Adiós")