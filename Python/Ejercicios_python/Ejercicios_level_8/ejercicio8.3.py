# Crea un diccionario donde las claves sean los números del 1 al 100 y los valores sean una tupla con el cuadrado y la raíz cuadrada del número. Usa comprensión de diccionarios.

dic = {i: tuple((i**2, i**0.5)) for i in range(1, 100)}

print(dic)
