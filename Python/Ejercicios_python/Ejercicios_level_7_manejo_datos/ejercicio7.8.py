# El fichero <calificaciones.csv> contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:
# 1. Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
# 2. Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a acada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoía en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
# 3. Una función que reciba una lista de diccionarios como la que devuelve la función anteriro y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

def csv_to_dict(file):
  """
  USO: convierte la informacion del archivo csv en una lista de diccionarios
  PARAMETROS:
    file[]: archivo csv con la informacion a convertir
  VARIABLES:
    data[list / str]: lista de diccionarios con la informacion / error
    headers[]: primera linea 
  RETURN:
    data[list / str]: lista de diccionarios con la informacion / error
  """
  data = [] # Se inicializa la lista vacia 'data' para guardar los diccionarios 
  try:
    with open(file, 'r', encoding='utf-8') as f:
      lines = f.readlines()                                     # Se leen todas las lineas y se guardan en la variable 'lines'
      headers = lines[0].strip().split(';')                     # Se guarda la primera linea en la variable 'hearders'
      for line in lines[1:]:                                      # Se iteran por las lineas a partir de la segunda
        rows = line.strip().split(';')                            # Cada linea se guarda en la variable 'rows'
        dic = {headers[i]: rows[i] for i in range(len(headers))}  # Se crea un diccionario emparejando 'headers' y 'rows' en el rango de la longitud de headers
        data.append(dic)                                          # Cada diccionario se guarda en la lista 'data' creando así una lista de diccionarios
      data = sorted(data, key = lambda x: x['Apellidos'])       # Se ordena la lista por la clave 'Apellidos'
  except FileNotFoundError:
    data = (f"Error: File '{file}' not found.")
  except Exception as e:
    data = (f"Error: {e}")
  return data                      # La funcion devuelve la variable 'data' que es la lista de diccionarios con la información de los alumnos ordenados por apellidos

file_path = "C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\Python\\Ejercicios_python\\Ejercicios_level_7_manejo_datos\\calificaciones.csv"
data = csv_to_dict(file_path)   # Se guarda el return de la funcion csv_to_dict(file_path) en la variable 'data'
print(f"Lista de diccionarios ordenada por apellido:\n{data}")

def nota_final(data):   # Funcion para añadir la nota final a cada alumno
  """
  USO: Añade una columna con clave 'NotaFinal' y como valor la ponderación de los parciales y las practicas
  PARAMETROS:
    data[list]: lista de diccionarios que corresponde al return de la funcion csv_to_dict()
  VARIABLES:
    data_final[list]: lista de diccionarios con la columna 'NotaFinal' añadida / error
  RETURN:
    data_final[list]: lista de diccionarios con la columna 'NotaFinal' añadida / error
  """
  data_final = []   # Se inicializa 'data_final' como lista vacia para guardar el resultado de la funcion
  try:
    for dic in data:    # Si algun valor es string vacio, se convierte en 0 para poder operar
      if dic['Parcial1'] == '':
        dic['Parcial1'] = 0
      elif dic['Parcial2'] == '':
        dic['Parcial2'] = 0
      elif dic['Practicas'] == '':
        dic['Practicas'] = 0
      else:
        parcial1 = float(dic['Parcial1'].replace(',', '.'))   # Se canvia la coma por un punto y se convierte a float para poder operar
        parcial2 = float(dic['Parcial2'].replace(',', '.'))
        practicas = float(dic['Practicas'].replace(',', '.'))
        suma_final = round((parcial1*0.3) + (parcial2*0.3) + (practicas*0.4), 2)  # Se suma cada parte con el porcentaje que le corresponde y se redondea a 2 decimales
        dic['NotaFinal'] = suma_final   # Se añade un nuevo apartado al diccionario con la clave 'NotaFinal' y con el valor 'suma_final'
        data_final.append(dic)    # Se añade cada nuevo dicconario con 'NotaFinal' a la lista 'data_final'
  except Exception as e:
    data_final = (f"Error: {e}")
  return data_final   # La funcion devuelve la variable 'data_final' que contiene la lista de diccionarios 'data' con una columna añadida que es la 'NotaFinal'

data_final = nota_final(data)
print(f"\nLista de diccionarios con NotaFinal:\n{data_final}")

def aprobados_suspensos(data_final):
  """
  USO: a partir del diccionario data_final se crean dos listas de diccionarios, separando alumnos aprobados de alumnos suspendidos
  PARAMETROS: 
    data_final[list]: lista de diccionarios resultado de la funcion nota_final()
  VARIABLES:
    aprobados[list]: lista de diccionarios con los alumnos aprobados
    suspensos[list]: lista de diccionarios con los alumnos suspendidos
  RETURN:
    aprobados[list]: lista de diccionarios con los alumnos aprobados
    suspensos[list]: lista de diccionarios con los alumnos suspendidos
  """
  aprobados = []    # Se crea 'aprobados' como lista vacia para almacenar los diccionarios de los alumnos aprobados
  suspensos = []    # Se crea 'suspensos' como lista vacia para almacenar los diccionarios de los alumnos suspensos
  try:
    for dic in data_final:                # Si algun valor es string vacio, se convierte en 0 para poder operar
      if dic['Parcial1'] == '':
        dic['Parcial1'] = 0
      elif dic['Parcial2'] == '':
        dic['Parcial2'] = 0
      elif dic['Practicas'] == '':
        dic['Practicas'] = 0
      else:
        asistencia = int(dic['Asistencia'].replace('%', ''))    # Se elimina el simbolo '%' de la asistencia y se convienrte en int para poder operar
        parcial1 = float(dic['Parcial1'].replace(',', '.'))   # Se canvia la coma por un punto y se convierte a float para poder operar
        parcial2 = float(dic['Parcial2'].replace(',', '.'))
        practicas = float(dic['Practicas'].replace(',', '.'))
        if asistencia >= 75 and parcial1 >= 4 and parcial2 >= 4 and practicas >= 4 and dic['NotaFinal'] >= 5:   # Se comprueba que los alumnos han pasado los distintos requisitos para aprobar
          aprobados.append(dic)   # Si los han pasado se añaden a la lista 'aprobados'
        else:
          suspensos.append(dic)   # Si no los han pasado se añaden a la lista 'suspensos'
  except Exception as e:
    return (f"Error: {e}")
  return aprobados, suspensos   # La funcion devuelve las dos listas, 'aprobados' y 'suspensos'

aprobados, suspensos = aprobados_suspensos(data_final)
print(f"\nLista de aprobados:\n{aprobados}\n\nLista de suspensos:\n{suspensos}")
