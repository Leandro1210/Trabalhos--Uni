import heapq

# Classe para representar um grafo
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

# Algoritmo de Dijkstra para encontrar o menor caminho
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

# Algoritmo de Kruskal para encontrar a árvore geradora mínima
def kruskal(graph):
    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    for node in graph.nodes:
        parent[node] = node
        rank[node] = 0

    minimum_spanning_tree = set()
    edges = list(graph.distances.keys())
    edges.sort(key=lambda x: graph.distances[x])

    for edge in edges:
        node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree

# Exemplo de uso dos algoritmos
graph = Graph()
for node in range(1, 6):
    graph.add_node(node)

graph.add_edge(1, 2, 7)
graph.add_edge(1, 3, 9)
graph.add_edge(1, 6, 14)
graph.add_edge(2, 3, 10)
graph.add_edge(2, 4, 15)
graph.add_edge(3, 4, 11)
graph.add_edge(3, 6, 2)
graph.add_edge(4, 5, 6)
graph.add_edge(5, 6, 9)

print("Menor caminho usando Dijkstra:")
distances, paths = dijkstra(graph, 1)
print(distances)

print("\nÁrvore Geradora Mínima usando Kruskal:")
mst = kruskal(graph)
print(mst)
