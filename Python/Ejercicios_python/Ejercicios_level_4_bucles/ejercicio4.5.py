# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obreniudo en la inversión cada año que dura la inversión

cantidad = float(input("Cantidad a invertir: ")) # El usuario introduce la cantidad a invertir
interes = float(input("Interés anual: "))        # El usuario introduce el interes anual
años = int(float(input("Numero de años: ")))     # El usuario introduce el numero de años

for i in range(1, años+1):                       # Se recorre el rango de numeros desde 1 hasta los años introducidos por el usuario
  cantidad += (cantidad*interes)/100             # Se modifica la cantidad, según en interés para cada año
  print(f"Año {i}: {cantidad:.2f}")              # Se imprime la cantidad de cada año
