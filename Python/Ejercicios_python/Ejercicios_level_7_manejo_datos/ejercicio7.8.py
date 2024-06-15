# El fichero <calificaciones.csv> contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:
# 1. Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
# 2. Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a acada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoía en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
# 3. Una función que reciba una lista de diccionarios como la que devuelve la función anteriro y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

file = r"C:\Users\polka\OneDrive\Escritorio\data-science-bootcamp\Python\Ejercicios_python\Ejercicios_level_7_manejo_datos\calificaciones.csv"

def dic(file):
  data = []
  try:
    with open(file, 'r', encoding='utf-8') as f:
      lines = f.readlies()
      headers = f[0].split(';')
      for l in lines:
        rows = l.split(';')
  return data      
  except Exception as e:
    print(f"Error: {e}")