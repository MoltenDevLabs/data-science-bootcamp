import pandas as pd

datos_acciones = {
  "fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
  "cierre": [150, 155, 153, 160],
  "volumen": [1000, 1100, 1050, 1150]
}

df_acciones = pd.DataFrame(datos_acciones)

df_acciones["dif"] = df_acciones["cierre"].diff() # El metodo diff() calcula la diferencia de una posicion y con la anterior en la fila seleccionada

df_acciones = df_acciones[["fecha", "cierre", "dif"]]

print(df_acciones)
