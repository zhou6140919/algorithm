'''
第 3 个问题
In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight independent set of a path graph. 

Download the text file below.

This file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702. 

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set.

The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set?

(By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.)
'''

import sys


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return [int(x) for x in data[1:]]


def max_weight_independent_set(weights):
    A = [0] * (len(weights) + 1)
    A[1] = weights[0]
    for i in range(2, len(weights) + 1):
        A[i] = max(A[i - 1], A[i - 2] + weights[i - 1])
    return A


def reconstruct(weights, A):
    S = []
    i = len(weights)
    while i >= 1:
        if A[i - 1] >= A[i - 2] + weights[i - 1]:
            i -= 1
        else:
            S.append(i)
            i -= 2
    return S


def main():
    weights = read_data(sys.argv[1])
    A = max_weight_independent_set(weights)
    S = reconstruct(weights, A)
    for v in [1, 2, 3, 4, 17, 117, 517, 997]:
        if v in S:
            print(1, end='')
        else:
            print(0, end='')


if __name__ == '__main__':
    main()
