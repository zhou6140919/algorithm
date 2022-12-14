'''
The first line indicates the number of vertices and edges, respectively.
Each subsequent line describes an edge (the first two numbers are its tail and head, respectively)
and its length (the third number). NOTE: some of the edge lengths are negative.
NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path".
Precisely, you must first identify which, if any, of the three graphs have no negative cycles.
For each such graph, you should compute all-pairs shortest paths and remember the smallest one
(i.e., compute $min_{u,v∈V}d(u,v)$, where $d(u,v)$ denotes the shortest-path distance from $u$ to $v$).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below.
If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below.
If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question.
OPTIONAL: If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!
'''

import sys
from tqdm import trange
import numpy as np


def floyd_warshall(graph, num_node):
    A = np.zeros([num_node, num_node, num_node])
    for i in range(num_node):
        for j in range(num_node):
            if j+1 in graph[i+1]:
                if i == j:
                    A[i][j][0] = 0
                else:
                    A[i][j][0] = graph[i+1][j+1]
            else:
                A[i][j][0] = np.inf

    for k in trange(1, num_node):
        for i in range(num_node):
            for j in range(num_node):
                A[i][j][k] = min(A[i][j][k-1], A[i][k][k-1]+A[k][j][k-1])
    for i in range(num_node):
        if A[i][i][num_node-1] < 0:
            raise ValueError(f'Negative cycle detected at node {i+1}')
    return A[:, :, num_node-1].min()


def main():
    f = open(sys.argv[1])
    num_node, num_edge = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for _ in range(num_edge)]
    graph = {i: {} for i in range(1, num_node+1)}
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    min_dist = floyd_warshall(graph, num_node)
    print(min_dist)


if __name__ == '__main__':
    main()
