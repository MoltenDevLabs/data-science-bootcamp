# Crear una función llamada calificación que dada una nota pasada por parámetro nos diga si esta aprobado o suspenso. 
# El criterio de calificación es: 
  # Los suspensos son aquellas notas menores a cinco. 
  # Los aprobados notas hasta siete. 
  # Los notables hasta nueve. 
  # Los sobresalientes aquellos que tengan nueve y su parte fraccionaria hasta llegar diez.
  # Las matriculas son los 10.

def calificacion(nota):
  if nota < 5:
    c = "Suspenso"
  elif nota < 7:
    c = "Aprobado"
  elif nota < 9:
    c = "Notable"
  elif nota < 10:
    c = "Sobresaliente"
  elif nota == 10:
    c = "Matricula"
  else:
    c = "La nota debe ser de 0 a 10"
  
  return c

print(calificacion(11))