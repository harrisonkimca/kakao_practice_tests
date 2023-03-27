import networkx as nx
import matplotlib.pyplot as plt


ns = [
    11
]
starts = [
    1
]
ends = [
    11
]
roadss = [
    [
        [1,2,2],
        [1,3,1],
        [2,6,3],
        [2,7,1],
        [3,5,3],
        [3,10,2],
        [7,8,1],
        [7,9,2],
        [8,9,1],
        [3,4,3],
        [4,10,2],
        [4,11,1],
        [10,11,2],
    ]
]
trapss = [
    [4,7]
]
expected_results = [
    5
]

def reverse_edge(G, node_1, node_2):
  attrs = G.get_edge_data(node_1, node_2)
  G.add_edge(node_2, node_1, time=attrs["time"])
  G.remove_edge(node_1, node_2)

def spring_trap(G, node, traps):
  if node in traps:
    in_edges = list(G.in_edges(node))
    out_edges = list(G.out_edges(node))
    for in_edge in in_edges:
      reverse_edge(G, in_edge[0], in_edge[1])
    for out_edge in out_edges:
      reverse_edge(G, out_edge[0], out_edge[1])

graph_number = 1
def plot_graph(G,title=None):
  global graph_number
  plt.figure()
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True)
  edge_labels = nx.get_edge_attributes(G,"time")
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
  if title is not None:
    plt.title(title)
  plt.savefig(f"di_graph_{graph_number}.png", bbox_inches='tight')
  graph_number += 1

def new_state(next_graph,next_node,current_path):  
  for check_graph, check_node in current_path:
    next_graph_edges = next_graph.edges()
    check_graph_edges = check_graph.edges()
    if next_graph_edges == check_graph_edges and check_node == next_node:
      # plot_graph(G, f"{next_node}")
      # plot_graph(check_graph, f"{check_node}")
      return False
  return True

def minimum_escape_time(n, start, end, roads, traps):
  G = nx.DiGraph()
  for i in range(n):
    G.add_node(i+1)
  for road in roads:  
    G.add_edge(road[0],road[1],time=road[2]) 
     
  G_copy = G.copy()
  stack = [(G_copy,start,0,[(G_copy,start)])]
  visited = []
  
  while stack:
    current_state = stack.pop()
    current_graph,current_node,current_time,current_path = current_state
    print(f"pop:{current_node}")
    out_edges_all = list(current_graph.out_edges(current_node))
    for out_edge in out_edges_all:
      next_graph = current_graph.copy()
      edge_node = out_edge[0]
      next_node = out_edge[1]
      spring_trap(next_graph,next_node,traps)
      # plot_graph(next_graph,f"current_node: {current_node}, next_node: {next_node}")
      # if not already visited then push to stack
      print(f"CHECK:{out_edge[0]}->{out_edge[1]}")
      if new_state(next_graph,next_node,current_path):
        next_time = current_time+current_graph.get_edge_data(edge_node,next_node)['time']
        next_path = current_path.copy()
        next_path.append((next_graph,next_node))
        stack.append((next_graph,next_node,next_time,next_path))
        # print stack node and time weight
        for i in stack:
          print(f"stack:({i[1]},{i[2]})")
    visited.append(current_state)
  print(visited)

  reply = []
  for result in visited:
    if result[1] == end:
      if not reply:
        reply = result
      elif result[2] < reply[2]:
        reply = result
  return reply[2]


for test_index in range(len(ns)):
  n = ns[test_index]
  start = starts[test_index]
  end = ends[test_index]
  roads = roadss[test_index]
  traps = trapss[test_index]
  
  result = minimum_escape_time(n, start, end, roads, traps)
  expected_result = expected_results[test_index]
  print(f"test {test_index}: ", end="")
  if result == expected_result:
    print("pass")
  else:
    print(f"fail (expected {expected_result}, but got {result})")
