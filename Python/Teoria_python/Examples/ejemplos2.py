# Escribir dos funciones que permitan calcular:
  # La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
  # La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

def aSegundos(h,m,s):
  horas = h*3600
  minutos = m*60

  return f"{horas+minutos+s} segundos"

print(aSegundos(1,10,30))

def aHorasMinutosYSegundos(s):
  horas = int(s/3600)
  minutos = int(s%3600 / 60)
  segundos = s%60

  resultado = f"{horas} horas, {minutos} minutos, {segundos} segundos"

  return resultado

print(aHorasMinutosYSegundos(3668))

# Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:
  # Si recibe un argumento, supone que son segundos y convierte a horas, mintos y segundos.
  # Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

def aSegOHor(*t):
  if len(t) == 1:
    return aHorasMinutosYSegundos(t[0])
  elif len(t) == 3:
    return aSegundos(t[0], t[1], t[2])
  else:
    return "1 o 3 argumentos"
  
print(aSegOHor(30, 30, 30))
