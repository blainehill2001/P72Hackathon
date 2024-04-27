import networkx as nx  # type: ignore
from matplotlib import pyplot as plt  # type: ignore

LAT_START = 0
LAT_END = 7
LONG_START = 0
LONG_END = 7


class Node:
    def __init__(self, longitude, latitude, priority=0):
        self.longitude = longitude
        self.latitude = latitude
        self.priority = priority


class Edge:
    def __init__(self, start_node, end_node, money=0):
        self.start_node = start_node
        self.end_node = end_node
        self.money = money
        self.transport_time = self.Manhattan_Distance()
        self.weight = self.calculate_weight()

    def Manhattan_Distance(self):
        # 100 is a magic number
        return (
            abs(self.start_node.longitude - self.end_node.longitude)
            + abs(self.start_node.latitude - self.end_node.latitude)
        ) * 100

    def calculate_weight(self):
        # naive objective function
        return self.transport_time + self.money + self.end_node.priority


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = dict()
        self.graph = nx.Graph()

    def add_node(self, longitude, latitude):
        node = Node(longitude, latitude)
        self.nodes[(longitude, latitude)] = node
        self.graph.add_node((longitude, latitude))
        return node

    def find_node(self, longitude, latitude):
        return self.nodes.get((longitude, latitude))

    def Manhattan_Distance(self, start_node, end_node):
        # 100 is a magic number
        return (
            abs(self.start_node.longitude - self.end_node.longitude)
            + abs(self.start_node.latitude - self.end_node.latitude)
        ) * 100

    def add_edge(self, node1, node2):
        if node1 and node2:
            edge = Edge(node1, node2)
            self.edges[(node1, node2)] = edge
            self.graph.add_edge(
                (node1.longitude, node1.latitude),
                (node2.longitude, node2.latitude),
                weight=edge.weight,
            )

    def update_edge(self, node1, node2, new_money, new_transport):
        if (node1, node2) not in self.edges:
            raise ValueError("Invalid edge. All the edges are connected to the N,W,S,E nodes")
        new_edge = self.edges[(node1, node2)]
        new_edge.money = new_money
        new_edge.transport_time = new_transport
        new_edge.weight = new_edge.calculate_weight()
        self.edges[(node1, node2)] = new_edge
        self.graph.add_edge(
            (node1.longitude, node1.latitude),
            (node2.longitude, node2.latitude),
            weight=new_edge.weight,
        )

    def connect_nodes(self):
        for lat in range(LAT_START, LAT_END):
            for lon in range(LONG_START, LONG_END):
                current_node = self.find_node(lon, lat)
                east_node = self.find_node(lon + 1, lat)
                self.add_edge(current_node, east_node)
                self.add_edge(east_node, current_node)
                south_node = self.find_node(lon, lat + 1)
                self.add_edge(current_node, south_node)
                self.add_edge(south_node, current_node)

    def build_network(self):
        for lat in range(LAT_START, LAT_END):  # Adjusted range for inclusive end
            for lon in range(LONG_START, LONG_END):  # Adjusted range for inclusive end
                self.add_node(lon, lat)
        self.connect_nodes()

    def is_valid_path(self, start, end, node):
        if (
            node.longitude >= min(start.longitude, end.longitude)
            and node.longitude <= (max(start.longitude, end.longitude) + 1)
            and node.latitude >= min(start.longitude, end.longitude)
            and node.latitude <= (max(start.latitude, end.latitude) + 1)
        ):
            return True
        return False

    def update_path(self, start, end, new_money, new_transport):
        seen = []
        for lon in range(
            min(start.longitude, end.longitude), max(start.longitude, end.longitude) + 1
        ):
            for lat in range(
                min(start.latitude, end.latitude), max(start.latitude, end.latitude) + 1
            ):
                node1 = self.find_node(lon, lat)

                for hdir in [-1, 1]:
                    if lon == max(start.longitude, end.longitude):
                        continue
                    if hdir * (end.longitude - start.longitude) >= 0:
                        node2 = self.find_node(lon + hdir, lat)
                        if self.is_valid_path(start, end, node2):
                            seen.append((node1, node2))
                for vdir in [-1, 1]:
                    if lat == max(start.latitude, end.latitude):
                        continue
                    if vdir * (end.latitude - start.latitude) >= 0:
                        node2 = self.find_node(lon, lat + vdir)
                        if self.is_valid_path(start, end, node2):
                            seen.append((node1, node2))
        for u, v in seen:
            self.update_edge(u, v, new_money, new_transport)

    def display_edges(self):
        print(f"Total edges: {len(self.edges)}")


# Example usage
graph = Graph()
graph.build_network()
graph.display_edges()

n1 = graph.find_node(1, 2)
n2 = graph.find_node(4, 5)
graph.update_path(n1, n2, 100, 100)


def plot_graph(graph):
    pos = {(lon, lat): (lon, lat) for lon, lat in graph.nodes.keys()}
    weights = [graph.graph[u][v]["weight"] for u, v in graph.graph.edges()]
    print(weights)

    plt.figure(figsize=(10, 8))
    nx.draw(
        graph.graph,
        pos,
        node_size=10,
        edge_color=weights,
        width=1,
        edge_cmap=plt.cm.Blues,
        with_labels=False,
    )
    plt.title("Graph Visualization")
    plt.show()


plot_graph(graph)
