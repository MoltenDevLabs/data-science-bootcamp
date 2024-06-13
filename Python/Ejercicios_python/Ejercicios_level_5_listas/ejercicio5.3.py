# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y despúes las muestre por pantalla con el mensaje "En <asignatura> has sacado <nota>", donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario

a = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]  # Se crea la lista a
n = []                                                          # Se inicializa la variable n como lista vacia

for i in a:                                                     # Se itera sobre la lista a
  nota = input(f"Que nota has sacado en {i}? ")                  # Se pregunta al usuario que nota ha sacado para cada una de las asignaturas y se guarda en la variable nota
  n.append(nota)                                                # Se añade la variable nota a la lista n

for i in range(len(a)):                                         # Se itera sobre los elementos de la lista a
  print(f"En {a[i]} has sacado un {n[i]}")                       # Se imprime la frase con la nota de la lista n para cada una de las asignaturas de la lista a