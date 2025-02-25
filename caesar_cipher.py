#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# Metodo que no usa los valores relativos del alfabeto por tanto debe controlar los desbordamientos con condicionales
# para cada caso, es menos seguro que el método caesarCipher
def caesarCipher2(s, k):
    result = ''
    top = ord('Z')
    top_min = ord('z')
    k = k % 26
    for i in s:
        valueC = ord(i)
        if is_in_range_min(valueC):
            valueC = (valueC + k) if (valueC + k) <= top_min else (valueC + k) - 26
        elif is_in_range_cap(valueC):
            valueC = (valueC + k) if (valueC + k) <= top else (valueC + k) - 26
        result += chr(valueC)
    return result


def is_in_range_min(valueC):
    return valueC >= ord('a') and valueC <= ord('z')

def is_in_range_cap(valueC):
    return valueC >= ord('A') and valueC <= ord('Z')


# Metodo seguro, se usa el modulo 26 para evitar desbordamientos, se usa los valores relativos del alfabeto
# para hacer los desplazamientos y se convierte de vuelta a carácter
def caesarCipher(s, k):
    result = []
    for valueC in s:
        if valueC.islower():
            index = ord(valueC) - ord('a')  # Convertir a índice relativo
            new_index = (index + k) % 26  # Aplicar el desplazamiento
            new_char = chr(new_index + ord('a'))  # Convertir de vuelta a carácter
            result.append(new_char)

        elif valueC.isupper():
            index = ord(valueC) - ord('A')  # Convertir a índice relativo
            new_index = (index + k) % 26  # Aplicar el desplazamiento
            new_char = chr(new_index + ord('A'))  # Convertir de vuelta a carácter
            result.append(new_char)
        else:
            result.append(valueC)
    return ''.join(result)




if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher2(s, k)

    print(result)
