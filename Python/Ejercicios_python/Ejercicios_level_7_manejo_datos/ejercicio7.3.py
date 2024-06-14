# Escribir una función que pida dos números <n> y <m> entre 1 y 10, lea el fichero <tabla-n.txt> con la tabla de multiplicar de ese número, y muestre por pantalla la línea <m> del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def leer_linea_tabla_multiplicar(n, m):   # Función para leer una linea de un archivo .txt con una tabla de multiplicar
  try:
    with open(f'C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\tabla-{n}.txt', 'r', encoding='UTF-8') as f: # Se abre el archivo en la <dirección>, en el modo <'r'> (read), y se guarda en la variable <f>
      lineas = f.readlines()              # Lee todas las lineas
      return lineas[m-1]                  # La función devuelve la lectura de la linea <m> (se pone m-1 porque el primer indice es 0, de esta manera es como si fuera 1)
  except FileNotFoundError:               # Manejo del error si no se encuentra el archivo <tabla-{n}.txt>
    print(f"No se encuentra el archivo tabla-{n}.txt")
  except IndexError:                      # Manejo del error si no se encuentra la linea <m>
    print(f"No se encuentra la linea {m}")

n = int(float(input("Pon un numero de tabla: ")))  # El usuario introduce el numero de tabla <n>
m = int(float(input("Pon un numero de linea: ")))  # El usuario introduce el numero de linea <m>

r = leer_linea_tabla_multiplicar(n, m)             # Se guarda el retorno de la función en la variable <r>

print(r)                                           # Se imprime la tabla de multiplicar que se ha leido
