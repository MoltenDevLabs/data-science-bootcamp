import pandas as pd

datos_ventas = {
  "producto": ["A", "B", "A", "C", "B", "A", "C"],
  "cantidad": [10, 5, 20, 15, 10, 5, 10],
  "precio": [100, 200, 100, 150, 200, 100, 150]
}

df_ventas = pd.DataFrame(datos_ventas)

df_ventas_gr = df_ventas.groupby(["producto"]).apply(lambda x: (x["cantidad"]*x["precio"]).sum())

print(df_ventas_gr)
