# Distance Vector Routing Algorithm

This code implements the Distance Vector Routing algorithm (Bellman-Ford) for a network topology represented as an undirected graph. It calculates the distance tables for each node in a network at each iteration of the algorithm. The algorithm terminates when the distance tables of all nodes in the network converge.

After initially running, there is an update section where the user can modify or remove edges from the graph. The algorithm then runs again until convergence is reached, printing out the distance tables and routing tables for each router.

## To Do
- [ ] Add comments
- [ ] Add more test cases
- [ ] Implement split horizon
- [x] Put classes in separate files
- [x] Implement update section
- [x] Implement routing table
- [x] Implement convergence check
- [x] Implement Distance Vector Routing algorithm
- [x] Create distance table data structure
- [x] Implement graph adjacency list

## Usage

To run the code, execute the following command:

<!-- Make code segment -->
```bash
py DistanceVector
```

The code reads input from the standard input. The input format is as follows:

1. Specify the list of nodes in the network, each on a separate line. Enter `DISTANCEVECTOR` to indicate the end of the node list.
> ```
> X   
> Y   
> Z   
> DISTANCEVECTOR
> ```
2. Specify the edges between nodes and their weights. Each line should contain two node names and the weight separated by spaces. Enter `UPDATE` to indicate the end of the edge list. The code will then print the distance tables and routing tables for each router in the network.
> ```
> X Z 8
> X Y 2
> Y Z 3
> UPDATE
> ```
3. In the update section, specify the edges to modify or remove. Each line should contain two node names and an integer separated by spaces. Entering a weight of -1 removes an edge, while positive and  0 weights modify the edge weight. Enter `END` to indicate the end of the update list. 
> ```
> Y Z -1
> X Z 3
> END
> ```
4. The code will then print the distance tables and routing tables for each router in the network.

### Quick Start
To quickly test the program you can pipe/redirect the input from the included input files. For example, to run the program with the input from `input-update', you could use the following: 

**Bash**
`py DistanceVectorRouting < input` 

**PowerShell**
`Get-Content input | py DistanceVectorRouting`


## Classes

### Graph

- `add_edge(node1, node2, weight)`: Adds an edge between two nodes with the given weight to the graph.
- `remove_edge(node1, node2)`: Removes the edge between two nodes from the graph.
- `get_neighbors(node)`: Returns a list of neighbors of the given node.
- `print_graph()`: Prints the adjacency list of the graph (for debugging).

### Router

- `initialize_distance_table(nodes)`: Initializes the distance table for the router with all nodes in the network.
- `print_distance_table()`: Prints the current distance table for the router.
- `update_self(graph, routers_list)`: Updates the distance table of the router with its own costs to neighbors.
- `send_updates(neighbors, routers_list)`: Sends updates to neighbors if the router's distance table has changed.
- `process_received_tables()`: Processes received updates from neighbors to update the router's distance table.
- `find_min_cost(distance_table, dest)`: Finds the minimum cost to a destination in the given distance table.
- `create_routing_table()`: Creates the routing table for the router based on the distance table.
- `print_routing_table()`: Prints the routing table for the router.
- `process_after_update(graph, routers_list)`: Processes updates to the router's distance table after changes in the graph.
- `print_updates()`: Prints the updates to process (for debugging).

## Main Algorithm

The main algorithm starts by creating a graph and initializing routers with their distance tables. Then, it runs the Distance Vector Routing algorithm until convergence is reached. The algorithm sends updates to neighbors, processes received updates, and checks for convergence by comparing the distance tables of all routers. Finally, it prints the distance tables and routing tables for each router.

## Input/Output Format

### Input
The code expects the input to be provided through the standard input. Here is example input:
> The update section is optional. If you do not want to specify updates, you can skip to the end of the input. by entering `END` after `UPDATE` section.

```
X    # Node X
Y    # Node Y
Z    # Node Z
DISTANCEVECTOR    # Start of defining edges and weights
X Z 8    # Edge between X and Z with weight 8
X Y 2    # Edge between X and Y with weight 2
Y Z 3    # Edge between Y and Z with weight 3
UPDATE    # Start of specifying updates to the network
Y Z -1    # Update: Change weight of edge between Y and Z to -1
X Z 3    # Update: Change weight of edge between X and Z to 3
END    # End of input
```

### Output
The code prints the distance tables and routing tables for each router in the network. Here is the example output:
```
X Distance Table at t=0
     Y    Z    
Y    2    INF  
Z    INF  8    

Y Distance Table at t=0
     X    Z    
X    2    INF  
Z    INF  3    

Z Distance Table at t=0
     X    Y    
X    8    INF  
Y    INF  3    

X Distance Table at t=1
     Y    Z    
Y    2    11   
Z    5    8    

Y Distance Table at t=1
     X    Z    
X    2    11   
Z    10   3    

Z Distance Table at t=1
     X    Y    
X    8    5    
Y    10   3    

X Distance Table at t=2
     Y    Z    
Y    2    11   
Z    5    8    

Y Distance Table at t=2
     X    Z    
X    2    8    
Z    7    3    

Z Distance Table at t=2
     X    Y    
X    8    5    
Y    10   3    

X Routing Table:
Y,Y,2
Z,Y,5

Y Routing Table:
X,X,2
Z,Z,3

Z Routing Table:
X,Y,5
Y,Y,3

X Distance Table at t=3
     Y    Z    
Y    2    6    
Z    5    3    

Y Distance Table at t=3
     X    Z    
X    2    INF  
Z    7    INF  

Z Distance Table at t=3
     X    Y    
X    3    INF  
Y    5    INF  

X Distance Table at t=4
     Y    Z    
Y    2    8    
Z    9    3    

Y Distance Table at t=4
     X    Z    
X    2    INF  
Z    5    INF  

Z Distance Table at t=4
     X    Y    
X    3    INF  
Y    5    INF  

X Distance Table at t=5
     Y    Z    
Y    2    8    
Z    7    3    

Y Distance Table at t=5
     X    Z    
X    2    INF  
Z    5    INF  

Z Distance Table at t=5
     X    Y    
X    3    INF  
Y    5    INF  

X Routing Table:
Y,Y,2
Z,Z,3

Y Routing Table:
X,X,2
Z,X,5

Z Routing Table:
X,X,3
Y,X,5
```
