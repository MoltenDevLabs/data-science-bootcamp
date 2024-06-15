# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: <Nombre> (nombre de la empresa), <Final> (precio de la acción al cierre de bolsa), <Màximo> (precio máximo de la acción durante la jornada), <Mínimo> (precio mínimo de la acción durante la jornada), <Volumen> (Volumen al cierre de bolsa), <Efectivo> (capitalización al cierre en miles de euros).
# 1. Construir una función que reciba el fichero cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
# 2. Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de cada columna.

# 1
file_path = r"C:\Users\polka\OneDrive\Escritorio\data-science-bootcamp\Python\Ejercicios_python\Ejercicios_level_7_manejo_datos\cotizacion.csv"

def csv_to_dict(file):
  data = []                                     # Se inicializa la lista vacia data para guardar los diccionarios 
  try:
    with open(file, 'r', encoding="utf-8") as f:
      lines = f.readlines()                     # Se leen todas las lineas
      headers = lines[0].strip().split(';')     # La linea 0 corresponde a los headers, guardamos los valores en la variable headers que usaremos como claves en el diccionario
      for line in lines[1:]:                    # Empezamos a leer las lineas en la 1, ya que la 0 son los headers. Usaremos estas lineas como valores en el diccionario
        values = line.strip().split(';')        # El valor de cada linea se guarda en la variable values. Se usa strip() para quitar los saltos de linea ('\n')
        row_dict = {headers[i]: values[i] for i in range(len(headers))} # Se crea una compresion de diccionario a partir de 2 listas (lista headers y lista values). Empareja el elemento en la posicion 'i' de la lista headers con el elemento en posición 'i' de la lista values con la longitud de la lista headers
        data.append(row_dict)                   # Se guarda cada diccionario en la lista data, formando una lista de diccionarios.
    return data                                 # La función devuelve la lista data con todos los diccionarios
  except FileNotFoundError:
    print(f"Error: File '{file}' not found.")
  except Exception as e:
    print(f"Error: {e}")

data = csv_to_dict(file_path)                        # Se guarda el retorno de la función 'csv_to_dict(file_path)' en la variable 'data'
print(data)

# 2
def dict_to_csv(data):
  try:
    with open(f"7.7data.csv, 'w', encoding='utf-8'") as f:
    
    return algo
  except Exception as e:
    print(f"Error: {e}")