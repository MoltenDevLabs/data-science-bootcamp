import pandas as pd

datos_transacciones = {
  "cliente": ["Juan", "Ana", "Luis", "Ana", "Juan", "Luis", "Ana"],
  "monto": [150, 200, 100, 250, 300, 150, 100],
  "fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07"]
}

df_transacciones = pd.DataFrame(datos_transacciones)

df_final = df_transacciones.groupby(["cliente"]).agg( # El metodo agg() sirve para agregar los resultados en el grupo especificado en el metodo groupby()
  gasto_total = ("monto", lambda x: x.sum()),
  n_trans = ("monto", lambda x: x.count()),
  gasto_medio = ("monto", lambda x: x.mean())
)

print(df_final)
