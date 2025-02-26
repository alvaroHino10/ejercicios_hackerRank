#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# Bubble sort con conteo de swaps, modificado del original, al final realiza la suma de los swaps y si alguno es mayor a
# 2 imprime "Too chaotic"
def minimumBribes(q):
    # Write your code here
    n = len(q)
    bribes = [0] * n
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if q[j] > q[j + 1]:
                bribes[q[j] - 1] += 1
                q[j], q[j + 1] = q[j + 1], q[j]
                swapped = True
        if not swapped:
            break
    max_swaps = max(bribes)
    if max_swaps > 2:
        print("Too chaotic")
    else:
        print(sum(bribes))

# Clasico orden de bubble sort, para el ejercicio solo se debe agregar el conteo del numero de swaps que hace cada
# elemento
def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
