# Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc) que se le pida al usuario. Cada vez que se añada un nuevo daro deve imprimirse el contenido del diccionaro

d = {}

n = input("Pon tu nombre: ")
d['Nombre'] = n
print(d)

e = input("Pon tu edad: ")
d['Edad'] = e
print(d)

s = input("Pon tu sexo: ")
d['Sexo'] = s
print(d)

t = input("Pon tu teléfono: ")
d['Teléfono'] = t
print(d)
