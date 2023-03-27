root = 0

n_1 = 9

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

order_1 = [
      [8,5],
      [6,7],
      [4,1]
    ]

order_2 = [
      [4,1],
      [8,7],
      [6,5]
    ]


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

# cycling check
tree = get_adjacency_list(path)

# true = no cycle exists / false = cycle exists
visit_first_true = get_visit_first(root, tree, order_1)
print(f"visit_first_true: {visit_first_true}")

visit_first_false = get_visit_first(root, tree, order_2)
print(f"visit_first_false: {visit_first_false}")

cycling_check_true = get_cycles(root, visit_first_true)
print(f"cycling_check_true: {cycling_check_true}")

cycling_check_false = get_cycles(root, visit_first_false)
print(f"cycling_check_false: {cycling_check_false}")