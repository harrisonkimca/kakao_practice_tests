import sys

# Dijkstra Algorithm finds the shortest path between two nodes in a graph (problem needs to be represented as a graph) 

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        # Make symmetrical graph
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        # Returns the nodes of the graph
        return self.nodes

    def get_outgoing_edges(self, node):
        # Returns the neighbors of a node
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        # Returns the value of an edge between two nodes
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    # Use max_value to initialize the "infinity" value of unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
      shortest_path[node] = max_value
      print(f"shortest_path[{node}]:{shortest_path[node]}")
    # Initialize starting node value with 0   
    shortest_path[start_node] = 0
    print(f"shortest_path[{start_node}]:{shortest_path[start_node]}")

    while unvisited_nodes:
        print("*************WHILE LOOP*************")
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            print(f"node: {node}")
            if current_min_node == None:
                current_min_node = node
                print(f"if shortest_path[{node}]:{shortest_path[node]} < shortest_path[{current_min_node}]:{shortest_path[current_min_node]}")
                
            elif shortest_path[node] < shortest_path[current_min_node]:
                print(f"elif shortest_path[{node}]:{shortest_path[node]} < shortest_path[{current_min_node}]:{shortest_path[current_min_node]}")
                current_min_node = node
                
            print(f"current_min_node: {current_min_node}")

        # Retrieve current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        print(f"neighbors:{neighbors}")
        for neighbor in neighbors:
            print("******FOR NEIGHBOR IN NEIGHBORS******")
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            print(f"tentative_value:{tentative_value} = shortest_path[{current_min_node}]:{shortest_path[current_min_node]} + graph.value({current_min_node}, {neighbor}):{graph.value(current_min_node, neighbor)}")
            print(f"if tentative_value:{tentative_value} < shortest_path[{neighbor}]:{shortest_path[neighbor]}")
            if tentative_value < shortest_path[neighbor]:
                print("*****ADD TO PREVIOUS_NODES*****")
                shortest_path[neighbor] = tentative_value
                print(f"shortest_path[{neighbor}]:{shortest_path[neighbor]} = tentative_value:{tentative_value}")
                # Also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
                print(f"previous_nodes[{neighbor}]:{previous_nodes[neighbor]} = current_min_node:{current_min_node}")
        # Node marked as "visited" after checking all neighbors
        unvisited_nodes.remove(current_min_node)
        print(f"unvisited_nodes:{unvisited_nodes}")
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

def print_edges(graph):
  for k, v in graph.graph.items():
    print(f"{k}:{v}")

  
def run_dijkstra():
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
 
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}
    
    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    graph = Graph(nodes, init_graph)
    print_edges(graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
    print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")

run_dijkstra()