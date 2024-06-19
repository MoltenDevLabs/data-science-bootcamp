# Genera una lista de números perfectos menores a 10,000. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el propio número).

# Aqui esta hecho sin lista de comprensión
def calcular_divisores_largo(numero):
  lista_divisores = []
  for i in range(1, numero):
    if numero % i == 0:
      lista_divisores.append(i)
  return lista_divisores

def numero_perfecto_largo(numero):
  lista_perfectos = []
  divisores = calcular_divisores_largo(numero)
  suma_divisores = sum(divisores)
  if numero == suma_divisores:
    lista_perfectos.append(numero)
  return lista_perfectos

lista_perfectos_largo = []
for n in range(1, 10000):
  lista_perfectos_largo += numero_perfecto_largo(n)

print(f"Solución sin lista de comprensión: {lista_perfectos_largo}")

# Aqui esta hecho con lista de comprensión

def calcular_divisores(numero):
  return [i for i in range(1, numero) if numero % i == 0] # Retorna una lista de divisores propios del número dado, incluyendo todos los números en el rango de 1 a (numero - 1) que son divisibles exactamente por el número dado como parámetro.

def numero_perfecto(numero):
  divisores = calcular_divisores(numero)  # Se guarda el retorno de la funcion 'calcular_divisores()' en la variable 'divisores'
  suma_divisores = sum(divisores) # Se guarda la suma de los divisores en la variable 'suma_divisores'
  return numero if numero == suma_divisores else None # Devuelve un numero o nada, no hay que poner corchetes ya que lo hacemos devolvera listas

lista_perfectos = [numero_perfecto(n) for n in range(1, 10000) if numero_perfecto(n) is not None] # Añade cada numero en el rango si el retorno de la funcion 'numero_perfecto()' algo que no sea 'None'

print(f"Solución con lista de comprensión: {lista_perfectos}")
