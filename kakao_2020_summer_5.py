'''

kakao 2020 summer intern test

https://tech.kakao.com/2020/07/01/2020-internship-test/

Problem 5

'''

parameters = [
  {
    "n": 9,
    "path": [
      [0,1],
      [0,3],
      [0,7],
      [8,1],
      [3,6],
      [1,2],
      [4,7],
      [7,5]
    ],
    "order": [
      [8,5],
      [6,7],
      [4,1]
    ]
  },{
    "n": 9,
    "path": [
      [8,1],
      [0,1],
      [1,2],
      [0,7],
      [4,7],
      [0,3],
      [7,5],
      [3,6]
    ],
    "order": [
      [4,1],
      [5,2]
    ]
  },{
    "n": 9,
    "path": [
      [0,1],
      [0,3],
      [0,7],
      [8,1],
      [3,6],
      [1,2],
      [4,7],
      [7,5]
    ],
    "order": [
      [4,1],
      [8,7],
      [6,5]
    ]
  }
]

expected_results = [
  True,
  True,
  False
]


from collections import deque

# for brute force method
# build undirected graph of overall tree
def get_adjacency_list(path):
  child_nodes = {}
  for node in path:
    if node[0] in child_nodes:
      child_nodes[node[0]].append(node[1])
    else:
      child_nodes[node[0]] = [node[1]]
    # assume undirected graph
    if node[1] in child_nodes:
      child_nodes[node[1]].append(node[0])
    else:
      child_nodes[node[1]] = [node[0]]
  return child_nodes

# set up reverse order dictionary of required nodes
# for brute force method for quick lookup of required nodes
def get_required(order):
  required = {}
  for node in order:
    if node[1] in required:
      required[node[1]].append(node[0])
    else:
      required[node[1]] = node[0]
  return required

# cycle check method
# create directed graph from undirected graph
# that also includes required order nodes
# (ie, nodes that must be visited first
# before going to the next node)
def get_visit_first(root, tree, order):
  stack = [root]
  previous = [0]
  # convert order list into required dictionary
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
  # add required nodes in list of children
  for node in order:
    if node[0] in required:
      required[node[0]].append(node[1])
  return required

# use state traversal to check if all nodes visited
def get_brute_force(n, root, links, required):
  # set() used to store state for check against set() used for
  # visited nodes because order of visiting nodes does not matter
  # (otherwise list() and permutations should be used if order matters)
  state = set([root])
  stack = deque([(state, links[root])])
  visited = set()
  while stack:
    state, frontier = stack.pop()
    print(f"state: {state}")
    # input()
    # if all nodes visited then return True
    if len(visited) == n:
      return True
    for next in frontier:
      if next not in visited:
        # check order requirements
        if next in required:
          # check if required order traversed 
          # before adding next node to stack
          if required[next] in state:
            next_state = state.copy()
            next_state.add(next)
            next_next = []
            for frontier in next_state:
              next_next += links[frontier]
            next_frontier = []
            for node in next_next:
              if node not in next_state:
                next_frontier.append(node)
            stack.append((next_state, next_frontier))
          # if next node does not meet order requirement 
          # then skip node and continue to next node
          else:
            continue
        # if next_node not in required order 
        # then just add to stack
        else:
          next_state = state.copy()
          next_state.add(next)
          next_next = []
          for frontier in next_state:
            next_next += links[frontier]
          next_frontier = []
          for node in next_next:
            if node not in next_state:
              next_frontier.append(node)
          stack.append((next_state, next_frontier))
    visited.update(state)
  return False

# check state (ie, sequence of nodes) or 'path' 
# until end of 'path' and dfs search backtracks 
def get_cycles(root, visit_first):
  stack = [[root]]  # [ [root] ]  # state = sequence of nodes (path) instead of a single node
  while stack:
    state = stack.pop()
    print(f"backtrack {state}")
    for next in visit_first[state[-1]]:
      # if node already in state then cycle
      # exists and return False
      if next in state:
        return False
      next_state = state.copy()
      next_state.append(next)
      stack.append(next_state)
  return True
      

def problem(**kwargs):
  n = kwargs["n"]
  path = kwargs["path"]
  order = kwargs["order"]
  # root given in text of problem
  root = 0

  # build undirected graph
  tree = get_adjacency_list(path)
  # print(f"tree: {tree}")
  
  # find reverse index of required nodes
  required = get_required(order)
  # print(f"required: {required}")

  # convert undirected graph to directed graph 
  # to find parents and required nodes 
  # (ie, nodes that need to be visited first)
  visit_first = get_visit_first(root, tree, order)
  # print(f"visit_first: {visit_first}")

  # visit first solution 
  # (ie, check for cycles)
  return get_cycles(root, visit_first)
  
  # brute force solution 
  # (ie, check all possible paths)
  # return get_brute_force(n, root, tree, required)


for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

