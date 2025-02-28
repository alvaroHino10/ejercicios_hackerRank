#Ejecicio de permutacion

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    mod = 1000000007

    # Paso 1: Calcular el número de formas de llenar una fila hasta el ancho de los bloques disponibles
    permutations = [0, 1, 2, 4, 8]

    for i in range(5, m + 1):
        # La forma de llenar una fila de ancho i es la suma de las formas para (i-1), (i-2), (i-3) y (i-4)
        dp_value = (permutations[i - 1] + permutations[i - 2] + permutations[i - 3] + permutations[i - 4]) % mod
        permutations.append(dp_value)

    # Paso 2: Calcular el total de muros sin restricción de grieta (para cada ancho)
    # Elevamos a la potencia n el número de formas de llenar una fila, ya que el muro tiene n filas
    # (seria como permutation[i] x permutations[i]....n veces).
    for i in range(1, m + 1):
        permutations[i] = pow(permutations[i], n, mod)

    # Paso 3: Eliminar las paredes que tienen grietas verticales, dejando solo las sólidas.
    # good_permutations[i] será el número de muros sólidos para un ancho i.
    # El caso base: para ancho 1, solo hay 1 muro y es sólido.
    good_permutations = [0, 1]

    # Calcular good_permutations para anchos de 2 hasta m
    for i in range(2, m + 1):
        bad = 0
        # Restamos las configuraciones que se pueden dividir en dos secciones a través de una grieta
        for j in range(1, i):
            # good_permutations[j] corresponde a la parte izquierda ya "sólida"
            # permutations[i-j] es el total (inestable o no) de la parte derecha
            bad += (good_permutations[j] * permutations[i - j]) % mod
        good_permutations_i = (permutations[i] - bad) % mod
        good_permutations.append(good_permutations_i % mod)

    return good_permutations[m]


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        print(result)
