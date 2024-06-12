# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales

producto = input("Como se llama el producto? ")
precio = float(input("Cuanto vale? "))
unidades = int(input("Cuantas unidades llevas? "))

precio_total = precio*unidades

print(f"{producto} vale {precio:09.2f}; {unidades:03} unidades tienen un coste total de {precio_total:11.2f}")