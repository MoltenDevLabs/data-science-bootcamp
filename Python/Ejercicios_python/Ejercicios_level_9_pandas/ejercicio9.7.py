empleados = [
  {"nombre": "Juan", "salario": 50000, "departamento": "Ventas"},
  {"nombre": "Ana", "salario": 60000, "departamento": "Marketing"},
  {"nombre": "Luis", "salario": 75000, "departamento": "IT"},
  {"nombre": "Marta", "salario": 45000, "departamento": "RRHH"}
]

impuesto = list(map(lambda x: {**x, "impuesto": x["salario"]*0.1}, empleados))

nombre_impuesto = list(map(lambda x: {"nombre": x["nombre"], "impuesto": x["impuesto"]}, impuesto))

print(nombre_impuesto)
print(impuesto)
