# Ejercicio 126

import matplotlib.pyplot as plt
import pandas as pd

calificaciones = [7,4,3,6,7,2,1,6]
notas = pd.Series(calificaciones)

def notas_plot(notas):
  fig, ax = plt.subplots()
  ax.boxplot(notas)
  ax.set_xlabel('Asignatura')
  ax.set_ylabel('Nota')
  ax.set_title('Distribución de notas')
  plt.show()

notas_plot(notas)
