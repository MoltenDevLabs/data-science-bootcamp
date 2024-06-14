# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

f = input("Pon una frase: ")                                    # El usuario introduce una frase f
l = input("Pon una letra: ")                                    # El usuario introduce una letra l

c = 0                                                           # Se inicializa la variable c a 0
for i in f:                                                     # Se recorren las letras de la frase f
  if i.lower() == l:                                            # Se evalua si cada letra convertida a minúscula coincide con la letra l
    c += 1                                                      # Si coincide se suma 1 al contador

print(f"la letra '{l}' aparece {c} veces en la frase: '{f}'")   # Se imprime cuantas veces aparece la letra l en la frase f
