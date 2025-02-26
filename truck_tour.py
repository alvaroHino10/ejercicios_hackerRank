#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

# Se recorre la lista de estaciones de gasolina, se suman los valores de gasolina y distancia, si toda la gasolina menos
# la distancia total es menor a 0 iniciamos en el siguiente indice, el ejercicio es algo tramposo ya que se menciona un
# circulo y deja a pensar que se debe recorrer las demas gasolineras, pero en realidad solo se debe recorrer una vez y
# se puede iniciar en cualquier gasolinera.
def truckTour(petrolpumps):
    # Write your code here
    index_i = 0
    total_gas = 0
    total_distance = 0
    for petrol in petrolpumps:
        total_gas += petrol[0]
        total_distance += petrol[1]
        if total_gas - total_distance < 0:
            total_gas = 0
            total_distance = 0
            index_i = petrolpumps.index(petrol) + 1
    return index_i


if __name__ == '__main__':

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(result)
