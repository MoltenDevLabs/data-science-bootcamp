import os as so
uri = "salidas\\listin.txt"
try:
    so.remove(uri)
    x = "Fichero borrado"
except FileExistsError:
    x = "No existe el fichero o la uri es invalida"
except PermissionError:
    x = "No tienes privilegios para borrar el fichero"
except Exception as error:
    x = f"Se ha producido un error desconocido.\nSe ha producido el error: {error}"