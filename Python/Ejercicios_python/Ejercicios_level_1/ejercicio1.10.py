# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldán en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

payaso = int(input("Cuantos payasos? "))
muñeca = int(input("Cuantas muñecas? "))

peso_payaso = 112
peso_muñeca = 75

peso_total = (payaso*peso_payaso) + (muñeca*peso_muñeca)

print(peso_total,"g")