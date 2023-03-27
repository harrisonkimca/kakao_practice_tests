# https://www.delftstack.com/howto/python/dfs-python/#:~:text=The%20depth%2Dfirst%20search%20is,it%20reaches%20the%20leaf%20node.

import networkx as nx
import matplotlib.pyplot as plt

n = 10

starts = [
    1
]
ends = [
    11
]
roads = [
        [1,2],
        [1,3],
        [2,6],
        [2,7],
        [3,5],
        [3,10],
        [7,8],
        [7,9],
        [8,9],
        [3,4],
        [4,10],
        [4,11],
        [10,11]
        ]

# Generate graph
G = nx.DiGraph()

for i in range(n):
  G.add_node(i+1)
for road in roads:  
  G.add_edge(road[0],road[1])

# Save graph image
plt.figure()
pos = nx.spring_layout(G, k=0.15, iterations=20)
nx.draw(G, pos, with_labels=True)  
plt.savefig(f"dfs_graph.png", bbox_inches='tight')

# dfs using iteration
def dfs_iteration(graph, start):
  stack = [start]
  traversed = [start]

  while stack:
    node = stack[-1]
    # print(f"stack_1:{stack}")
    print(f"node_1:{node}")
    if node not in traversed:
      traversed.append(node)
      # print(f"traversed_1:{traversed}")
    pop = True
    # print(f"pop_1:{pop}")
    out_edges_all = list(graph.out_edges(node))
    for out_edge in out_edges_all:
      neighbor = out_edge[1]
      # print(f"neighbor:{neighbor}")
      if neighbor not in traversed:
        stack.append(neighbor)
        # print(f"stack_2:{stack}")
        pop = False
        # print(f"pop_2:{pop}")
        break
    if pop:
      # print(f"stack_pop:{stack[0]}")
      stack.pop()
  return traversed

# print("Depth First Search (Iteration):")
# print(dfs_iteration(G,1))

# dfs using recursion
start = 1
traversed = []
stack = [start]

def dfs_recursion(stack, traversed, graph, vertex):
  if vertex not in traversed:
    traversed.append(vertex)
    out_edges_all = list(graph.out_edges(vertex))
    for out_edge in out_edges_all:
      neighbor = out_edge[1]
      stack.append(neighbor)
      print(f"stack:{stack}")
      dfs_recursion(stack, traversed, G, neighbor)
      # every time edges 'list' is empty (ie, dead end) then
      # recursion moves to next line and 'pops' node from
      # stack before 'for loop' moves to next node    
      stack.pop()
  return traversed

print("Depth First Search (Recursion):")
print(dfs_recursion(stack, traversed, G, start))