# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla el mensaje "Yo estudio <asignatura>", donde <asignatura> es cada una de las asignaturas de la lista

a = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]  # Se crea la lista a

for i in a:                                                     # Se itera sobre la lista a
  print(f"Yo estudio {i}")                                      # Se imprime tantas veces la frase como elementos tiene a donde i es cada una de las asignaturas
