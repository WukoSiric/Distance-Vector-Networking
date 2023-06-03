class Graph:
    # Constructor - Initialises adjacency list
    def __init__(self):
        self.adj_list = {}

    # Add edge - Adds edge between two nodes with given weight
    # Parameters: node1, node2, weight
    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj_list:
            self.adj_list[node1] = {}
        if node2 not in self.adj_list:
            self.adj_list[node2] = {}

        self.adj_list[node1][node2] = weight
        self.adj_list[node2][node1] = weight

    # Remove edge - Removes edge between two nodes
    # Parameters: node1, node2
    def remove_edge(self, node1, node2):
        if node1 not in self.adj_list:
            return
        if node2 not in self.adj_list:
            return

        del self.adj_list[node1][node2]
        del self.adj_list[node2][node1]

    # Get neighbors - Returns list of neighbors of given node
    # Parameters: node
    def get_neighbors(self, node):
        return self.adj_list[node]

    # Print graph - Prints adjacency list (for debugging)
    def print_graph(self):
        for node, neighbors in self.adj_list.items():
            print(f"Node {node}: {neighbors}")