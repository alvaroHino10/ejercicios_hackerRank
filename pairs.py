#!/bin/python3
import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
# Metodo que comprueba a doble paso si existen pares si se encuentra se corta y reduce la complejidad, pero en el peor
# de los casos sigue siendo O(n^2)
def pairs(k, arr):
    # Write your code here
    arr.sort()
    count = 0
    limit = arr.index(k) - 1 if k in arr else 0

    for i in range(len(arr) - 1, limit, -1):
        for j in range(i - 1, -1, -1):
            value = arr[i] - k
            if arr[j] == value:
                count += 1
                break
            elif arr[j] < value:
                break
    return count

# Metodo eficiente (greedy) usando set, que reduce la complejidad a O(n), recorre una sola vez la lista
def pairs(k, arr):
    arr_set = set(arr)  # Convertimos la lista en un conjunto para búsqueda rápida
    count = 0
    for num in arr:
        if num - k in arr_set:
            count += 1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
