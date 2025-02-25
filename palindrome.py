# !/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Metodo lento, revisa toda la cadena cuando no es necesario tanto costo, ya que a medida que se va recorriendo se puede controlar que ya sean indicios de palindromo comparando los caracteres, eso lo logramos con la condicion y cambiando los slice de check y check_fin, la version eficiente de este metodo esta debajo y similar a palindrome2()
def palindromeLento(s):
    final = len(s)
    if is_palindrome(s):
        return -1
    for i in range(len(s) // 2):
        check = s[:i] + s[i + 1:]
        check_fin = s[:final - i - 1] + s[final - i:]
        if is_palindrome(check):
            return i
        elif is_palindrome(check_fin):
            return final - i - 1
    return -1

# Mejorado y aprobado en hackerRank, se agrego la condicion de comparacion de cada letra inicial y si no fuera el caso, se revisa si es palindromo sin la letra inicial o sin la letra final pero solo los elementos del medio ya que los extremos ya fueron revisados a medida que avanza el for.
def palindrome(s):
    final = len(s)
    if is_palindrome(s):
        return -1
    for i in range(len(s) // 2):
        if s[i] != s[final - i - 1]:
            check = s[i + 1: final - i]
            check_fin = s[i:final - i - 1]
            if is_palindrome(check):
                return i
            elif is_palindrome(check_fin):
                return final - i - 1
            else:
                return -1

def is_palindrome(s):
    return s == s[::-1]

# Metodo que revisa solo los extremos y cuando encuentra una diferencia, compara los caracteres intermedios para comprobar si es palindromo, inspirado en el de internet pero mas legible y entendible.
def palindrome2(s):
    length = len(s)
    if is_palindrome(s):
        return -1
    for i in range(length//2):
        if s[i] != s[length-i - 1]:
            if is_palindrome(s[i + 1:length - i]):
                return i
            elif is_palindrome(s[i:length - i - 1]):
                return length-1-i
            else:
                return -1


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindrome2(s)

        print(result)
