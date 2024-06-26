### NUMPY

# pip install numpy
import numpy as np

# Objeto array

# 1D array
m1 = [1,2,3,4]  # m = 1, n = 4

M1 = np.array(m1)
M1

# 2D array (imagen monocromatica)
m2 = [[1,2,3], [4,5,6]] # m = 2, n = 3
M2 = np.array(m2)
M2

# 3D array
m3 = [ [ [0,1], [1, 2] ], [ [2, 3], [3, 4] ], [ [5, 6], [6, 7] ] ] # m = 3, n = 2, e = 4
M3 = np.array(m3)
M3.shape

# Array imaginario
np.array([[1,2],[2,3]], dtype=complex)

# Matriz cero: Sirve para crear una matriz vacia
matriz_cero = np.zeros([3,2])
f"Matriz cero: {matriz_cero}"

# Matriz vacia: igual que la matriz cero
matriz_vacia = np.empty((3,2))
f"Matriz vacia: {matriz_vacia}"

# Matriz unos
matriz_unos = np.ones((3,3))
f"Matriz unos: {matriz_unos}"

# Matriz identidad: matriz que en la diagonal principal hay 1 y el resto son 0
matriz_identidad = np.identity(3)
f"Matriz identidad: {matriz_identidad}"

# Matrices de dimension m x n de un valor
matriz_llena = np.full((3,2), 10)
f"Matriz llena: {matriz_llena}"

# Matriz de datos aleatorios
matriz_aleatoria = np.random.random((3,2))
f"Matriz aleatoria: {matriz_aleatoria}"

# Array entre y hasta con salto
""" arrange = np.arrange(1,9,1)
f"Array arrange: {arrange}") """

# Genera un array 5 elementos del 0 al 10 con espacios equidistantes
linspace = np.linspace(0,10,5)
f"Array linspace: {linspace}"

### Atributos array

# Dimensiones m x n: devuelve una tupla con las dimensiones
M2.shape

# Numero de dimensiones (len(<<matrix>>))
M2.ndim

# Numero de elementos de una matriz (n*m)
M2.size

# Tipo
M2.dtype

### Acceder a los elementos de un array

a = np.array([[1, 2, 3], [4, 5, 6]])

m,n = 1,0 # Fila 1, columna 2
a[m][n] # En este caso fila 1, columna 2 corresponde al 4

a[:, 0:2] # En este caso saca una submatriz [[1,2], [4, 5]]

# Acceder con una condicion simple
a[a % 2 == 0] # Devuelve un array con los multiplos de 2. array([2, 4, 6])

# Condicion compleja
a[(a % 2 == 0) & (a > 2)]  # Devuelve  un array con los multiplos de 2 y mayores que 2. array([4, 6])

## Opciones con array

a, b = np.array([[1, 2, 3], [4, 5, 6]]), np.array([[2, 2, 2], [3, 3, 3]])

#suma
a+b

#resta
a-b

#division
a/b

#potenciación de elementos
a ** 2

# Producto escalar de vectores
a, b = np.array([1, 2, 3]), np.array([2, 2, 2])

a.dot(b)
a@b
np.inner(a,b)

# Producto cruzado
np.cross(a,b)

# Producto combinado
np.outer(a,b)

# Modulo de un vector
np.linalg.norm(a)

# Producto matricial (para poderse hacer tienen que ser dimensionalmente compatibles)
a, b = np.array([[1, 2], [4, 5]]), np.array([2, 2])

a.dot(b)
a@b

# Matriz traspuesta
a.T

# Traza de la matriz
a.trace()

# Determinante de la matriz
np.linalg.det(a)

# Inversa de una matriz
np.linalg.inv(a)

# Autovalores
np.linalg.eigvals(a)

# Autovectores
np.linalg.eig(a)

# Solventar sistema de ecuaciones
c, d = np.array([[1,2], [3,5]]), np.array([1,2])
np.linalg.solve(c,d)

# Suma de los elementos de un array 
# axis=1 para sumar por filas
# axis=0 para sumar por columnas
a, b = np.array([[1,2], [4,5]]), np.array([[2,2], [3,3]])
a.sum()
a.cumsum(axis=1) # suma acumulada por filas
b.sum(axis=1) # 1 por filas, 0 por columnas

# Productorio de un array
a.prod()

### Aplicacion de funciones trigonometreicas a los array
a = np.linspace(0, 2*np.pi, 50) # Da 50 valores equidistantes en toda la circunferencia

# Seno de los elementos del array
np.sin(a)

### Estadistica sobre array

# Media
np.mean(a) # La media del array
np.mean(axis=0) # La media de la fila (axis=1) o de la columna (axis=0)

# Mediana
np.median(a)

# Desviación tipica
np.std(a)

# Covarianza de un vector
np.cov(a)

# Covarianza de dos vectores
np.cov(a,b)

# Histogramas
v = np.random.normal(2,0.5,10000)

n, bins = np.histogram(v, bins = 50, density = True)

import matplotlib.pyplot as plt


