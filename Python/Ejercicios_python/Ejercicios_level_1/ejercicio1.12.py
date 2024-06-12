# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barra_hoy = 3.49
barra_ayer = barra_hoy * 0.4

n_barras = int(input("Cuantas barras? "))

precio_barras_hoy = round((barra_hoy * n_barras), 2)
precio_barras_ayer = round((barra_ayer * n_barras), 2)
descuento = round((precio_barras_hoy - precio_barras_ayer), 2)

print(f"Si las barras fueran de hoy costraian {precio_barras_hoy}, como son de ayer te ahorras {descuento}, el precio final es {precio_barras_ayer}")