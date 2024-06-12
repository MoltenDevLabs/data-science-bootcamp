# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obrenido en la inversión

cantidad = int(input("Cantidad a invertir? "))
interes = int(input("Interés anual? "))
n_años = int(input("Cuantos años? "))

capital_obtenido = cantidad * (interes*0.01) * n_años

print(capital_obtenido)