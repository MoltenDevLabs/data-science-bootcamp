# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe incorporar funciones para crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado  en el fichero de texto <listin.txt> donde el nombre del cliente y su teléfono deven aparecer separados por comas y cada cliente en una línea distinta.

def write_listin(n, t):                                 # Functión para crear el listin y poner el primer valor
  with open(f"listin.txt", 'w', encoding='utf-8') as f:
    f.write(f"{n}, {t}\n")
    print(f"Se ha creado el listin con {n}")

def add_listin(n, t):                                   # Función para añadir valores al listin
  with open(f"listin.txt", 'a', encoding='utf-8') as f:
    f.write(f"{n}, {t}\n")
    print(f"Se ha añadido {n} al listin")

def read_listin():                                      # Función para leer el listin entero
  try:
    with open(f"listin.txt", 'r', encoding='utf-8') as f:
      c = f.read()
      print(c)
  except FileNotFoundError:
    print("El archivo listin.txt no existe")

def read_line(n):                                       # Función para leer la linea del nombre introducido
  try:
    with open(f"listin.txt", 'r', encoding='utf-8') as f:
      found = False
      l = f.readlines()
      for i in l:                                       # Iterar por todas las lineas del listin
        if i.startswith(n):                             # Si la linea coincide con el nombre introducido entra
          print(i)
          found = True
          break
      if not found:
        print(f"No se encontró {n}")
  except FileNotFoundError:
    print("El archivo listin.txt no existe")

def erase_line(n):                                        # Función para borrar una entrada del listin
  try:
    with open(f"listin.txt", 'r', encoding='utf-8') as f: # Pimero se leen las lineas
      l = f.readlines()
    found = False
    with open(f"listin.txt", 'w', encoding='utf-8') as f: # Luego se sobreescribe la linea que coincide con el nombre
      for i in l:
        if not i.startswith(n):
          f.write(i)
        else:
          found = True
    if found:
      print(f"Se ha borrado {n}")
    else:
      print(f"No se encontró {n}")
  except FileNotFoundError:
    print("El archivo listin.txt no existe")


i = input("Introduce instrucción: 'w' para write, 'a' para add, 'r' para read, 'rl' para read line, 'e' para erase: ").lower() # El usuario escoje la acción a realizar
if i == "w":                    # Acción write
  n = (input("Nombre: "))
  t = int(input("Teléfono: "))
  write_listin(n, t)
elif i == "a":                  # Acción add
  n = (input("Nombre: "))
  t = int(input("Teléfono: "))
  add_listin(n, t)
elif i == "r":                  # Acción read
  read_listin()
elif i == "rl":                 # Acción read line
  n = (input("Nombre: ")).lower()
  read_line(n)
elif i == "e":                  # Acción erase
  n = (input("Nombre: ")).lower()
  erase_line(n)
else:
  i = input("Instrucción desconocida: 'w' para write, 'a' para add, 'r' para read, 'rl' para read line, 'e' para erase: ").lower()
