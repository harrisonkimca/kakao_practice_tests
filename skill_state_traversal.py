from collections import deque

root = 0
n = 9
path = [
      [0,1],
      [0,3],
      [0,7],
      [8,1],
      [3,6],
      [1,2],
      [4,7],
      [7,5]
    ]

'''

    Direct Mapping

          0
       /  |  \
      1   3   7
     / \  |  / \
    8   2 6 4   5

                    Tree

                      0
         /            |            \
      (0,1)         (0,3)         (0,7)   
        |             |             |
     (0,1,8)       (0,3,1)       (0,7,1)
     (0,1,2)       (0,3,6)       (0,7,3)
     (0,1,3)       (0,3,7)       (0,7,4)
     (0,1,7)          |          (0,7,5)
        |             |             |
---------------------------------------------
    (0,1,8,2)     (0,3,1,8)     (0,7,1,8)
    (0,1,8,3)     (0,3,1,2)     (0,7,1,2)
    (0,1,8,7)     (0,3,1,6)     (0,7,1,3)
        |         (0,3,1,7)     (0,7,1,4)
        |             |         (0,7,1,5)
        |             |             |
    (0,1,2,8)     (0,3,6,1)     (0,7,3,1)
    (0,1,2,3)     (0,3,6,7)     (0,7,3,6)
    (0,1,2,7)         |         (0,7,3,4)
        |             |         (0,7,3,5)
        |             |             |
    (0,1,3,8)     (0,3,7,1)     (0,7,4,1)
    (0,1,3,2)     (0,3,7,6)     (0,7,4,3)
    (0,1,3,6)     (0,3,7,4)     (0,7,4,5)
    (0,1,3,7)     (0,3,7,5)         |
        |             |             |
        |             |         (0,7,5,1)
        |             |         (0,7,5,3)
        |             |         (0,7,5,4)
        |             |             |
---------------------------------------------
   (0,1,8,2,3)   (0,3,1,8,2)   (0,7,1,8,2)
   (0,1,8,2,7)   (0,3,1,8,6)   (0,7,1,8,3)
        |        (0,3,1,8,7)   (0,7,1,8,4)
        |             |        (0,7,1,8,5)
        |             |             |
   (0,1,8,3,2)   (0,3,1,2,8)   (0,7,1,2,8)
   (0,1,8,3,6)   (0,3,1,2,6)   (0,7,1,2,3)
   (0,1,8,3,7)   (0,3,1,2,7)   (0,7,1,2,4)
        |             |        (0,7,1,2,5)
        |             |             |
   (0,1,8,7,2)   (0,3,1,6,8)   (0,7,1,3,8)
   (0,1,8,7,3)   (0,3,1,6,2)   (0,7,1,3,2)
   (0,1,8,7,4)   (0,3,1,6,7)   (0,7,1,3,6)
   (0,1,8,7,5)        |        (0,7,1,3,4)
        |             |        (0,7,1,3,5)
        |             |             |
        |        (0,3,1,7,8)   (0,7,1,4,8)
        |        (0,3,1,7,2)   (0,7,1,4,2)
        |        (0,3,1,7,6)   (0,7,1,4,3)
        |        (0,3,1,7,4)   (0,7,1,4,5)
        |        (0,3,1,7,5)        |
        |             |             |
        |             |        (0,7,1,5,8)
        |             |        (0,7,1,5,2)
        |             |        (0,7,1,5,3)
        |             |        (0,7,1,5,4)
        |             |             |
   (0,1,2,8,3)   (0,3,6,1,8)   (0,7,3,1,8)
   (0,1,2,8,7)   (0,3,6,1,2)   (0,7,3,1,2)
        |        (0,3,6,1,7)   (0,7,3,1,6)
        |             |        (0,7,3,1,4)
        |             |        (0,7,3,1,5)
        |             |             |
   (0,1,2,3,8)   (0,3,6,7,1)   (0,7,3,6,1)
   (0,1,2,3,6)   (0,3,6,7,4)   (0,7,3,6,4)
   (0,1,2,3,7)   (0,3,6,7,5)   (0,7,3,6,5)
        |             |             |
   (0,1,2,7,8)        |        (0,7,3,4,1)
   (0,1,2,7,3)        |        (0,7,3,4,6)
   (0,1,2,7,4)        |        (0,7,3,4,5)
   (0,1,2,7,5)        |             |        
        |             |        (0,7,3,5,1)
        |             |        (0,7,3,5,6)
        |             |        (0,7,3,5,4)
        |             |             |
   (0,1,3,8,2)   (0,3,7,1,8)   (0,7,4,1,8)
   (0,1,3,8,6)   (0,3,7,1,2)   (0,7,4,1,2)
   (0,1,3,8,4)   (0,3,7,1,6)   (0,7,4,1,3)
   (0,1,3,8,5)   (0,3,7,1,4)   (0,7,4,1,5)
        |        (0,3,7,1,5)        |
        |             |             |
   (0,1,3,2,8)   (0,3,7,6,1)   (0,7,4,3,1)
   (0,1,3,2,6)   (0,3,7,6,4)   (0,7,4,3,6)
   (0,1,3,2,4)   (0,3,7,6,5)        |
   (0,1,3,2,5)        |             |
        |             |             |
   (0,1,3,6,8)   (0,3,7,4,1)   (0,7,4,5,1)
   (0,1,3,6,2)   (0,3,7,4,6)   (0,7,4,5,3)
   (0,1,3,6,7)   (0,3,7,4,5)        |
        |             |             |
   (0,1,3,7,8)   (0,3,7,5,1)        |
   (0,1,3,7,2)   (0,3,7,5,6)        |
   (0,1,3,7,6)   (0,3,7,5,4)        |
   (0,1,3,7,4)        |             |
   (0,1,3,7,5)        |             |
        |             |             |
        |             |        (0,7,5,1,8)
        |             |        (0,7,5,1,2)
        |             |        (0,7,5,1,3)
        |             |        (0,7,5,1,4)
---------------------------------------------
        .             .             .
        .             .             .
        .             .             .

'''

