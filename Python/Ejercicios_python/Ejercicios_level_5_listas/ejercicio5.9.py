# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal

p = input("Pon una palabra: ")            # El usuario pone una palabra p

a = ['a', 'e', 'i', 'o', 'u']             # Se inicializa la lista a con las vocales
c = [0, 0, 0, 0, 0]                       # Se inicializa la lista c con cinco contadores a 0

for i in p:                               # Se itera por las letras de la palabra p
  if i.lower() == a[0]:                   # Si la letra es 'a'
    c[0] += 1                             # Se suma 1 a la primera posicion de la lista contador c
  elif i.lower() == a[1]:                 # Si la letra es 'e'
    c[1] += 1                             # Se suma 1 a la segunda posicion de la lista contador c
  elif i.lower() == a[2]:                 # Si la letra es 'i'
    c[2] += 1                             # Se suma 1 a la tercera posicion de la lista contador c
  elif i.lower() == a[3]:                 # Si la letra es 'o'
    c[3] += 1                             # Se suma 1 a la cuarta posicion de la lista contador c
  elif i.lower() == a[4]:                 # Si la letra es 'u'
    c[4] += 1                             # Se suma 1 a la quinta posicion de la lista contador c

for i in range(len(a)):                   # Se itera por los indices de la lista a
  print(f"{a[i]} aparece {c[i]} veces")   # Se imprime cuantas veces aparecen las vocales