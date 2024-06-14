# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido desde 1 hasta su edad

e = int(input("Edad: "))          # El usuario intoduce su edad como entero

for i in range(1,e+1):            # Se recorren los numeros de 1 hasta el número introducido
  print(f"Has cumplido {i} años") # Se imprimen los numeros de 1 hasta el número introducido
