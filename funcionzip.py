# Explicación función zip()

matematicas, lengua, personas = [3, 8, 3, 9, 0], [8, 5, 3, 7, 5], ['pol', 'merchu', 'roc', 'lluna', 'guiu']

for i, j, k in zip(personas, matematicas, lengua):
  print(i, j, k)
  