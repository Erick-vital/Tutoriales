# ALGORITMO DE INSERCION

""" Imagina que de una baraja de carta desordenada te van dando una
    por una y tu cada carta que te dan la ordenas segun su valor
"""

numeros = [4, 3, 1, 2, 5]

for i in range(1, len(numeros)):
    current = numeros[i]

    while numeros[i-1] > current and i>0:
        numeros[i] = numeros[i-1]
        numeros[i-1] = current
        # Con esto hacemos que se recorra asia atras la busqueda
        i = i-1

print(numeros)

