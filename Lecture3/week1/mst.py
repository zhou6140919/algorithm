# Minimum Spanning Tree Algorithm


data = open("edges.txt").readlines()
data = data[1:]
v1s = [int(line.strip().split()[0]) for line in data]
v2s = [int(line.strip().split()[1]) for line in data]
costs = [int(line.strip().split()[2]) for line in data]
edges = []
for v1, v2, c in zip(v1s, v2s, costs):
    edges.append([v1, v2, c])
    edges.append([v2, v1, c])

explored_vertices = [1]
minimum_cost = []

while len(explored_vertices) < 500:
    cross_edges = []
    for ev in explored_vertices:
        for e in edges:
            if e[0] == ev and e[1] not in explored_vertices:
                cross_edges.append(e)
    cross_edges = sorted(cross_edges, key=lambda x: x[2])
    explored_vertices.append(cross_edges[0][1])
    minimum_cost.append(cross_edges[0][2])

print(sum(minimum_cost))
