# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def fun1(f):
  """
  USO: cuenta las letra de cada una de las palabras
  PARAMETROS:
    f[str]: frase a analizar
  VARIABLES:
    lp[list]: lista de las palabras de la frase
    lon[map]: evalua la funcion len sobre los elementos de la lista lp
    d[dict]: guarda el contaje de letras de cada palabra
  RETURN:
    d[dict]: guarda el contaje de letras de cada palabra
  """
  lp = f.split()
  lon = map(len, lp)
  d = dict(zip(lp,lon)) 
  return(d)

F = "el perro verde es verde"

print(fun1(F))