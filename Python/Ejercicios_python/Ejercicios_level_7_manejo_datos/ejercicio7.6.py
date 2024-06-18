# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe incorporar funciones para crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado  en el fichero de texto <listin.txt> donde el nombre del cliente y su teléfono deven aparecer separados por comas y cada cliente en una línea distinta.

import os as so

def recuperarTelefono(f,c): # Función para consultar telefonos del listin
    """
    USO: devuelve el telefono del cliente en el fichero
    PARAMETROS:
        f[str]: fichero de telefono - cliente
        c[str]: nombre del cliente
    VARIABLES:
        c[list]:  lectura de las fichero nombre - tfno
        x[str]:   diccionario nom -tfno / advertencia no exista el nombre 
    RETURN:
        x[str]:   diccionario nom -tfno / advertencia no exista el nombre 
    """
    try:
        with open(f,'r',encoding='utf8') as F:      # Abre el archivo f pasado como parametro en modo lectura ('r') y lo guarda en la variable 'F'
            c = F.readlines()                       # Lee las lineas de 'F' y lo guarda en la variable 'c'
    except FileNotFoundError:                       # Gestión del error si no se encuentra el archivo 'f'
        x = "Archivo no encontrado"
    else:
        x = dict([tuple(k.split(",")) for k in c])  # Crea un diccionario con el nombre como clave y el telefono como valor
    return x
def anadirTelefono(f,nc,tc):    # Función para añadir una entrada al listin
    """
    USO: Añade el telefono del cliente en el fichero 
    PARAMETROS:
        f[str]: fichero de telefono - cliente
        nc[str]: nombre del cliente
        tc[str]: telefono del cliente
    VARIABLES:
        F[doc]:  lectura de las fichero 
        x[str]:   diccionario nom -tfno / advertencia no exista el nombre 
    RETURN:
        y[str]: nombre cliente y su telefono para escribir con formato
        x[str]:   advertencia no exista el nombre / advertencia de escritura
    """
    try:
        F = open(f,'a',encoding='utf8') # Se abre el listin en modo add ('a')
    except FileNotFoundError:
        x = "Archivo no encontrado"
    else:
        y = f"{nc},{tc}"    # Se crea el formato 'nombre,telefono' y se guarda en 'y'
        F.write(y)          # Se escribe 'y' en el listin
        x = f"Se ha añadido el {nc} con el telefono {tc} a {f}"
        F.close()           # Al usar la funcion open en vez de with open hay que cerrar al final
    return x
def eliminarTelefono(f,nc): # Función para eliminar una entrada del listin
    """
    USO: Elimina el telefono del cliente del fichero 
    PARAMETROS:
        f[str]: fichero de telefono - cliente
        nc[str]: nombre del cliente
    VARIABLES:
        F[doc]:  lectura de las fichero
        p[list / dict]:  lineas de la lectura del archivo por cada indice del list 
                         que muta a un diccionario cuya clave es el nombre tras list anterior
        x[str]:   advertencia no exista el nombre / advertencia de eliminacion de persona sobre el fichero
    RETURN:
        y[str]:   nombre cliente y su telefono para escribir con formato sobre el diccionario
        x[str]:   advertencia no exista el nombre / advertencia de escritura
    """
    try:
        F = open(f,'r',encoding='utf8') # Se abre en modo ('r')
    except FileNotFoundError:
        x = "Archivo no encontrado"
    else:
        p = F.readlines()   # Se leen las lineas y de guarda en 'p'
        F.close()
        p = dict([tuple(k.split(",")) for k in p])  # La variable 'p' muta a un diccionario cuya clave es el nombre
        if nc in p:                         # Si encuentra el nombre en las lineas del archivo ('p')
            del p[nc]                       # Se usa la keyword 'del' para borrar el diccionario 'p' en la posicion del nombre introducido
            F = open(f,'w',encoding='utf8')
            for i,j in p.items():
                y = f"{i},{j}"
                F.write(y)
            x = f"Se ha eliminado el cliente {nc} del fichero {f}"
            F.close()
        else:
            x = f"El cliente {nc} no existe en el fichero {f}"
    return x
def borrarArchivo(f):   # Función para borrar el listin o crear uno nuevo
    """
    USO: Elimina el fichero 
    PARAMETROS:
        f[str]: fichero de telefono - cliente
    VARIABLES:
        r[str]:  confirmacion de borrado
        p[list / dict]:  lineas de la lectura del archivo por cada indice del list 
                         que muta a un diccionario cuya clave es el nombre tras list anterior
        x[str]:   advertencia de borrado / advertencia de no borrado
    RETURN:
        x[str]:   advertencia de borrado / advertencia de no borrado
    """
    if so.path.isfile(f):   # Devuelve True si el archivo existe o False si no existe
        r = input("¿Borramos el archivo? (S-N):").upper().strip()
        if r == "S":
            try:
                so.remove(f)    # Se usa la función .remove() de la libreria os sobre el archivo 'f'
                x = "Fichero borrado"
            except FileExistsError:
                x = "No existe el fichero o la uri es invalida"
            except PermissionError:
                x = "No tienes privilegios para borrar el fichero"
            except Exception as error:
                x = f"Se ha producido un error desconocido.\nSe ha producido el error: {error}"
        else:
            x = "No se ha borrado el archivo"
    else:   # Si el archivo no existe entra aqui
        h = input("El archivo no existe\n Quieres crear un fichero? (S-N)").upper()
        if h == "S":
            with open(f, 'w') as F:
                c = F.write('')
            x = "Fichero creado"
        else:
            x = "No se ha creado el fichero"
    return x
def menu(f):    # Función principal que dirigira el flujo a uno o otra función dependiendo de la elección del usuario
    qh = input("¿Que quieres hacer?: ")
    if qh == "1":
        op = input("Nombre a consultar: ").strip()
        y = recuperarTelefono(f,op)
    elif qh == "2":
        op = input("añadir Nombre-Telefono: ").strip()
        n , t = op.split("-")[0], op.split("-")[1]
        y = anadirTelefono(f,n,t)
    elif qh == "3":
        op = input("Nombre a eliminar: ").strip()
        y = eliminarTelefono(f,op)
    elif qh == "4":
        y = borrarArchivo(f)
    else:
        y = "Bye bye" 
    return y

print("""
1: Mirar telefono
2: Añadir telefono
3: Eliminar telefono
4: Crear fichero
5: Terminar
""")

F = "C:\\Users\\polka\\OneDrive\\Escritorio\\data-science-bootcamp\\Python\\Ejercicios_python\\Ejercicios_level_7_manejo_datos\\salidas\\listin.txt"
print(menu(F))