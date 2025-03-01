#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappush, heappop
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

# La idea inicial era ordenar la lista y luego ir sumando los dos primeros elementos de la lista, pero resulta
# ineficiente para listas muy grandes ya que se vuelve costoso ordenar la lista en cada iteración. Se penso en set pero
# debido a que existen elementos repetidos no es posible usarlo.
# Se opto por usar un heap (cola de prioridad) que es una estructura de datos que permite mantener los elementos
# ordenados y que es eficiente para agregar y eliminar elementos.
def cookies(k, a):
    # Write your code here
    count = 0
    heapify(a)
    while len(a) > 1 and a[0] < k:
        first = heappop(a)
        second = heappop(a)
        new_cookie = first + 2 * second
        heappush(a, new_cookie)
        count += 1
    return count if a[0] >= k else -1

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = cookies(k, a)

    print(result)
