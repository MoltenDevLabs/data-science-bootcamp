# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_08_10/?format=TSV&compressed=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país do todos los años disponibles.

import gzip
from urllib import request
from urllib.error import URLError

def abrir_fichero(url): # Función para abrir y leer el archivo de la url
  """
  USO: Abrir y leer el archivo de la url
  PARAMETROS:
    url[str]: url del archivo a abrir y leer
  VARIABLES:
    x[list / str]: lista de la lectura de lineas / string mostrando el error
  RETORNO:
    x[list / str]: lista de la lectura de lineas / string mostrando el error
  """
  try:
    with request.urlopen(url) as f:  # Abre el archivo y lo guarda en la variable 'f'
      with gzip.GzipFile(fileobj=f) as f_unzip:  # Se utiliza gzip para descomprimir el archivo 'f'
        x = f_unzip.read().decode('utf-8').splitlines()  # Lee las lineas, las decodifica y las guarda en la variable 'x'
  except URLError:
      x = "La url no existe o no se encuentra el fichero"
  return x

def mostrar_PIB(x, p):
  """
  USO: mostrar los datos del PIB del pais seleccionado
  PARAMETROS:
    x[list]: lista de lineas del archivo
    p[str]: iniciales del pais a inspeccionar pasado por el usuario
  VARIABLES:
    y[list]: lista para almacenar las lineas que corresponden al pais seleccionado
  RETORNO:
    info[str]: informacion formateada del PIB del pais escogido
  """
  y = []                     # Se inicializa la lista 'y' vacia
  headers = x[0].split('\t') # Se asigna a la variable header la primera linea de datos separados por tabulacion (ya que el archivo a leer es .tsv (tab separated values))
  for l in x[1:]:            # Se itera por las lineas de los datos empezando por la segunda (ya que la primera es para los headers)
    lines = l.split('\t')    # Para cada iteración se guarda el resultado de la linea de datos separada por tabulacion en la variable 'lines'
    if lines[0].startswith(p):  # Se comprueba si la primera columna coincide con las iniciales intoducidas por el usuario
      y.append(lines)        # Si coincide, se guardan los datos correspondientes a esa linea en la lista 'y'
  
  info = []   # Se inicializa la lista 'info' vacia
  for r in y: # Se itera sobre la lista creada en el apartado anterior que contiene la información del pais seleccionado por el usuario
    values = zip(headers[1:], r[1:])  # Se juntan los valores de la lista headers y los de cada columna de la lista 'y'
    info.append("\n".join([f"{año}: {valor}" for año, valor in values]))  # Se formatean los valores como 'año: valor' de 'values'
  
  return info

d = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_08_10/?format=TSV&compressed=true"
p = input("Pon las 2 iniciales de un país: ").upper()

print(abrir_fichero(d))