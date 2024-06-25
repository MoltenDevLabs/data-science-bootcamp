# Dada una lista de precios de productos, utiliza una función lambda para aplicar un descuento del 10% a los productos cuyo precio sea mayor a 100. Para los productos cuyo precio sea menor o igual a 100, aplicar un descuento del 5%.

precios = [400.52, 60.32, 50.14, 120.35, 100.54, 25.78]

descuento = list(map(lambda x: x*0.9 if x >= 100 else x*0.95, precios))

print(descuento)
