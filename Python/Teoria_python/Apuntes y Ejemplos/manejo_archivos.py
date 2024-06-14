## MANEJO DE ARCHIVOS

# Con open hay que cerrar siempre con el método close()
# Con with open se cierra automáticamente al salir del bloque with

# Acceder a los archivos:
# open ('<<archivo>>','<<modo>>', encoding='<<coding>>')
# with open ('<<archivo>>','<<modo>>', encoding='<<coding>>') as <<nombre>>:
#     <<cuerpo_sintaxis>>

# Métodos:
#   write() -> escritura
#   readline() -> lectura línea por línea
#   read(<<n>>) -> lectura de n caracteres
#   read() -> lectura de todo el archivo
#   close() -> cierre

# Modos:
#   'r' -> lectura
#   'w' -> escritura
#   'a' -> añadir
#   'x' -> creación

## EJEMPLO 1 - Uso básico

archivo = open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\texto.txt', 'r', encoding='UTF-8')

for linea in archivo.readlines():  # Bucle para iterar por cada línea del archivo
    print(f"Ejemplo 1: {linea.strip()}")  # strip() para eliminar espacios en blanco al principio y final de cada línea

archivo.close()  # Cerrar el archivo

## EJEMPLO 2 - Ejemplo tradicional con open()

try:
    archivo = open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\texto.txt', 'r', encoding='UTF-8')
    contador = 0
    for linea in archivo.readlines():
        print(f"Ejemplo 2_try: {linea.strip()}")
        contador += 1
except FileNotFoundError:
    print("Ejemplo 2_except: No se encuentra el archivo")
finally:        # Siempre necesitamos un bloque finally para usar close()
    archivo.close()  # Si usamos open() siempre hay que usar close() para cerrar
    print(f"Ejemplo 2_finally: Archivo cerrado, con {contador} líneas")

## EJEMPLO 3 - Ejemplo básico con with open *** IMPORTANTE ***

try:
    with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\texto.txt', 'r', encoding='UTF-8') as archivo:
        for linea in archivo.readlines():
            print(f"Ejemplo 3_try: {linea.strip()}")
except FileNotFoundError:
    print("Ejemplo 3_except: No se encuentra el archivo")
