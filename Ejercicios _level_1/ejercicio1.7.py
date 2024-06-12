# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase "Tu indice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeando con dos decimales

peso = float(input("Introduce tu peso: "))
estatura = float(input("Introduce tu estatura: "))

imc = round((peso / estatura**2), 2)

print(f"Tu indice de masa corporal es {imc}")