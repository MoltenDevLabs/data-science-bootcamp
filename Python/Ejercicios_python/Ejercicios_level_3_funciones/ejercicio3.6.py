# Escribir una función que reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

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

notas = [6.67, 2.86, 8.64, 7.01, 4.9]
nota_cualitativa = list(map(calificacion, notas))
print(nota_cualitativa)