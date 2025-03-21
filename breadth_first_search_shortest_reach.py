#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Dict, List, Tuple


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s

# Representacion de un grafo con listas de adyacencia, representado en un diccionario donde la clave es el vertice y el
# valor es una lista de tuplas donde el primer elemento es el vertice adyacente y el segundo elemento es el peso de la
# arista.
class Graph:
    def __init__(self):
        self.ady: Dict[int, List[Tuple[int, int]]] = {}

    def add_vert(self, vertice):
        if vertice not in self.ady:
            self.ady[vertice] = []

    def add_edge(self, vertice1: int, vertice2: int, peso: int):
        if vertice1 not in self.ady:
            self.add_vert(vertice1)
        if vertice2 not in self.ady:
            self.add_vert(vertice2)

        self.ady[vertice1].append((vertice2, peso))
        self.ady[vertice2].append((vertice1, peso)) 

    def show_graph(self):
        for vertice in self.ady:
            print(f"{vertice} -> {self.ady[vertice]}")

# Funcion extra que crea un grafo a partir de una lista de aristas, donde n es el numero de vertices y edges la lista de
# aristas.
def create_graph(n, edges):
    graph = Graph()
    for i in range(n):
        graph.add_vert(i)
    for edge in edges:
        graph.add_edge(edge[0], edge[1], 6)
    return graph

# Funcion bfs para el grafo que recorre en anchura y calcula la distancia de cada vertice al vertice de inicio s.
def bfs(n, m, edges, s) -> List[int]:
    graph: Graph = create_graph(n, edges)
    visited = [False] * n
    distances = [-1] * n
    distances[s - 1] = 0
    queue = [s]
    visited[s - 1] = True
    while queue:
        current = queue.pop(0)
        for neighbor, weigth in graph.ady[current]:
            if not visited[neighbor - 1]:
                distances[neighbor - 1] = distances[current - 1] + weigth
                queue.append(neighbor)
                visited[neighbor - 1] = True
    return [x for x in distances if x != 0]

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        sys.stdout.write(' '.join(map(str, result)))
        sys.stdout.write('\n')

