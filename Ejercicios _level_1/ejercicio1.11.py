# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Despuñes el programa debe calcular y mostrar por la pantalla la cantidad de ahorros tras el primer, segundo y tercer año. Redondear cada cantidad a dos decimales

cantidad = int(input("Cantidad? "))
interes = 0.04

año1 = round(cantidad + (cantidad * interes), 2)
año2 = round(año1 + (año1 * interes), 2)
año3 = round(año2 + (año2 * interes), 2)

print(f"Primer año: {año1}, Segudo año: {año2}, Tercer año: {año3}")