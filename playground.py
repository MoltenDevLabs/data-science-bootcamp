# EJEMPLO ESCRIBIR DATOS
# si no existe el archivo "sucio.txt" lo va a crear de nuevo

l = [1,2,3,4,5]

with open ("sucio.txt", 'w', encoding='utf-8') as f:
  for k in l:
    f.write(f"He escrito el valor {k} de la lista {l}\n")