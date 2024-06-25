celsius = [0, 10, 20, 30, 40]

farenheit = list(map(lambda x: x*1.8 + 32, celsius))

clas = list(map(lambda x: "Frío" if x < 50 else "Templado" if 50<=x<=80 else "Calor", farenheit))

print(farenheit)
print(clas)
