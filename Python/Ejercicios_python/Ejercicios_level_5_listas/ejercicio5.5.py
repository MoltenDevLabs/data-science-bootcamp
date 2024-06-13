# Escribir un programa que almacene en una lista los números de 1 al 10 y los muestre por pantalla en orden inverso separados por comas

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Se inicializa la lista n con valores del 1 al 10
ns = ''                             # Se inicializa la variable ns como string vacio

for i in n[::-1]:                   # Se itera sobre los elementos de la lista n al revés
  ns += str(i) + ','                # Para cada elemento se añade como string y una coma al string ns

print(ns[:-1])                      # Se imprime el string ns eliminando el último valor, que es una coma