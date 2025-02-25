#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_grid = []
    for row in grid:
        row = ''.join(sorted(row))
        sorted_grid.append(row)
    for i in range(len(sorted_grid[0])):
        for j in range(len(sorted_grid) - 1):
            first = sorted_grid[j][i]
            second = sorted_grid[j + 1][i]
            if first > second:
                return 'NO'
    return 'YES'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)

        print(result)
