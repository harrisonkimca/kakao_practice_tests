routes = [
      [1,2,3],
      [1,3,5],
      [2,1,3],
      [2,3,1],
      [2,4,2],
      [3,1,5],
      [3,2,1],
      [3,4,3],
      [3,5,6],
      [4,2,2],
      [4,3,3],
      [4,5,4],
      [5,3,6],
      [5,4,4]
    ]

'''

       2
    /  |  \
 3 /   |   \ 2
  /    |    \
 1   1 |     4
  \    |    / \
 5 \   | 3 /   \ 4
    \  |  /     \
       3 -------- 5
            6

Dijkstra - Find 'shortest path' tree for graph
or all the shortest paths between each node
and the start node

Find distance between each node and start node by 
checking the distance of every neighboring node.

1. Initiate total_distance dictionary to record every node's distance from the start node by setting the start node as zero and other nodes as infinity.

2. From the start node find the distance for each neighboring node.

3. Add the neighboring node's distance to the previous node's (ie, start node) distance (ie, zero) to find the new distance.

4. If new distance is shorter than the existing distance (ie, infinity) then replace this new distance as the neighboring node's distance from the start node.

5. Also record the parent in the previous_node dictionary if the new distance of the neighboring node is shorter than the existing distance.

6. Add this neighboring node to the queue to repeat the process build the total distance of every node in the graph from the start node.

7. After checking all the neigboring nodes add the start node to the visited set.

8. Repeat for all remaining nodes by using the while loop to pop the next neighboring node from the queue to find the distance of its neighbors.

9. Add this distance to the existing distance of the popped node if the distance is shorter and replace the new distance as the distance of the neighboring node in the total_distance dictionary.

10. Record the popped node as the parent of the neighboring node with the shorter distance in the previous_node dictionary.

11. Add the neighboring node to the stack to repeat. 

12. After checking all the neighbors of the popped node then add the popped node to the visited set.

The resulting total_distance and previous_nodes dictionaries make up the 'shortest-path tree' that represents the shortest paths from the start node to every node in the graph. This information can be used to calculate the shortest path between any two nodes by using the previous_nodes to subtract the total_distances to find distances between two selected nodes. 

'''

# convert routes lists into dictionary
def get_adjacency_list(edges):
  child_nodes = {}
  for node in edges:
    if node[0] in child_nodes:
      child_nodes[node[0]].append((node[1],node[2]))
    else:
      child_nodes[node[0]] = [(node[1],node[2])]
  return child_nodes

graph = get_adjacency_list(routes)
# print(f"graph: {graph}")
start = 1

import sys
from collections import deque

# https://www.youtube.com/watch?v=FSm1zybd0Tk
def get_dijkstra(graph, start):
  # initiate
  total_distance = {}
  prev_nodes = {}
  queue = deque()
  visited = set()
  infinity = sys.maxsize

  # set start node distance to zero
  total_distance[start] = 0
  # initiate queue with start node
  queue.append(start)

  # set distances of remaining nodes to maxvalue
  for node in graph:
    if node != start:
      total_distance[node] = infinity
  
  while queue:
    # pop FIFO to conduct a BFS traversal
    current = queue.popleft()
    # check if current node already visited
    if current not in visited:
      # find the distance of neighboring nodes
      for neighbor in graph[current]:
        # add neighbor distance to extend current node distance
        check_path = total_distance[current] + neighbor[1]
        # check if new distance is new shortest distance
        if check_path < total_distance[neighbor[0]]:
          # replace new distance if shorter than current distance
          total_distance[neighbor[0]] = check_path
          # record previous node as current parent node
          prev_nodes[neighbor[0]] = current
          # add neighbor to queue
          queue.append(neighbor[0])
    # after checking all neighbors add current node to visitedj
    visited.add(current)
  
  results = []
  results.append(total_distance)
  results.append(prev_nodes)
  print(f"visited: {visited}")
  return results
  
print(get_dijkstra(graph, start))
  