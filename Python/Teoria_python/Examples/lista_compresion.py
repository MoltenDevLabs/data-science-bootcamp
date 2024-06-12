# Encontrar una lista extensional de las diez primeras potencias de 2

def potenciometro(n=10):
  potencias_de_2 = []
  c=1
  while c <= n:
    x = 2**c
    potencias_de_2.append(x)
    c+=1
  
  return(potencias_de_2)

n = 10
print(f"las {n} primeras potencias de 2 son: ", potenciometro(n))

# Solucion del profe
a2 = []
for k in range(10):
  a2.append(k**2)

print(a2)

# Encontrar una lista intensional o de compresion de las diez primeras potencias de 2

a2 = [2**k for k in range(10)]
print(a2)

# Tambien se puede hacer las listas de compresion con condiciones (simple: condicion if)

a2 = [2**k for k in range(10) if k%4 == 0]
print(a2)

# Incluso se puede hacer con else (multiple: condicion if - else)

a2 = [2**k if k%4 == 0 else 3**k in range(10)]
print(a2)