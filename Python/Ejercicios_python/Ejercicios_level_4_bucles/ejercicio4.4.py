# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

n = int(float(input("Pon un número: "))) # El usuario intoduce un entero n

r = ''                              # Se inicializa el string r
for i in range(n, -1, -1):          # Se recorre el rango desde n hasta 0 en orden decreciente
  r += str(i) + ','                 # Se añade el número recorrido y una coma al string r

r = r[:-1]                          # Se eleimina la última coma al string r

print(r)                            # Se muestra el string r
