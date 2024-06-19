# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa devbe mostrar por pantalla las asignaturas que el usuario tienen que repetir

a = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]  # Se crea la lista a

n = []                                                          # Se inicializa la variable n como lista vacia
for i in a:                                                     # Se itera sobre la lista a
  x = float(input(f"Que nota has sacado en {i}? "))               # Se pregunta al usuario la nota de cada asignatura
  n.append(x)                                                   # Se añaden las notas a la lista n

asus = []                                                       # Se inicializa la variable asus como lista vacia
for i in range(len(a)):                                         # Se itera en los elementos de la lista a
  if n[i] < 5:                                                  # Se comprueba si la nota de cada asignatura es menor a 5
    asus.append(a[i])                                           # Si es menor a 5 se añade a la lista asus

print(f"Has suspendido {asus}")                                 # Se muestra la lista asus
