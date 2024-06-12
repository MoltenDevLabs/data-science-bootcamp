# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptasr el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Pon tu fecha de nacimiento: ")   # Introducción de datos en formato dd/mm/aaaa

x = fecha.split('/')                            # Separar en strings por el carácter ('/')
dia, mes, año = x[0], x[1], x[2]                # Asignar variables a los distintos strings

print(f"Día: {dia}, mes: {mes}, año: {año}")    # Imprir por pantalla