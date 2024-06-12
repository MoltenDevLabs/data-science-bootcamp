# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es

correo = input("Cuál es tu correo? ") # Entrada de datos

x = correo.split('@')                 # Separacion antes y después de la @
correo_ceu = x[0] + '@ceu.es'         # Poner '@ceu.es'

print(correo_ceu)                     # Impresión por pantalla