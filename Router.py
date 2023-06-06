import copy
import math
INF = math.inf

class Router:
    def __init__(self, name):
        self._name = name
        self.distance_table = {}
        self.updates_to_process = [] # update[i] = (source, distance_table)
        self.routing_table = {}
        self.update_neighbors = False

    def initialize_distance_table(self, nodes):
        nodes = nodes.copy()
        if self._name in nodes:
            nodes.remove(self._name)
        for node in nodes:
            self.distance_table[node] = {}
            for n in nodes:
                self.distance_table[node][n] = float('inf')
    
    def print_distance_table(self):
        nodes = sorted(self.distance_table.keys())
        header = [' '] + nodes

        # Print table header
        print('\t'.join(header))

        # Print table rows
        for node in nodes:
            row = [node] + [str(self.distance_table[node][n]).replace('inf', 'INF') for n in nodes]
            print('\t'.join(row))

    def update_self(self, graph, routers_list):
        neighbors = graph.get_neighbors(self._name)
        for neighbor in neighbors:
            self.distance_table[neighbor][neighbor] = graph.adj_list[self._name][neighbor]

        # If not a neighbor, set cost to infinity for all destinations 
        for router in routers_list:
            if router._name not in neighbors and router._name != self._name:
                for dest in self.distance_table:
                    self.distance_table[dest][router._name] = INF
        self.update_neighbors = True

    def send_updates(self, neighbors, routers_list): 
        if self.update_neighbors == True: 
            for router in routers_list:
                if router._name in neighbors:
                    router.updates_to_process.append((self._name, copy.deepcopy(self.distance_table)))
        self.update_neighbors = False

    def process_received_tables(self):
        for update in self.updates_to_process:
            received_from = update[0] 
            received_distance_table = update[1]
            for dest in self.distance_table:
                if dest == received_from:
                    continue
                for via_node in self.distance_table[dest]: 
                    if via_node == received_from: 
                        previous_cost = self.distance_table[dest][via_node]
                        cost_to_received_from = self.distance_table[received_from][received_from]
                        total_cost = cost_to_received_from + self.find_min_cost(received_distance_table, dest)
                        self.distance_table[dest][received_from] = total_cost
                        if previous_cost != total_cost:
                            self.update_neighbors = True

        # Reset updates to process
        self.updates_to_process = []

    def find_min_cost(self, distance_table, dest): 
        min_cost = INF
        for node in distance_table[dest]:
            if distance_table[dest][node] < min_cost:
                min_cost = distance_table[dest][node]
        return min_cost
    
    def create_routing_table(self):
        for dest in self.distance_table:
            min_cost = INF
            min_cost_node = INF
            for node in self.distance_table[dest]:
                if self.distance_table[dest][node] < min_cost:
                    min_cost = self.distance_table[dest][node]
                    min_cost_node = node
            self.routing_table[dest] = (min_cost_node, min_cost)

    def print_routing_table(self):
        self.create_routing_table()
        print(f"{self._name} Routing Table:")
        for dest in sorted(self.routing_table.keys()):
            print(f"{dest},{self.routing_table[dest][0]},{self.routing_table[dest][1]}")
        print()

    def process_after_update(self, graph, routers_list): 
        # Clear all updates
        self.updates_to_process = []
        original_distance_table = copy.deepcopy(self.distance_table)

        # Get neighbors costs
        neighbors = graph.get_neighbors(self._name)
        for neighbor in neighbors:
            self.distance_table[neighbor][neighbor] = graph.adj_list[self._name][neighbor]

        # If not a neighbor, set cost to infinity for all destinations
        for dest in self.distance_table: 
            for via_node in self.distance_table[dest]: 
                if via_node not in neighbors:
                    self.distance_table[dest][via_node] = INF
        
        for router in routers_list: 
            if (router._name in neighbors): 
                for dest in router.routing_table: 
                    if dest == self._name: 
                        continue
                    cost_to_via_node = self.distance_table[router._name][router._name]
                    via_node_to_dest = router.routing_table[dest][1]
                    self.distance_table[dest][router._name] = cost_to_via_node + via_node_to_dest
        
        if self.distance_table != original_distance_table: 
            self.update_neighbors = True

    def print_updates(self):
        print(f"{self._name} Updates to Process:")
        for update in self.updates_to_process:
            print(update)
        print()