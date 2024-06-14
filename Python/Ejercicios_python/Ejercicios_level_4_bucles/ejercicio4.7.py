# Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10

n = 1                             # Se inicializa la variable n
while n < 11:                     # Se recorre el bucle mientras n sea menor a 11
  for i in range(1, 11):          # Se recorre el rango de números del al 10 sin modificar n
    print(f"{n}*{i} = {n*i}")     # Se imprime el valor de n, de i y el resultado n*i
  n += 1                          # Se suma 1 a la n y vuelve a empezar el bucle while
  