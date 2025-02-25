#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    row_diagonal_rl = len(arr) - 1
    sum_lr = 0
    sum_rl = 0
    for i in range(0, len(arr)):
        sum_lr += arr[i][i]
        sum_rl += arr[row_diagonal_rl - i][i]
    sum_abs = abs(sum_lr - sum_rl)
    return sum_abs


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)