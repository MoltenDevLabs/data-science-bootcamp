# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido

precio = input("Cual es el precio (con 2 decimales)? ")                 # Poner el precio

eur = precio.split('.')                                                 # Dividir el string por el punto ('.')
n_euros = eur[0]                                                        # Asignar variable n_euros a la parte de delante del punto
n_centimos = eur[1]                                                     # Asignar variable n_centimos a la parte de después del punto

print(f"Número de euros: {n_euros}, número de centimos: {n_centimos}")  # Imprimir por pantalla