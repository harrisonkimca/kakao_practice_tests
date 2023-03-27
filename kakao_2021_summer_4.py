'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 4

'''

parameters = [
  {
    "ns": 3,
    "starts": 1,
    "ends": 3,
    "roadss": [
      [1,2,2],
      [3,2,3]
    ],
    "trapss": [2],
  }, {
    "ns": 4,
    "starts": 1,
    "ends": 4,
    "roadss": [
      [1,2,1],
      [3,2,1],
      [2,4,1]
    ],
    "trapss": [2,3],
  }, {
    "ns": 4,
    "starts": 1,
    "ends": 4,
    "roadss": [
      [1,3,2],
      [1,2,3],
      [2,3,2],
      [2,4,1],
      [3,4,2],
    ],
    "trapss": [2],
  }, {
    "ns": 4,
    "starts": 1,
    "ends": 4,
    "roadss": [
      [1,3,3],
      [1,2,3],
      [2,3,2],
      [2,4,1],
      [3,4,2],
    ],
    "trapss": [2],
  }, {
    "ns": 10,
    "starts": 1,
    "ends": 11,
    "roadss": [
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
    ],
    "trapss": [4,7],
  }
]

expected_results = [
  5,
  4,
  4,
  5,
  6
]


# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
import os
import networkx as nx
import sys
import matplotlib.pyplot as plt

my_dir = "./"
for fname in os.listdir(my_dir):
  if fname.startswith("di_graph_"):
    os.remove(os.path.join(my_dir, fname))

def reverse_edge(G,node_1,node_2):
  attrs = G.get_edge_data(node_1, node_2)
  G.add_edge(node_2, node_1, time=attrs["time"])
  G.remove_edge(node_1, node_2)

def spring_trap(G,node,traps):  # O(e)
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
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True)
  edge_labels = nx.get_edge_attributes(G,"time")
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
  if title is not None:
    plt.title(title)
  plt.savefig(f"di_graph_{graph_number:2}.png", bbox_inches='tight')
  graph_number += 1

def not_in_shortest_time(check_state,shortest_time):  # O(len(shortest_time))
  for state in shortest_time:
    check_edges = check_state[0].edges()
    shortest_time_edges = state[0].edges()
    if check_edges == shortest_time_edges and check_state[1] == state[1]:
      return False
  return True

# variables for the input size = v (number of vertices), e (number of edges)
# adjacency list -> O((v+e)*lg(v)) = O(v*lg(v)+e*lg(v))
# adjacency matrix -> O(v^2)
# networkx uses a hybrid data structure for fast operations, so it will probably be possible to implement djikstra's as fast as if it were using an adjacency list
# original graph: v1, e1, t
# transformed graph: see whiteboard
def run_dijkstra(G,start,end,traps):
  plot_graph(G,"start")  
  unvisited = [] # O(1) * 1
  G_copy = G.copy() # O(v+e) * 1
  unvisited.append((G_copy,start))
  shortest_time = {}
  # set shortest_time variable to max_value
  max_value = sys.maxsize
  shortest_time[unvisited[0]] = 0
  while unvisited:  # O(1) * how many times does the while loop
    # find min_state
    min_state = None
    for state in unvisited:  # O(len(unvisited))
      if min_state is None:
        min_state = state
      elif shortest_time[state] < shortest_time[min_state]:
        min_state = state
    # after finding min_state, find neighbors of min_state
    min_graph = min_state[0]
    out_edges = list(min_graph.out_edges(min_state[1]))
    for chosen_edge in out_edges:  # O(1) * O(e) * number of times while loop runs
      min_node = min_state[1]
      neighbor_graph = min_graph.copy()
      neighbor_node = chosen_edge[1]
      neighbor_state = (neighbor_graph,neighbor_node)
      spring_trap(neighbor_graph,neighbor_node,traps)  # O(e) * O(e) * number of times while loop runs
      if not_in_shortest_time(neighbor_state,shortest_time): # O(len(shortest_time))
        shortest_time[neighbor_state] = max_value
        unvisited.append(neighbor_state)
        time = min_graph.get_edge_data(min_node,neighbor_node)['time']
        time_check = shortest_time[min_state] + time
        # only add to shortest_time if time is lower value
        if time_check < shortest_time[neighbor_state]:
          shortest_time[neighbor_state] = time_check
      # for time in shortest_time:
        # print(f"NODE:     {time[1]}   EDGES:     {time[0].edges()}")
    # remove min_state from unvisited list
    unvisited.remove(min_state)
  # check for lowest time
  shortest_time_value = None
  for state in shortest_time:  #O(len(shortest_time))
    if state[1] == end and shortest_time_value is None:
      shortest_time_value = shortest_time[state]
    elif state[1] == end and shortest_time[state] < shortest_time_value:
      shortest_time_value = shortest_time[state]

  return shortest_time_value
    
def new_state(next_graph,next_node,current_path): # O(len(current_path))
  for check_graph, check_node in current_path:
    next_graph_edges = next_graph.edges()
    check_graph_edges = check_graph.edges()
    if next_graph_edges == check_graph_edges and check_node == next_node:
      return False
  return True

def minimum_escape_time(n,start,end,roads,traps):
  # set up graph data structure for the problem
  G = nx.DiGraph()
  for i in range(n):
    G.add_node(i+1)
  for road in roads:  
    G.add_edge(road[0],road[1],time=road[2])

  # print("-------------Brute force------------")  
  # return run_brute_force(G, start, end , traps)
  print("--------------Dijkstra--------------")
  return run_dijkstra(G, start, end, traps)  

def run_brute_force(G,start,end,traps):
  # brute force solution:
    # 1. try every possible path, keeping track of the distance of each path
    # 2. avoid repetition of the same state along the current path:
      # state means current node and graph edges
      # use G.copy() to take a snapshot of the whole graph
    # 3. choose path from start to end with smallest distance

  # initiate stack with initial state (current_graph,current_node,current_time)
  # pop off each state as visited and push to stack all possible states when visiting the next state
  G_copy = G.copy()
  stack = [(G_copy,start,0,[(G_copy,start)])] # .append() means push, .pop() means pop
  visited = []
  while stack:  # O(len(stack))
    current_state = stack.pop()    
    current_graph,current_node,current_time,current_path = current_state
    # plot_graph(current_graph,f"current_node: {current_node}")
    out_edges_all = list(current_graph.out_edges(current_node))
    for out_edge in out_edges_all:  # O(out_edges)
      next_graph = current_graph.copy()
      edge_node = out_edge[0]
      next_node = out_edge[1]
      spring_trap(next_graph,next_node,traps)  # O(len(out_edges & in_edges))
      # plot_graph(next_graph,f"current_node: {current_node}, next_node: {next_node}")
      
      # if not already visited then push to stack
      if new_state(next_graph,next_node,current_path): # O(len(current_path))
        next_time = current_time+current_graph.get_edge_data(edge_node,next_node)['time']
        next_path = current_path.copy()
        next_path.append((next_graph,next_node))
        stack.append((next_graph,next_node,next_time,next_path))
    visited.append(current_state)
  # print(f"visited: {visited}")
      
  # check visited list for state with end node and lowest time value
  reply = []
  for result in visited: # O(len(visited))
    if result[1] == end:
      if not reply:
        reply = result
      elif result[2] < reply[2]:
        reply = result
  return reply[2]


def problem(**kwargs):
  n = kwargs["ns"]
  start = kwargs["starts"]
  end = kwargs["ends"]
  roads = kwargs["roadss"]
  traps = kwargs["trapss"]

  result = minimum_escape_time(n,start,end,roads,traps)
  return result

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
