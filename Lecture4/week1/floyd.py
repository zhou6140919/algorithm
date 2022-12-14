'''
APSP reduces to n invocations of SSSP.
- non-negative edge lengths: O(mnlogn) via Dijkstra
- general edge lengths: O(mn^2) via Bellman-Ford
'''
import sys
import numpy as np

f = open(sys.argv[1])
num_node, num_edge = map(int, f.readline().split())
graph = [tuple(map(int, f.readline().split())) for _ in range(num_edge)]


def floyd_warshall(graph):
    A =
    for k in range(num_node):
        for i in range(num_node):
            for j in range(num_node):
