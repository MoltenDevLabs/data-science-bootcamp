ingresos = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]

clas = list(map(lambda x: "Bajo" if x<30000 else "Medio" if 30000<=x<=70000 else "Alto", ingresos))

print(clas)
