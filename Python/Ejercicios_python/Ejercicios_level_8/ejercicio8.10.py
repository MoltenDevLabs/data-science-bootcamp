# Genera una lista con los primeros 100 números de Fibonacci y luego filtra los números que son primos. Usa lista de comprensión.

# Solución sin lista de comprensión
def fib_nums(num):
  list = []
  i,j = 0, 1

  for n in range(num):
    list.append(i)
    i, j = j, i+j

  return list

fib_list = fib_nums(100)

def es_primo(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

fib_prime_list = []

for num in fib_list:
  if es_primo(num) == True:
    fib_prime_list.append(num)

print(fib_prime_list)

# Solución con lista de comprensión
