import collections
import sys
import random


def return_emptylist():
    return []


def return_false():
    return False


def ParseGraph(filename):
    edges = []
    for l in open(filename):
        fields = [int(f) for f in l.split()]
        edges.append(tuple(fields))

    adjacency = collections.defaultdict(return_emptylist)
    reverse_adjacency = collections.defaultdict(return_emptylist)
    for e in edges:
        adjacency[e[0]] = adjacency[e[0]] + [e]
        reverse_adjacency[e[1]] = reverse_adjacency[e[1]] + [(e[1], e[0])]

    return adjacency, reverse_adjacency, edges


t = 0
s = 0
finishing = {}
leader = {}
explored = collections.defaultdict(return_false)


def ResetState():
    global t, s, finishing, leader, explored
    t = 0
    s = 0
    finishing = {}
    leader = {}
    explored = collections.defaultdict(return_false)


def DFSLoop(edges, labeling, reversed=False):
    global s
    for i in labeling:
        if not explored[i]:
            s = i
            DFS(edges, i, reversed)


forward_adjacency = {}
reverse_adjacency = {}


def DFS(edges, start, reversed=False):
    global t
    if reversed:
        adjacency = reverse_adjacency
    else:
        adjacency = forward_adjacency

    # Iterative (i.e. manually managing a stack) solution.
    stack = []
    stack.append((start, 1))

    while len(stack) > 0:
        current, phase = stack.pop()
        if phase == 1:
            explored[current] = True
            leader[current] = s
            edge_found = False
            for edge in adjacency[current]:
                if not explored[edge[1]]:
                    stack.append((current, 1))
                    stack.append((edge[1], 1))
                    edge_found = True
                    break
            if not edge_found:
                stack.append((current, 2))
        if phase == 2:
            t += 1
            finishing[current] = t


forward_adjacency, reverse_adjacency, edges = ParseGraph("scc.txt")


num_nodes = max([e[0] for e in edges] + [e[1] for e in edges])
labeling = range(num_nodes, 0, -1)
DFSLoop(edges, labeling, True)


inverse_finishing = dict((v, k) for k, v in finishing.items())
finish_labeling = [inverse_finishing[i] for i in range(num_nodes, 0, -1)]

ResetState()
DFSLoop(edges, finish_labeling)


sccs = {}
for i in leader:
    if leader[i] not in sccs:
        sccs[leader[i]] = [i]
    else:
        sccs[leader[i]].append(i)
num_largest = []
for i in sccs:
    a = len(sccs[i])
    if len(num_largest) < 5:
        num_largest.append(a)
    if a > min(num_largest):
        num_largest.remove(min(num_largest))
        num_largest.append(a)
print(",".join(sorted(num_largest, reverse=True)))
