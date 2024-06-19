# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica (o desviación estandar)

n = input("Pon una muestra de números separados por comas: ") # El usuario pone una muestra de numeros

lista_num = [float(i) for i in n.split(',')]  # Se inicializa la lista de numeros lista_num con una lista de compresión que itera sobre los elementos de la variable n separados con una ','

media = sum(lista_num)/len(lista_num)         # Se calcula la media y se guarda en la variable med

desv_est = 0                                  # Se inicializa la variable desv_est a 0
for i in lista_num:                           # Se itera sobre la lista lista_num
  desv_est += (i - media)**2                  # Se suma cada valor de la lista lista_num menos la media al cuadrado a la variable desv_est
desv_est = (desv_est/len(lista_num))**0.5     # Se hace la raiz cuadrada de desv_est partido por el numero de elementos de la lista lista_num

print(f"Para {lista_num}, la media es {media:.02f} y la desviación típica es {desv_est:.02f}")   # Se imprime la lista lista_num, su media y su desviación típica con 2 decimales
