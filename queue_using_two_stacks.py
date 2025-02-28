from sys import stdout, stdin
from collections import deque

deque = deque()

# Se usa la estructura de datos deque para simular una cola, se usa la funcion popleft para eliminar el primer elemento
# de la cola y la funcion append para agregar un elemento al final de la cola. Segun los datos de entrada se decide si
# insertar, eliminar o imprimir el primer elemento de la cola.
def input_data():
    q = int(input())
    for _ in range(q):
        operation= list(map(int, stdin.readline().strip().split(' ')))
        if operation[0] == 1:
            enqueue(operation[1])
        elif operation[0] == 2:
            dequeue()
        else:
            print_data()

def enqueue(number):
    deque.append(number)

def dequeue():
    deque.popleft()

def print_data():
    stdout.write(str(deque[0]) + '\n')

if __name__ == '__main__':
    input_data()