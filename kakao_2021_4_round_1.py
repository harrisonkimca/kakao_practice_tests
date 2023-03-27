'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 4


'''

parameters = [
  {
    "n": 6,
    "s": 4,
    "a": 6,
    "b": 2,
    "fares": [
      [4,1,10],
      [3,5,24],
      [5,6,2],
      [3,1,41],
      [5,1,24],
      [4,6,50],
      [2,4,66],
      [2,3,22],
      [1,6,25]
    ]
  },{
    "n": 7,
    "s": 3,
    "a": 4,
    "b": 1,
    "fares": [
      [5,7,9],
      [4,6,4],
      [3,6,1],
      [3,2,3],
      [2,1,6]
    ]
  },{
    "n": 6,
    "s": 4,
    "a": 5,
    "b": 6,
    "fares": [
      [2,6,6],
      [6,3,7],
      [4,6,7],
      [6,5,11],
      [2,5,12],
      [5,3,20],
      [2,4,8],
      [4,3,9]
    ]
  }
]

expected_results = [
  82,
  14,
  18
]

import sys
from collections import deque

def get_adjacency_list(edges):
  child_nodes = {}
  for node in edges:
    if node[0] in child_nodes:
      child_nodes[node[0]].append((node[1],node[2]))
    else:
      child_nodes[node[0]] = [(node[1],node[2])]
    # assume undirected graph
    if node[1] in child_nodes:
      child_nodes[node[1]].append((node[0],node[2]))
    else:
      child_nodes[node[1]] = [(node[0],node[2])]
  return child_nodes

def get_shortest_path_tree(start,links):
  total_fare = {}
  queue = deque()
  visited = set()
  max_value = sys.maxsize
  # initiate total_fare and queue with start node
  total_fare[start] = (0,0)
  queue.append(start)
  # assign remaining nodes in total_fare with max_value
  for node in links:
    if node != start:
      total_fare[node] = (max_value,0)
  
  while queue:
    current = queue.popleft()
    # *** also check for nodes with no edges ***
    if current not in visited and current in links:
      # find fares for all neighboring nodes 
      for neighbor in links[current]:
        # add neighbor fare to current node's fare
        check_path = total_fare[current][0] + neighbor[1]
        # if new fare is lower then replace as lowest fare
        # and record current node as previous node
        if check_path < total_fare[neighbor[0]][0]:
          total_fare[neighbor[0]] = (check_path,current)
          # add neighbor to queue
          queue.append(neighbor[0])
    # after checking all neighbors add current node to visited
    visited.add(current)
  return total_fare

def problem(**kwargs):
  n = kwargs["n"]
  s = kwargs["s"]
  a = kwargs["a"]
  b = kwargs["b"]
  fares = kwargs["fares"]
  
  # get adjacency list and assume undirected graph
  links = get_adjacency_list(fares)
  # print(f"links: {links}")
  # find shortest path tree from start node
  # to avoid key value error (ie, start can be any node)
  # use paths from start to check for separate fare
  path_s = get_shortest_path_tree(s, links)
  separate_fare = path_s[a][0] + path_s[b][0]
  # initiate shared_fare as max_value
  max_value = sys.maxsize
  shared_fare = (max_value,0)
  # check paths for all nodes
  for i in range(n):
    node = i + 1
    # check for nodes with no edges
    if node != s and node in links:
      # find shortest path for all other nodes
      path = get_shortest_path_tree(node, links)
      check_path = path_s[node][0] + path[a][0] + path[b][0]
      # find shortest path assuming separate fares from any of the other nodes
      if check_path < shared_fare[0]:
        shared_fare = (check_path, node)

  if shared_fare[0] < separate_fare:
    print(f"shared_fare: {shared_fare}")
    return shared_fare[0]
  else:
    print(f"separate_fare: {separate_fare}")
    return separate_fare


for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

