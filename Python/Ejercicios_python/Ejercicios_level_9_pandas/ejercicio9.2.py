# Dada una lista de puntuaciones de exámenes, utiliza una función lambda para clasificar cada puntuación en "Aprobado" o "Reprobado". Una puntuación de 60 o más es considerada "Aprobado".

examenes = [5.34, 2.94, 8.23, 5.45, 7.30, 9.42, 4.99, 1.02]

calificaciones = list(map(lambda x: "Aprobado" if x >= 6 else "Reprobado", examenes))

print(calificaciones)
