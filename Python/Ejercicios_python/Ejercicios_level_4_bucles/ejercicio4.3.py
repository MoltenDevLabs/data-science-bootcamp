# Escribir un programa que pida al usuario un número entero positivo y omuestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

n = int(float(input("Pon un numero entero positivo: "))) # El usuario introduce un numero

r= ""                                               # Se inicializa r como string vacio
for i in range(n+1):                                # Se recorre el rango de valores desde 0 hasta el numero introducido
  if i % 2 != 0:                                    # Si los numeros son impares entran
    r += str(i) + ","                               # Se añade el numero y una coma al string r

r=r[:-1]                                            # Se elminina el ultimo valor (una coma ",")

print(r)                                            # Se muestra el string r
