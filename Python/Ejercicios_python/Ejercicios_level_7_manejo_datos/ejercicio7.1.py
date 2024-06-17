# Escribir una función que pida un número entero 1 y 10 y guarde enm un fichero con el nombre <tabla-n.txt> la tabla de multiplicar de ese número, donde <n> es el número introducido.

def crear_tabla_multiplicar(n):                               # Función para crear un archivo .txt con una tabla de multiplicar                                       # Se añade a la lista <l> el numero de iteración * valor introducido <n>
  nom = f"tabla-{n}.txt"
  with open (f"{nom}", 'w') as f:   # Se crea (o sobreescribe) con el modo <'w'> (write) un archivo <tabla-{n}.txt> y se guarda en la variable <f>
    for i in range(1, 11):                                    # Se itera por los valores del 1 al 10
      f.write(f"{i} * {n} = {i*n}\n")                         # En el archivo <tabla-{n}> se escribe la tabla de <n>
    print(f"Se ha creado un archivo con el titulo {nom} que contiene la tabla del {n}")

n = int(float(input("Pon un numero: ")))                      # El usuario introduce un numero <n>

crear_tabla_multiplicar(n)                                    # Se dispara la función con el parametro <n>


# Solución profe

""" c = True
while c:
  n = int(float(input("Numero del 0 al 10: ")))
  if 0 <= n <= 10:
    c = False
  else:
    print("Por favor mete un numero del 0 al 10: ")
    n = int(float(input("Numero del 0 al 10: ")))

nom = f"tabla-{n}.txt"

with open("salidas\\"+nom, 'w') as f:
  for k in range(1, 11):
    f.write(f"{n} x {k} = {n * k}\n") """