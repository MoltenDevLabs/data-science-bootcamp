# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

from urllib import request
from urllib.error import URLError



""" def url_word_counter(file):
  c = 0
  try:
    with open(file, 'r', encoding='utf-8') as f:
      words = f.readlines().split(" ")
      for i in words:
        c += 1
    return c
  except Exception as e:
    print(f"Error: {e}")

count = url_word_counter(url)
print(count) """


# Solucion profe

def scrap_i(url):
  """
  
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