# build undirected graph of overall tree
def get_adjacency_list(path):
  frontier = {}
  for node in path:
    if node[0] in frontier:
      frontier[node[0]].append(node[1])
    else:
      frontier[node[0]] = [node[1]]
    # assume undirected graph
    if node[1] in frontier:
      frontier[node[1]].append(node[0])
    else:
      frontier[node[1]] = [node[0]]
  return frontier

# create directed graph (ie, parent child edges)
def get_visit_first(root, tree):
  stack = [root]
  previous = [0]
  # required nodes act as parent nodes in tree
  required = {}
  # convert undirected graph into directed
  # graph by excluding parent nodes
  while stack:
    cur = stack.pop()
    for next in tree[cur]:
      if cur not in required:
        required[cur] = []
      if next not in previous:
        if cur in required:
          required[cur].append(next)
        stack.append(next)
        previous.append(next)
  return required
  
# build a tree with nodes representing different states
# or groups of nodes and not just mapping of edges/nodes
  
# *** find path to visit all nodes (no order) or ***
# *** verify whether all nodes visited ***
def state_traversal_no_order(root, links):
  # initiate stack with state and frontier 
  # use set() for state to be able to compare to visited set()
  state = set([root])
  stack = deque([(state, links[root])])
  # use set() for visited when sequence of nodes does not matter
  visited = set()
  while True:
    # pop from stack (LIFO) fo DFS traversal
    state, frontier = stack.pop()
    # INSERT CHECK HERE (EARLY TERMINATION):
    # IF CHECK:
      # RETURN TRUE
    # terminate while loop if all nodes visited
    if len(visited) == len(links):
      return visited
    # find next_next_nodes of next_nodes
    # to build the next_frontier of the next_state
    for next in frontier:
      # use visited set to prevent duplicate states
      if next not in visited:
        next_state = state.copy()
        # add next node to the state to create the next_state
        next_state.add(next)
        # build the next_frontier
        next_next = []
        # add children of the new node added to the new state
        for frontier in next_state:
          # add new children to existing frontier...
          next_next += links[frontier]
        # ...then remove parent nodes to create the next_frontier 
        next_frontier = []
        for node in next_next:
          if node not in next_state:
            next_frontier.append(node)
        # add the next_state and next_frontier to the stack
        stack.append((next_state, next_frontier))
    # add state to visited set()
    visited.update(state)
  # RETURN FALSE IF CHECK NOT HIT
  # RETURN FALSE
  
# *** find path to visit all permutations of nodes ***
def state_traversal_permutation(root,links):
  # initiate stack with state and frontier 
  # (all child nodes of nodes in state)
  stack = deque([([root], links[root])])
  path = []
  while stack:
    # pop from stack (LIFO) fo DFS traversal
    state, frontier = stack.pop()
    # INSERT CHECK HERE (EARLY TERMINATION):
    # IF CHECK:
      # RETURN
    # add full traversals to path
    if len(state) == len(links):
      path.append(state)
      # print(f"state: {state}")
      # input()
    # find next_next_nodes of next_nodes
    # to build the next_frontier of the next_state
    for next in frontier:
      next_state = state.copy()
      # add next node to the state to create the next_state
      next_state.append(next)
      # build the next_frontier
      next_next = []
      # add children of the new node added to the new state
      for frontier in next_state:
        print(f"frontier: {frontier}")
        # add new children to existing frontier...
        next_next += links[frontier]
      # ...then remove parent nodes to create the next_frontier 
      next_frontier = []
      for node in next_next:
        if node not in next_state:
          next_frontier.append(node)
      # add the next_state and next_frontier to the stack
      stack.append((next_state, next_frontier))
  # RETURN FALSE IF CHECK NOT HIT
  return path

links = get_adjacency_list(path)
print(f"links: {links}")
tree = get_visit_first(root, links)
print(f"tree: {tree}")
# permutations = state_traversal_permutation(root, links)
# print(f"permutations: {permutations}")
visited = state_traversal_no_order(root, links)
print(f"path: {visited}")
