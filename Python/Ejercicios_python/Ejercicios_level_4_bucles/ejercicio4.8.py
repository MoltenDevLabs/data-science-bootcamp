# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo resctángulo como el que se muestra más abajo
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

n = int(float(input("Pon un número: "))) # El usuario introduce un entero n

r = ''                             # Se inicializa r como string vacio
for i in range(1, n+1):            # Se recorren los números desde 1 hasta n
  if i % 2 != 0:                   # Entran los números impares
    r += str(i) + " "              # Al string r se le añade el número impar y un espacio
    print(r[::-1])                 # Para cada iteración de imprime el string r al revés
