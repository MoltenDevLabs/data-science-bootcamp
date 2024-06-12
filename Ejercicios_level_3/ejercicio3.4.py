# Esctibir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

def par(x):
  """
  USO: Indica si un numero es divisible por dos
  PARAMETROS:
    x[int/float]: numero a operar
  RETURN:
    [bool]: resultado de operar division entera entre 2
  """
  
  return x % 2 == 0

def miFuncion(f, l):
  """
  USO: Aplica una funcion a los elementos de una lista si son int o float
  PARAMETROS:
    f[func]: funcion a aplicar
    l[list]: lista de valores a aplicar la funcion f
  VARIABLES:
    L[list]: lista de valores resultantes de aplicar la funcion
  RETURN:
    L[list]: lista de valores resultantes de aplicar la funcion
  """
  L = []
  for k in l:
    if type(k) == float or type(k) == int:
      if f(k):
        L.append(k)
    else:
      pass
  return L

v = [4, '2', 5., 8, '9']

print(miFuncion(par,v))


