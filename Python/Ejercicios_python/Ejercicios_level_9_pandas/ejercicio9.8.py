import pandas as pd

datos = {
  "nombre": ["Carlos", "Lucía", "Marcos", "Ana"],
  "matematicas" : [90, 85, 78, 92],
  "ciencias": [88, 90, 80, 85],
  "ingles": [85, 88, 90, 86]
}

df = pd.DataFrame(datos)

df["promedio"] = df[["matematicas", "ciencias", "ingles"]].apply(lambda x: x.mean(), axis=1) # axis=1 indica que se aplica por filas del dataframe

print(df)
