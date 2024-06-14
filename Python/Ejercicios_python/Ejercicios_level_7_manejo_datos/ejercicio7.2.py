# Escribir una función que pida un número entero entre 1 y 10, lea el fichero <tabla-n.txt> con la tabla de multiplicar de ese número, donde <n> es el número introducido, y la muestre por pantalla. Si el fichero no existe deve mostrar un mensaje por pantalla informando de ello.

def leer_tabla_multiplicar(n):              # Función para leer un archivo .txt con una tabla de multiplicar
  try:
    with open(f'C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\tabla-{n}.txt', 'r', encoding='UTF-8') as f: # Se abre el archivo en la <dirección>, en el modo <'r'> (read), y se guarda en la variable <f>
      return f.read()                       # La función devuelve la lectura del archivo <f>
  except FileNotFoundError:                 # Manejo del error si no se encuentra el archivo <tabla-{n}.txt>
    print(f"No se encuentra el archivo tabla-{n}.txt")

n = int(float(input("Pon un número: ")))    # El usuario introduce un numero <n>

r = leer_tabla_multiplicar(n)               # Se guarda el retorno de la función en la variable <r>

print(r)                                    # Se imprime la tabla de multiplicar que se ha leido
