# https://www.delftstack.com/howto/python/dfs-python/#:~:text=The%20depth%2Dfirst%20search%20is,it%20reaches%20the%20leaf%20node.

import networkx as nx
import matplotlib.pyplot as plt

ns = [
  3,
  4,
  4,
  4,
  10
]

starts = [
  1,
  1,
  1,
  1,
  1
]
ends = [
  3,
  4,
  4,
  4,
  11
]
roadss = [
  [
    [1,2,2],
    [3,2,3]
  ], [
    [1,2,1],
    [3,2,1],
    [2,4,1]
  ], [
    [1,3,2],
    [1,2,3],
    [2,3,2],
    [2,4,1],
    [3,4,2],
  ], [
    [1,3,3],
    [1,2,3],
    [2,3,2],
    [2,4,1],
    [3,4,2],
  ], [
    [1,2,2],
    [1,3,1],
    [2,6,3],
    [2,7,1],
    [3,5,3],
    [3,10,3],
    [7,8,1],
    [7,9,2],
    [8,9,1],
    [3,4,3],
    [4,10,2],
    [4,11,1],
    [10,11,2]
  ]
]

trapss = [
  [2],
  [2,3],
  [2],
  [2],
  [4,7]
]

expected_results = [
  5,
  4,
  4,
  5,
  6
]

import os
my_dir = "./"
for fname in os.listdir(my_dir):
  if fname.startswith("dfs_graph_"):
    os.remove(os.path.join(my_dir, fname))

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
    # plot_graph(G,f"current_node: {node}")

graph_number = 1
def plot_graph(G,title=None):
  global graph_number
  plt.figure()
  pos = nx.spring_layout(G,k=0.5,iterations=2)
  nx.draw(G, pos, with_labels=True)
  edge_labels = nx.get_edge_attributes(G,"time")
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
  if title is not None:
    plt.title(title)
  plt.savefig(f"dfs_graph_{graph_number:2}.png", bbox_inches='tight')
  graph_number += 1

def new_state(graph,node,traversed):
  for path in traversed:
    check_graph = path[0]
    check_graph_edges = check_graph.edges()
    graph_edges = graph.edges()
    check_node = path[1]
    if graph_edges == check_graph_edges and check_node == node:
      # plot_graph(graph, f"new_state_node:{node}")
      # plot_graph(check_graph, f"new_state_check_node:{check_node}")
      return False
  return True

def minimum_escape_time(n, start, end, roads, traps):
  # Generate graph
  G = nx.DiGraph()
  for i in range(n):
    G.add_node(i+1)
  for road in roads:  
    G.add_edge(road[0],road[1],time=road[2])
  # Save graph image
  plot_graph(G,"start")

  G_copy = G.copy()
  # iteration
  traversed = [(G_copy,start,0,[(G_copy,start)])]
  stack = [(G_copy,start,0,[(G_copy,start)])]
  print("-------------Depth First Search (Iteration)-------------")
  visited = dfs_iteration(stack,traversed,G,start)

  # recursion
  # traversed = []
  # stack = [(G_copy,start,0,[(G_copy,start)])]
  # print("-------------Depth First Search (Recursion)-------------")
  # visited = dfs_recursion(stack,traversed,G,start)
  
  reply = []
  for result in visited:
    if result[1] == end:
      if not reply:
        reply = result
      elif result[2] < reply[2]:
        reply = result
  return reply[2],reply[3]
  
# dfs using iteration
def dfs_iteration(stack,traversed,graph,start):
  while stack:
    # ONLY READ from stack
    state = stack[-1]
    current_graph,current_node,current_time,current_path = state
    if new_state(current_graph,current_node,traversed):
      traversed.append((current_graph,current_node,current_time,current_path))
    # TURN ON POP: allow while loop to pop from stack if no more new_state nodes from the subtree to add to stack
    pop = True
    out_edges_all = list(current_graph.out_edges(current_node))
    for out_edge in out_edges_all:
      next_graph = current_graph.copy()
      edge_node = out_edge[0]
      next_node = out_edge[1]
      spring_trap(next_graph,next_node,traps)
      if new_state(next_graph,next_node,traversed):
        next_time = current_time+current_graph.get_edge_data(edge_node,next_node)['time']
        next_path = current_path.copy()
        next_path.append((next_graph,next_node))
        stack.append((next_graph,next_node,next_time,next_path))
        # TURN OFF POP: keep drilling down subtree by adding nodes to stack
        pop = False
        break
    # only pop from stack if no more new_state nodes
    if pop:
      # REMOVE from stack
      stack.pop()
  return traversed
  
def dfs_recursion(stack,traversed,graph,vertex):
  state = stack[-1]
  current_graph,current_node,current_time,current_path = state
  spring_trap(current_graph,current_node,traps)
  if new_state(current_graph,current_node,traversed):
    traversed.append((current_graph,current_node,current_time,current_path))
    out_edges_all = list(current_graph.out_edges(vertex))
    for out_edge in out_edges_all:
      next_graph = current_graph.copy()
      edge_node = out_edge[0]
      neighbor = out_edge[1]
      next_time = current_time+current_graph.get_edge_data(edge_node,neighbor)['time']
      next_path = current_path.copy()
      next_path.append((next_graph,neighbor))
      stack.append((next_graph,neighbor,next_time,next_path))
      # print stack node and time weight
      # for i in stack:
      #   print(f"stack:(node:{i[1]},time:{i[2]})")
      # print("-----------") 
      dfs_recursion(stack,traversed,graph,neighbor)
      stack.pop()
  return traversed

for test_index in range(len(ns)):
  n = ns[test_index]
  start = starts[test_index]
  end = ends[test_index]
  roads = roadss[test_index]
  traps = trapss[test_index]
  
  result,path = minimum_escape_time(n, start, end, roads, traps)
  expected_result = expected_results[test_index]
  print(f"test {test_index}: ", end="")
  if result == expected_result:
    print("pass")
    route = []
    for node in path:
      route.append(node[1])
    print(f"path:{route}")
  else:
    print(f"fail (expected {expected_result}, but got {result})")