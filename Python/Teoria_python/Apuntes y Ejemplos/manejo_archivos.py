## MANEJO DE ARCHIVOS

# Con open hay que cerrar siempre con el método close()
# Con with open se cierra automáticamente al salir del bloque with

# Acceder a los archivos:
# open ('<<archivo>>','<<modo>>', encoding='<<coding>>')
# with open ('<<archivo>>','<<modo>>', encoding='<<coding>>') as <<nombre>>:
#     <<cuerpo_sintaxis>>

# Métodos:
#   write() -> escritura
#   read() -> lectura de todo el archivo
#   read(<<n>>) -> lectura de n caracteres
#   readline() -> lectura línea por línea
#   close() -> cierre

# Modos:
#   'w' -> escritura
#   'r' -> lectura
#   'a' -> añadir
#   'x' -> creación

## EJEMPLO 1 - Leer un archivo línea por línea

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

## EJEMPLO 4 - Crear un nuevo archivo y escribir en él

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 'w', encoding='UTF-8') as archivo:
    archivo.write("Línea 1\n")
    archivo.write("Línea 2\n")
    archivo.write("Línea 3\n")

print("Ejemplo 4: Archivo creado y líneas escritas")

## EJEMPLO 5 - Añadir nuevas líneas a un archivo existente

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 'a', encoding='UTF-8') as archivo:
    archivo.write("Línea 4\n")
    archivo.write("Línea 5\n")

print("Ejemplo 5: Nuevas líneas añadidas")

## EJEMPLO 6 - Leer todo el contenido de un archivo

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 'r', encoding='UTF-8') as archivo:
    contenido = archivo.read()

print(f"Ejemplo 6: Contenido del archivo:\n{contenido}")

## EJEMPLO 7 - Leer n caracteres de un archivo

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 'r', encoding='UTF-8') as archivo:
    contenido_parcial = archivo.read(10)  # Leer los primeros 10 caracteres

print(f"Ejemplo 7: Primeros 10 caracteres del archivo:\n{contenido_parcial}")

## EJEMPLO 8 - Eliminar una línea específica de un archivo

def eliminar_linea(nombre_archivo, numero_linea):
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        lineas = archivo.readlines()
    with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
        for i, linea in enumerate(lineas):
            if i != numero_linea:
                archivo.write(linea)

eliminar_linea('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 1)

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\nuevo_archivo.txt', 'r', encoding='UTF-8') as archivo:
    contenido = archivo.read()

print(f"Ejemplo 8: Contenido del archivo después de eliminar la línea 2:\n{contenido}")

## EJEMPLO 9 - Manejar archivos binarios

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\archivo_binario.bin', 'wb') as archivo:
    archivo.write(b'\x00\xFF\x00\xFF')

print("Ejemplo 9: Archivo binario creado")

with open('C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\archivo_binario.bin', 'rb') as archivo:
    contenido_binario = archivo.read()

print(f"Ejemplo 9: Contenido del archivo binario:\n{contenido_binario}")

