# Ejercicio 125

import matplotlib.pyplot as plt

def notas_asig(notas, color):
  fig, ax = plt.subplots()
  ax.bar(notas.keys(),notas.values(), color = color)
  ax.set_xlabel('Asignatura')
  ax.set_ylabel('Nota')
  ax.set_title('Notas')
  plt.show()


dict_notas = {"matematicas": 4, "fisica": 5, "historia": 8, "lengua": 7}
color_ejemplo = "green"

notas_asig(dict_notas, "red")
