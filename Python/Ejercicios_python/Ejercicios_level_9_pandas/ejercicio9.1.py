# Dada una lista de edades, utiliza una función lambda para filtrar las edades qwue sean mayores o iguales a 18 años (es decir, filtrar adultos)

edades = [4, 84, 52, 20, 12, 74, 1]

edades_filtradas = list(filter(lambda x: x >= 18, edades))

print(edades_filtradas)
