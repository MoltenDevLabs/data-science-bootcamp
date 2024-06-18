# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: <Nombre> (nombre de la empresa), <Final> (precio de la acción al cierre de bolsa), <Màximo> (precio máximo de la acción durante la jornada), <Mínimo> (precio mínimo de la acción durante la jornada), <Volumen> (Volumen al cierre de bolsa), <Efectivo> (capitalización al cierre en miles de euros).
# 1. Construir una función que reciba el fichero cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
# 2. Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de cada columna.

import csv

def csv_to_dict(file):
  """
  USO: convertir los datos de un archivo csv a una lista de diccionarios
  PARAMETROS:
    file[str]: dirección del archivo csv a leer
  VARIABLES:
    data[list]: lista para almacenar los diccionarios con la informacion / errores
    headers[list]: valores correspondientes a la linea en la primera posicion
    rows[list]: valores correspondientes a las lineas a partir de la segunda posicion
    dic[dict]: diccionarios resultado de juntar cada header y value en la misma posicion
  RETURN:
    data[list]: lista de diccionarios con la informacion del archivo csv ordenada / errores
  """
  data = []                                     # Se inicializa la lista vacia 'data' para guardar los diccionarios 
  try:
    with open(file, 'r', encoding="utf-8") as f:
      lines = f.readlines()                     # Se leen todas las lineas y se guardan en la variable 'lines'
      headers = lines[0].strip().split(';')     # La linea 0 corresponde a los headers, guardamos los valores en la variable headers que usaremos como claves en el diccionario
      for line in lines[1:]:                    # Empezamos a leer las lineas en la 1, ya que la 0 son los headers. Usaremos estas lineas como valores en el diccionario
        rows = line.strip().split(';')          # El valor de cada linea se guarda en la variable 'rows'. Se usa strip() para quitar los saltos de linea ('\n')
        dic = {headers[i]: rows[i] for i in range(len(headers))} # Se crea una compresion de diccionario a partir de 2 listas (lista headers y lista rows). Empareja el elemento en la posicion 'i' de la lista headers con el elemento en posición 'i' de la lista rows con la longitud de la lista headers
        data.append(dic)                        # Se guarda cada diccionario en la lista 'data', formando una lista de diccionarios.
  except FileNotFoundError:
    data = (f"Error: File '{file}' not found.")
  except Exception as e:
    data = (f"Error: {e}")
  return data

file_path = "C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\Python\\Ejercicios_python\\Ejercicios_level_7_manejo_datos\\cotizacion.csv"
print(csv_to_dict(file_path))

def dict_to_csv(data, csv_output):
  """
  USO: a partir de los datos de la funcion csv_to_dict crear un archivo csv
  PARAMETROS:
    data[list]: lista de diccionarios que es el return de la funcion csv_to_dict
    csv_output[str]: nombre del archivo resultante
  VARIABLES:
    file_csv[]: 
  RETURN:
    x[str]: advertencia de que el archivo a sido creado / error
  """
  try:
    with open(csv_output, 'w', newline='', encoding='utf-8') as f:
      file_csv = file_csv.writer(f)
      x = "Fichero creado"
  except Exception as e:
    x = (f"Error: {e}")
  return x

print(dict_to_csv(csv_to_dict(file_path)))