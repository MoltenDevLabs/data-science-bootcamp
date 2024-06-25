import pandas as pd

datos_rendimiento = {
  "nombre": ["Pedro", "Maria", "Luis", "Ana"],
  "proyectos_completados": [5, 7, 3, 8],
  "horas_trabajadas": [40, 35, 50, 30],
  "satisfaccion": [80, 90, 70, 85]
}

df_rendimiento = pd.DataFrame(datos_rendimiento)

df_rendimiento["metrica"] = df_rendimiento[["proyectos_completados", "horas_trabajadas", "satisfaccion"]].apply(
  lambda x: (x["proyectos_completados"]*0.5) + (x["horas_trabajadas"]*0.3)+(x["satisfaccion"]*0.2), axis=1)

print(df_rendimiento)
