# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica (o desviación estandar)

n = input("Pon una muestra de números separados por comas: ")                     # El usuario pone una muestra de numeros

ln = [float(i) for i in n.split(',')]                                             # Se inicializa la lista de numeros ln con una lista de compresión que itera sobre los elementos de la variable n separados con una ','

med = sum(ln)/len(ln)                                                             # Se calcula la media y se guarda en la variable med

dt = 0                                                                            # Se inicializa la variable dt a 0
for i in ln:                                                                      # Se itera sobre la lista ln
  dt += (i - med)**2                                                              # Se suma cada valor de la lista ln menos la media al cuadrado a la variable dt
dt = (dt/len(ln))**0.5                                                            # Se hace la raiz cuadrada de dt partido por el numero de elementos de la lista ln

print(f"Para {ln}, la media es {med:.02f} y la desviación típica es {dt:.02f}")   # Se imprime la lista ln, su media y su desviación típica con 2 decimales
