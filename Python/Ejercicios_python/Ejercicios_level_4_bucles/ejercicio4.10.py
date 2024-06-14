# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no

n = int(float(input("Pon un número: ")))    # El usuario introduce un entero (n)

primo = True                                # Se inicializa la variable primo a True

for i in range (2, n):                      # Se recorre el rango de números de 2 hasta n-1
  if (n % i) == 0:                          # Se evalua si n entre cada número de 2 hasta n-1 tiene un módulo de 0
    primo = False                           # Si algún módulo da 0 la variable primo pasa a ser False

if primo:                                   # Se evalua la variable primo
  print(f"{n} es un número primo")          # Si es True se imprime que el número es primo
else:                                       
  print(f"{n} no es un número primo")       # Si es False se imprime que el número no es primo

# Solución profe

for k in range(2, n):
  if n % k == 0:
    break

if k+1 == n:
  print("Solución profe: Es primo")
else:
  print("Solución profe: No es primo")
