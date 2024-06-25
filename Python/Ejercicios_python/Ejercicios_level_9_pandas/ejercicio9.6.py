productos = [
  {"nombre": "Producto A", "precio": 150, "cantidad": 30},
  {"nombre": "Producto B", "precio": 85, "cantidad": 50},
  {"nombre": "Producto C", "precio": 120, "cantidad": 5},
  {"nombre": "Producto D", "precio": 200, "cantidad": 20},
  {"nombre": "Producto E", "precio": 75, "cantidad": 40},
  {"nombre": "Producto F", "precio": 110, "cantidad": 15}
]

precio_mayor_100 = list(filter(lambda x: x["precio"]> 100, productos))

print(precio_mayor_100)
