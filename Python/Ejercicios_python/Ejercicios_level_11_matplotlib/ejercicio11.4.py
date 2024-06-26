# Ejercicio 127

import matplotlib.pyplot as plt
import pandas as pd

numero_ventas = [3,5,7]
serie_ventas = pd.Series(numero_ventas)
trimestre = ["mes1", "mes2", "mes3"]
nombre_grafico = "Gráfico ventas trimestre"

def ventas_plot(serie, meses, titulo):
  fig, ax = plt.subplots()
  ax.pie(serie, labels=meses)
  ax.set_title(titulo)
  plt.savefig(f"{titulo}.png")  # El metodo savefig() guarda el gráfico coon el titulo dado en el formato dado
  plt.show()

ventas_plot(serie_ventas, trimestre, nombre_grafico)
