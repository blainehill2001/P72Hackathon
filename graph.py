import networkx as nx
from matplotlib import pyplot as plt
import google_maps
api_key = "AIzaSyBF1v47rTxjmm0LEBx-vtO5IDWYvlUBBcA"

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, start, end, distance):
        self.graph.add_edge(start, end, weight=distance)

    def display_edges(self):
        print(f"Total edges: {len(self.graph.edges)}")

    def plot_graph(self):
        pos = nx.spring_layout(self.graph)
        weights = [self.graph[u][v]["weight"] for u, v in self.graph.edges()]
        plt.figure(figsize=(10, 8))
        nx.draw(
            self.graph,
            pos,
            node_size=10,
            edge_color=weights,
            width=1,
            edge_cmap=plt.cm.Blues,
            with_labels=True,
        )
        plt.title("Graph Visualization")
        plt.show()

    def minimum_spanning_tree(self):
        mst = nx.minimum_spanning_tree(self.graph)
        return mst

    def dfs(self, start):
        visited = set()
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
        return order


# Example usage
graph = Graph()

data = calculate_all_routes(api_key, landmarks)

for start, end, distance in data:
    graph.add_edge(start, end, distance)

mst = graph.minimum_spanning_tree()

# Start the DFS from the first landmark
start_landmark = landmark[0]
sorted_order = graph.dfs(start_landmark)

print("Sorted order to visit the landmarks:")
print(sorted_order)

nx.draw(mst, with_labels=True)
plt.show()

def results():
    return sorted_order

