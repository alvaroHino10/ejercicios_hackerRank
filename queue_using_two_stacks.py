from sys import stdout, stdin
from collections import deque

deque = deque()

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