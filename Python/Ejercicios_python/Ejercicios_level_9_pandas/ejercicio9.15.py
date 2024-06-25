import pandas as pd

datos_productos = {
  "productos": ["A", "B", "C", "D", "E"],
  "precio": [150, 85, 120, 200, 75],
  "cantidad_vendida": [30, 50, 5, 20, 40]
}

df_productos =  pd.DataFrame(datos_productos)

df_filtrado = df_productos[lambda x: (x["precio"] >= df_productos["precio"].mean()) & (x["cantidad_vendida"] >= 50)]

print(df_filtrado)  # Ningún producto cumple las condiciones
