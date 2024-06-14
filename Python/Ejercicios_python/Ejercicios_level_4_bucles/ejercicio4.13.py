# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir", que terminará

x = input("Introduce algo: ")           # El usuario introduce algo y se guarda en la variable x

while x != 'salir':                     # Se ejecuta el bucle a menos que el usuario introduzca el string 'salir'
  print(x)                              # Se imprime lo que el usuario ha introducido
  x = input("Introduce otra cosa: ")    # Se insta al usuario a introducir otra cosa que se guarda en la variable x y se inicia de nuevo el bucle

print("Adiós")                          # Si el usuario introduce el string 'salir' se imprime "Adiós"
