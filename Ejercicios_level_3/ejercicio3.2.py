# Escribir una función que simule una calculdora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla xon los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

#from math import sin, cos, tan, exp, log
import math

def aplicacion(f="seno", n=90):
  """
  USO: Aplica una funcion a un numero
  PARAMETROS:
    f[str]: funcion a aplicar
    n[int]: numero a evaluar final de la serie
  VARIABLES:
    funciones[dict]: recupera la instrucción de math en funcion de f
    resultado[dict]: almacena la aplicación de la función matematica al rango de valores desde 1 hasta n
  RETURN:
    pd[float]: el valor evaluacion de la funcion al numero
  """
  funciones = {'seno':math.sin, 'coseno':math.cos, 'tangente':math.tan, 'exponencial':math.exp, 'logaritmo':math.log}
  resultado = {}
  for i in range(1, n+1):
    resultado[i] = funciones[f](i*math.pi/180)
  return resultado

def calculadora():
  """
  USO: 
  FUNCIONES:
    aplicacion[fun]: aplica una funcion a un numero
  VARIABLES:
    f[str]: funcion a aplicar
    n[int]: numero a evaluar
    tx[str]: cadena que proporciona valor y evaluacion de la funcion
  RETURN:
    []: 
  """
  print(f"Funciones disponibles: seno, coseno, tangente, exponencial, logaritmo")
  tx, f, n = "", input("Funcion: "), int(float(input("Numero: ")))

  for i, j in aplicacion(f, n).items():
    tx +=f"{i}\t{j:.3f}\n"
  return tx

r = calculadora()

print(r)