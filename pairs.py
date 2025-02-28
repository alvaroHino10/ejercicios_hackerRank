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


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
