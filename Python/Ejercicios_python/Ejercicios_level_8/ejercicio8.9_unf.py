# Dada una lista de palabras, genera un diccionario donde las claves sean las palabras y los valores sean listas con todas las permutaciones posibles de las letras de la palabra. Usa comprensión de diccionarios.

lista = ["Hola", "Mundo", "Python"]
values = []

dic = {i:j for i in lista for j in i}

print(dic)