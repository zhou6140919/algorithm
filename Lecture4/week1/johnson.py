'''
Reduces APSP to 
- 1 invocation of Bellman-Ford O(mn)
- n invocations of Dijkstra O(mnlogn)

If there are no negative cycles in the graph, there always exists a magical vertex weight that transforms all
of the edge links to be non-negative.
'''
