# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

internet_file = "https://ec.europa.eu/eurostat/documents/15234730/17582411/KS-HA-23-001-EN-N.pdf/5d783d9e-9cb3-897c-8360-5122563ae8f3?version=6.0&t=1700579783008"

def internet_file_word_counter(file):
  c = 0
  try:
    with open(file, 'r', encoding='utf-8') as f:
      words = f.readlines().split(" ")
      for i in words:
        c += 1
    return c
  except Exception as e:
    print(f"Error: {e}")

count = internet_file_word_counter(internet_file)
print(count)