# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato "dd de <mes> de aaaa" donde <mes> es el nombre del mes.

c = {'01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto', '09': 'septimebre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}

f = input("Pon una fecha en formato dd/mm/aaaa: ")  # El usuario pone una fecha en formato dd/mm/aaaa

d, m, a = f.split('/')                              # Se separa la fecha introducida por el usuario por el simbolo '/' y se guardan la primera parte en la variable d, la segunda en m y la tercera en a

print(f"{d} de {c[m]} de {a}")                      # Se imprime el dia tal como lo ha puesto el usuario, para el mes se usa la clave correspondiente al valor introducido y el año tal como lo ha puesto el usuario
