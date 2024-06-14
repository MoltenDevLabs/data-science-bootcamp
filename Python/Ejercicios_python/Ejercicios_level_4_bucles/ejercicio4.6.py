# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido

n = int(float(input("Pon un entero: "))) # El usuario introduce un entero

e = '*'                             # Se inicializa el string e con '*'
for i in range(1, n+1):             # Se recorre el rango de números de 1 hasta el introducido por el usuario
  print(e*i)                        # Se imprimen las * desde una hasta el número introducido por el usuario
