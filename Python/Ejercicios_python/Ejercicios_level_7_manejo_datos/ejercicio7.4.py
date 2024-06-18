# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

from urllib import request
from urllib.error import URLError

# Solucion profe

def scrap_i(url):
  """
    USO: recibe una url y cuenta el numero de palabras de la url
    PARAMETROS:
      url[str]: direccion url a inspeccionar
    VARIABLES:
      c[list]: lectura de las palabras presentes en la web de la url
      x[str]: contaje de palabras / advertencia si no existe o no se puede acceder al archivo de la url
    RETURN:
      x[str]: contaje de palabras / advertencia
  """
  try:
    with request.urlopen(url) as f:
      c = f.read()
  except URLError:
    x = "La url no existe o no se encuentra el fichero"
  else:
    x = len(c.split())
  return x

d = "https://docs.openstack.org/glance/ocata/_sources/sample-configuration.txt"

print(scrap_i(d))