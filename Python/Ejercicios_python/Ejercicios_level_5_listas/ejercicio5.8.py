# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

p = input("Pon una palabra: ")        # El usuario pone una palabra

if p == p[::-1]:                      # Se compara la palabra con la palabra al revés
  print(f"{p} es un palíndromo")      # Si son iguales se impreme que la palabra es un palíndromo
else:
  print(f"{p} no es un palíndromo")   # Si son distintas se imprime que la palabra no es un palíndromo