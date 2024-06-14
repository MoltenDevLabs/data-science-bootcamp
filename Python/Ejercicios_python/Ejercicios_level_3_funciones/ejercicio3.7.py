# Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúscilas y las calificaciones correspondientes a las notas.

def calificacion(n):
  c = ''
  if n<5:
    c = 'Suspenso'
  elif n<7:
    c = 'Aprobado'
  elif n<9:
    c = 'Notable'
  elif n<10:
    c = 'Sobresaliente'
  else:
    c = 'Matricula'
  
  return c

def aplicacion(d):
  materias = map(str.upper, d.keys())
  notas = map(calificacion, d.values())
  return dict(zip(materias, notas))

alberto = {'matematicas': 6.89, 'fisica': 5.01, 'quimica': 3.3, 'historia': 9.9, 'filosofia': 10}
print(aplicacion(alberto))
