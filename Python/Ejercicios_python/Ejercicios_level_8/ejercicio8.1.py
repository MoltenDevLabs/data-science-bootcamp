# Crea un archivo CSV llamado "cartera-acciones.csv" mediante Microsoft Excel, cuyo contenido es el siguiente:
# names,shares,price
# "AA",100,32.20
# "IBM",50,91.10
# "CAT",150,83.44
# "MSFT",200,51.23
# "GE",95,40.37
# "MSFT",50,65.10
# "IBM",100,70.44
# Dicho CSV contiene la información sobre diferentes acciones (name), el número de acciones (shares) y el precio por acción (price). Se pide calcular el coste total de la cartera con una sola declaración de Python (compresion list)
# Usa el siguiente bloque de código para ayudarte:

# import csv
# with open('cartera-acciones.csv', 'r') as f:
#   filas = csv.reader(f)
#   headers = next(filas)   # Salta los encabezados
#   <<continuar_codigo>>

import csv

def total_cartera(file):
  with open(file, 'r', encoding='utf-8') as f:
    filas = csv.reader(f)
    headers = next(filas)   # Salta los encabezados
    """ total = 0           # Codigo sin usar comprensión de listas
      for i in filas:
      shares = int(i[1])
      price = float(i[2])
      total += shares*price """
    total = sum(int(i[1]) * float(i[2]) for i in filas) # Codigo usando comprensión de listas. Iteramos por cada fila (i[0] es name, i[1] es shares, i[2] es price)
  return total


file_path = "C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\Python\\Ejercicios_python\\Ejercicios_level_8\\cartera-acciones.csv"
print(total_cartera(file_path))
