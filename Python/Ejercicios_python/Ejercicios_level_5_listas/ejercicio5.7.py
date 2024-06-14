# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

b = []                    # Se inicializa la variable b como lista vacia
for i in range(len(a)):   # Se itera por los indices de la lista a
  if (i + 1) % 3 != 0:    # Se filtran los valores de los indices que no son divisibles por 3 (se usa i+1 para que los indices empiezen en 1 y no en 0)
    b.append(a[i])        # Los indices que no son divisibles por 3 se añaden a la lista b

print(b)                  # Se imprime la lista b
