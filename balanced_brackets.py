#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Metodos para simular una pila, se usa la funcion append para agregar un elemento al final de la pila y la funcion pop
# para eliminar el ultimo elemento de la pila. Se usa la funcion is_empty para verificar si la pila esta vacia y la
# funcion peek para obtener el ultimo elemento de la pila.
def pop(stack):
    return stack.pop()

def push(item, stack):
    stack.append(item)

def is_empty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[-1] if not is_empty(stack) else ''

# Clasico ejercicios para aplicarlo a una pila, para comparar cierres de parentesis, corchetes y llaves
def isBalanced(s):
    # Write your code here
    stack = list(s)
    aux_stack = []
    item = pop(stack)
    push(item, aux_stack)
    while not is_empty(stack):
        item = pop(stack)
        if item == '(' and peek(aux_stack) == ')':
            pop(aux_stack)
        elif item == '[' and peek(aux_stack) == ']':
            pop(aux_stack)
        elif item == '{' and peek(aux_stack) == '}':
            pop(aux_stack)
        else:
            push(item, aux_stack)

    return 'YES' if is_empty(aux_stack) else 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
