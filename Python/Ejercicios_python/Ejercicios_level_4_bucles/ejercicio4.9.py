# Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta

c = 'abc123'                                                        # Se inicializia la variable contraseña
c_usuario = input("Escribe la contraseña: ")                        # El usuario pone la contraseña

while c_usuario != c:                                               # El bucle evalua si la contraseña introducida por el usuario coincide con la contraseña
  c_usuario = input("Contraseña incorrecta, vuelve a intetarlo: ")  # Si no coincide, se vuelve a pedir la contraseña al usuario en bucle
print("Contraseña correcta")                                        # Si la contraseña coincide se acaba el bucle y se informa al usuario
