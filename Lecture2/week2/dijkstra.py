from collections import defaultdict
import copy


class Graph:
    def __init__(self, path):
        data = open(path).readlines()
        data = [i.strip() for i in data]
        data = [i.split("\t") for i in data]

        graph = defaultdict(list)

        for line in data:
            start_vertex = line[0]
            for end_tuple in line[1:]:
                end_vertex, length = end_tuple.split(",")
                end_vertex, length = int(end_vertex), int(length)
                graph[start_vertex].append((end_vertex, length))
                graph[end_vertex].append((start_vertex, length))

        self.graph = graph

        self.nodes = list(self.graph.keys())
        # print(self.nodes[0])

    def get_min_edge(self, visited):
        distance = {}
        for v_node in visited.keys():
            for edge_tuple in self.graph[v_node]:
                out_node, length = edge_tuple
                score = length + visited[v_node]
                if distance.get(out_node, 1000000) == 1000000:
                    distance[out_node] = score
                else:
                    if score < distance[out_node]:
                        distance[out_node] = score
        if distance == {}:
            return (0, False)
        min_distance = sorted(
            [(int(k), v) for k, v in distance.items() if int(k) not in visited.keys()],
            key=lambda x: x[1],
        )[0]
        # print(min_distance)
        return min_distance

    def get_shortest_path(self, source_node, target_node):
        visited = {source_node: 0}
        unvisited = copy.deepcopy(self.nodes)
        unvisited.remove(1)
        while target_node in unvisited:
            # print("visited", list(visited.keys()))
            next_node, distance = self.get_min_edge(visited)
            if not distance:
                return 1000000
            visited[next_node] = distance
            unvisited.remove(next_node)
        return visited[target_node]


graph = Graph("data.txt")
ans = []
for t in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
    l = graph.get_shortest_path(1, t)
    ans.append(l)
print(",".join([str(i) for i in ans]))
