'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 2

To prevent corona virus infection, test takers must keep a distance and wait, but since this is a development job interview, the following rules are guiding them to sit at a distance in the waiting room.

1. There are 5 waiting rooms, each of which is 5×5 in size.
2. In order to maintain a distance, please do not sit with a Manhattan distance of 2 or less between test takers.
3. However, it is allowed if the seats where the test takers are seated are blocked by a partition.

✔Manhattan distance: If two tables T1 and T2 are located in matrices (r1, c1) and (r2, c2) respectively, then the Manhattan distance between T1 and T2 is |r1 – r2| + |c1 – c2|.

"POOPP" 
"OXXOX" 
"OPXPX" 
"OOXOX" 
"POXXP"

"PXPXP" 
"XPXPX" 
"PXPXP" 
"XPXPX" 
"PXPXP"

'''


parameters = [
  {
    "places": ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
  }, {
    "places": ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
  }, {
    "places": ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"]
  }, {
    "places": ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
  }, {
    "places": ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
  }
]

expected_results = [
  1,
  0,
  1,
  1,
  1
]


import networkx as nx
import matplotlib.pyplot as plt

# brute-force version to construct graph
def make_graph_brute_force(room, G):
  for i, row in enumerate(room):
    for j, seat in enumerate(row):
      current_node = f"{i}{j}{seat}"
      G.add_node(current_node)
      if seat != 'X':
        # add edge to right neighbour
        if j < 4 and room[i][j+1] != 'X':
          G.add_edge(current_node, f"{i}{j+1}{room[i][j+1]}")
        # add edge to left neighbour
        if j > 0 and room[i][j-1] != 'X':
          G.add_edge(current_node, f"{i}{j-1}{room[i][j-1]}")
        # add edge to down neighbour
        if i < 4 and room[i+1][j] != 'X':
          G.add_edge(current_node, f"{i+1}{j}{room[i+1][j]}")
        # add edge to up neighbour
        if i > 0 and room[i-1][j] != 'X':
          G.add_edge(current_node, f"{i-1}{j}{room[i-1][j]}")
  return G

# efficient version to construct graph
def make_graph(room, G):
  for i, row in enumerate(room):
    for j, current_value, in enumerate(row):
      current_vertex = f"{i}{j}{current_value}"
      G.add_node(current_vertex)
      if current_value != "X":
        for adjacent_i, adjacent_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
          if 0 <= adjacent_i < len(room) and 0 <= adjacent_j < len(row):
            adjacent_value = room[adjacent_i][adjacent_j]
            if adjacent_value != "X":
              adjacent_vertex = f"{adjacent_i}{adjacent_j}{adjacent_value}"
              G.add_edge(current_vertex, adjacent_vertex)
  return G

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html

# parse through all tuples from breadth-first search that start with 'P' to find additional 'P' 
def check_seats(room, G):
  check = 1
  for i, row in enumerate(room):
    for j, current_value, in enumerate(row):
      if current_value == 'P':  
        current_vertex = f"{i}{j}{current_value}"
        edges = list(nx.bfs_edges(G,current_vertex,depth_limit=2))
        for c_value in edges:
          c_string = c_value[1]
          if c_string[2] == 'P':
            check = 0
  return check


def problem(**kwargs):
  places = kwargs["places"]

  # build graphs
  g_dict = nx.Graph()
  make_graph_brute_force(places, g_dict)

  # draw and save graphs
  plt.figure(test_index)
  nx.draw(g_dict, with_labels=True)
  plt.savefig(f'room_{test_index}.png', bbox_inches='tight')

  # check rooms if all test takers keeping distance
  check_room = check_seats(places, g_dict)
  return check_room

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
