# Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por laa desviación típica de la muestra.

from statistics import mean, stdev

pp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1999]
pp2 = [1, 2, 2, 2, 2, 2, 9999, 2, 3, 3, 2, 1, 1, 2]

def atipicos(l):
  media = mean(l)
  desvs = stdev(l)

  def score(n): # Función clousure (obliga a aplicar la funcion a cada uno de los elementos)
    puntuacion = (n - media) / (desvs)
    return (puntuacion < -3) or (puntuacion > 3)
  
  return score

def resol(x):
  return list(filter(atipicos(x), x))

print(f"Valor atipico en la lista pp: {resol(pp)}")
print(f"Valor atipico en la lista pp2: {resol(pp2)}")
