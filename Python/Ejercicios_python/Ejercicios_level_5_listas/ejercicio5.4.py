# Escribir un programa que ´pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor

n = []                                      # Se inicializa la variable n como lista vacia
for i in range(6):                          # Se itera sore 6 numeros
  nl = int(input("Número de la lotería: ")) # Se asigna el numero introducido por el usuario a la variable nl
  n.append(nl)                              # Se añade nl a la lista n

n.sort()                                    # Se ordena la lista n de menor a mayor
print(n)                                    # Se muesta la lista n
