# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario

d = {'euro':'€', 'dollar':'$', 'yen':'¥'}           # Diccionario con las divisas como clave y los símbolos como valor

m = input("Pon una divisa: ")                       # El usuario pone una divisa

if m.lower() in d:                                  # Se evalua si el input del usuario esta en el diccionario d
  print(d[m])                                       # Si encuentra la clave se imprime el valor de la clave encontrada
else:
  print(f"La divisa {m} no esta en el diccionario") # Sino se imprime que la divisa no esta en el diccionario
