# Dada una lista de palabras, genera un nuevo diccionario que contenga como claves las palabras originales y como valores las palabras invertidas, pero sólo si la palabra original tiene más de 5 caracteres y no contiene ninguna vocal. Usa comprensión de diccionarios.

palabras = ['anchoa', 'atún', 'salmón', 'ba', 'tib', 'zxcvb', 'zx', 'bcdfghjklm', 'qrstvwxyz', 'fghjklmnp', 'bcdflnprstv']
vocales = ['a', 'e', 'i', 'o', 'u']

dic = {i: i[::-1] for i in palabras if len(i) >= 5 and not any(letra in i for letra in vocales)}

print(dic)
