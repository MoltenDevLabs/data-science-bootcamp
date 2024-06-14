# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario deve mostrar un mensaje informando de ello

g = {'plàtano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.7}  # Se inicializa el diccionario g

f = input("Pon una fruta: ")                                          # El usuario pone una fruta

if f.lower() in g:                                                    # Si la fruta que pone el usuario esta en el diccionario g
  n = float(input("Cuantos kilos? "))                                 # El usuario pone cuantos kilos en la variable n
  t = n*g[f]                                                          # Se calcula el total t
  print(f"{n} kilos de {f} valen {t:.2f}")                            # Se imprime la fruta, los kilos y cuanto vale en total con 2 decimales
else:                                                                 # Si la fruta que pone el usuario NO esta en el diccionario g
  print(f"No hay {f}")                                                # Se imprime que no hay de esa fruta
