
import os

f = "salidas\\listin.txt"
nc = "jose"
tc = "30495835"

def recuperar_telefono(f, c): # Falta normalizar variable de entrada
  """
  USO: devuelve el telefono del cliente en el fichero
  PARAMETROS:
    f[str]: fichero telefono - cliente
    nc[str]: nombre del cliente
  VARIABLES:
    nc[list]: lectura del fichero nombre - telefono
    x[str]: diccionario nombre - relefono / advertencia no existe el nombre
  RETURN:
    x[str]: telefono / advertencia
  """

  try:
    with open(f, 'r') as F:
      c = F.readlines()
  except FileNotFoundError:
    x = "Archivo no encontrado"
  else:
    x = dict([tuple(k.split(",")) for k in c])
  return x

def añadir_telefono(f, nc, tc):
  """
  USO: devuelve el telefono del cliente en el fichero
  PARAMETROS:
    f[str]: fichero telefono - cliente
    nc[str]: nombre del cliente
    tc[str]: telefono del cliente
  VARIABLES:
    F[doc]: lectura del fichero
    x[str]: diccionario nombre - relefono / advertencia no existe el nombre
  RETURN:
    y[str]: nombre del cliente y su telefono para escribir
    x[str]: telefono / advertencia
  """
  try:
    with open(f, 'a') as F:
      y = f"{nc}, {tc}\n"
      c = F.write()
  except FileNotFoundError:
    x = "Archivo no encontrado"
  else:
    x = "Se ha añadido el {nc} con el telefono {tc} a {f}"
  return x

def eliminar_telefono(f, nc):
  """
  USO: elimina el telefono del cliente del fichero
  PARAMETROS:
    f[str]: fichero telefono - cliente
    nc[str]: nombre del cliente
  VARIABLES:
    F[doc]: lectura del fichero
    p[list / dict]: lineas de la lectura del archivo por cada inedice del list 
                    que muta a un diccionario cuya clave es el nombre tras procesar el list anterior
    x[str]: advertencia no existe el nombre / advertencia de eliminacion de persona sobre el fichero
  RETURN:
    y[str]: nombre del cliente y su telefono para escribir con formato sobre el diccionario
    x[str]: telefono / advertencia
  """
  try:
    F = open(f, 'r')
  except FileNotFoundError:
    x = "Archivo no encontrado"
  else:
    p = F.readlines()
    F.close()
    p = dict([tuple(k.split(",")) for k in nc])
    if nc in p:
      del p[nc]
      F = open(f, 'w')
      for i, j in p.items():
        y = f"{i}, {j}"
        F.write(y)
      x = "Se ha eliminado el cliente {nc} con el telefono {tc} a {f}"
      F.close()
    else:
      x = "El cliente {nc} no existe en el fichero {f}"
  return x

def borrar_archivo(f):
  if os.path.isfile(f):
    r = input("¿Borramos el archivo? (Si - No)")
    if r == "Si":
      f = open(f, 'w')    # Se sobreescrive el archivo con el archivo en blanco
      f.close()
      x = "Se ha borrado el archivo"
    else:
      x = "No se ha borrado el archivo"
  return x