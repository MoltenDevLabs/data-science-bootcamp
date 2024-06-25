import pandas as pd

datos_sensores = {
  "sensor_id": [1, 2, 3, 4, 5],
  "temperatura": [22, 27, 30, 24, 26],
  "humedad": [55, 65, 60, 58, 63],
  "presion": [1012, 1008, 1005, 1011, 1009]
}

df_sensores = pd.DataFrame(datos_sensores)

sensores_filtrados = df_sensores[
  (df_sensores["temperatura"]>25) & 
  (df_sensores["presion"]<1010)
  ].apply(lambda x: {"sensor_id": x["sensor_id"], "temperatura": x["temperatura"]}, axis=1)

df_sensores_filtrados = pd.DataFrame(list(sensores_filtrados))  # Si no se usa list() el resultado es un diccionario que es lo que devuelve el metodo apply()

print(df_sensores_filtrados)
