import pandas as pd

datos_ventas = {
  "producto": ["A", "B", "C", "D"],
  "ventas_mensuales": [150, 200, 100, 250],
  "ventas_anuales": [1800, 2400, 1200, 3000]
}

df_ventas = pd.DataFrame(datos_ventas)

datos_normalizados = df_ventas[["ventas_mensuales", "ventas_anuales"]].apply(lambda x: (x-x.min())/(x.max()-x.min()))

print(datos_normalizados)
