#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    middle = len(matrix) // 2
    final_index = len(matrix) - 1
    max_total = 0
    for i in range(middle):
        for j in range(middle):
            max_val = max(
                matrix[i][j],
                matrix[i][final_index- j],
                matrix[final_index - i][j],
                matrix[final_index - i][final_index - j]
            )
            max_total += max_val
    return max_total

# Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
