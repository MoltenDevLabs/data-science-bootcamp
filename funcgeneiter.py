## Funciones iteradoras
# https://pypi.org/project // Librerias de Python

# map() (<<funcion>>, <<iterable>>)
# aplica una funcion sobre cada elemento de un iterable

l = [1,3,4,5]
def por2(i):
  return i*2
print(f"Ejemplo map: {list(map(por2, l))}") # Aplica la funcion por2 a los elementos de la lista l

# filter() (<<funcion>>, <<iterable>>)
# aplica una funcion sobre cada elemento que cumpla la condicion

l = [1,3,4,5]
pares = filter(lambda i: i % 2 == 0, l) # Aplica la funcion sobre los elementos que la condicion es true
print(f"Ejemplo filter: {list(pares)}")

# reduce() (<<funcion>>, <<iterable>>)
# no es propio de python, siempre hay que importarlo -> from functools import reduce

from functools import reduce  # Importar la funcion reduce() // pip install functools
from operator import add      # Importar la funcion add(), es para este ejemplo // pip install operator-courier

l = [1,3,4,5]
print(f"Ejemplo reduce: {reduce(add, l)}")      # Va a sumar cada elemento de la lista l