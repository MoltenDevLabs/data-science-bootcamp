# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después deve mostrar por pantalla el mensaje "<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>"

n = input("Pon tu nombre: ")                                              # El usuario pone su nombre y se guarda en la variable n
e = input("Pon tu edad: ")                                                # El usuario pone su edad y se guarda en la variable e
d = input("Pon tu dirección: ")                                           # El usuario pone su dirección y se guarda en la variable d
t = input("Pon tu teléfono: ")                                            # El usuario pone su teléfono y se guarda en la variable t

dic = {'Nombre': n, 'Edad': e, 'Dirección': d, 'Teléfono': t}             # Se inicializa el diccionario dic con las claves predeterminadas y los valores introducidos por el usuario

print(f"{dic['Nombre']} tiene {dic['Edad']} años, vive en {dic['Dirección']} y su número de teléfono es {dic['Teléfono']}")  # Se imprime la frase usando los valores del diccionario dic