#numeros perfectos

def numeros_perfectos(numero):
    es_perfecto = False
    divisores = []
    for n in range(1,numero):
        if numero % n == 0:
            divisores.append(n)
    return divisores

print(numeros_perfectos(6))