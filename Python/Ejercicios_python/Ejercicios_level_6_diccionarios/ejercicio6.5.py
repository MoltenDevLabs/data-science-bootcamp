# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso

a = {'Matemáticas': 6, 'Física': 4, 'Química': 5} # Se inicializa el diccionario a con las asignaturas como clave y los créditos como valor

for i, j in a.items():                            # Se itera por los pares clave-valor, donde i son las claves y j los valores
  print(f"{i} tiene {j} créditos")                # Para cada iteración de imprime el resutlado
