import networkx as nx

graph = nx.Graph()
with open("input.txt") as f:
    for l in f.read().splitlines():
        k, vs = l.split(": ")
        for v in vs.split():
            graph.add_edge(k, v)

graph.remove_edges_from(nx.minimum_edge_cut(graph))
a, b = nx.connected_components(graph)
print(len(a) * len(b))
