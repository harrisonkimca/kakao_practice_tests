
info = [
  0,0,1,1,1,0,1,0,1,0,1,1
]

edges = [
  [0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[ 6,9],[9,10]
]

#           0
#        /     \
#       1       2
#      / \     / \
#     3   4   5   6 
#    /     \       \
#   7       8       9
#                    \
#                    10
#
# {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [7], 4: [8], 6: [9], 9: [10]}

# iterative/recursive implementation 
# https://gist.github.com/thawsitt/87069512d39424696a2b1b60a3ed4262

def get_adjacency_list(edges):
  child_nodes = {}
  for node in edges:
    if node[0] in child_nodes:
      child_nodes[node[0]].append(node[1])
    else:
      child_nodes[node[0]] = [node[1]]
  return child_nodes

#dfs iterative version using while loop/stack
def dfs_simple(node,links):
  # 'recursion' by deferring nodes to stack
  stack = [root]
  visited = set()
  path = []
  while stack:
    # dfs pops from back of stack
    cur = stack.pop()
    print(f"cur: {cur}")
    path.append(cur)
    if cur in links and cur not in visited:
      for next_node in links[cur]:
        stack.append(next_node)
        print(f"stack: {stack}")
      visited.add(cur)
  return path


# dfs using discovered (visited) list
# https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python
def dfs_discover(root,links):
  discovered = [root]
  stack = [root]
  while stack:
    # ONLY READ from stack
    node = stack[-1]
    print(f"node: {node}")
    print(f"stack: {stack}")
    # add node to discovered list
    if node not in discovered:
      discovered.append(node)
    pop = True
    # check node to avoid index error
    if node in links:
      # loop through children of current node and
      # if not visited then add to stack and
      # disengage pop (allows stack to drill down
      # current subtree until no child nodes)
      # when no more children then while loop skips
      # this section (pop stays activated) and pops
      # nodes off the stack to backtrack 
      for next_node in links[node]:
        if next_node not in discovered:
          stack.append(next_node)
          pop = False
          break
    # while loop pops off the stack until node
    # backtracks to node with more than one child
    # to allow for loop to move to the next subtree
    if pop:
      # REMOVE from the stack
      stack.pop()
  # print(f"path: {discovered}")
  return discovered

  
# recursive dfs with added depth tracker
def dfs_recursive(node,links,depth=0,path=None):
  if path is None:
    path = []
  path.append(node)
  tab_depth = "\t"*depth
  print(f"{tab_depth}visiting {node}")
  if node in links:
    depth += 1
    for next in links[node]:
      # print(f"next: {next} links: {links[node]}")
      depth,path = dfs_recursive(next,links,depth,path)
    depth -= 1
  # else:
      # no more children (end of subtree)
  return depth,path


# reverse dfs traversal using recursion
# order reversed by printing nodes AFTER the recursion
def simple_reverse_dfs(node,links):
  if node is None:
    return None
  if node in links:
    print(f"links[{node}]: {links[node]}")
    for next in links[node]:
      simple_reverse_dfs(next,links)
  # printing after recursion reverses order of nodes
  print(f"node: {node}")
  return node

# reverse dfs using recursion with added path tracker
# order reversed by appending nodes to path AFTER recursion
# parent nodes (nodes with children) printed just after for_loop
# depth represented by tab_depth for each level
def reverse_dfs(node,links,depth=0,path=None):
  if path is None:
    path = []
  # tab_depth set according to depth of node
  tab_depth = "\t"*depth
  if node in links:
    # depth incremented at start of each subtree
    depth += 1
    for next in links[node]:
      depth,path = reverse_dfs(next,links,depth,path)
    # depth decremented to reset for next substree
    depth -= 1
    # parent nodes (nodes with children) printed here
    print(f"leader: {node}")
  # nodes added after recursion to reverse order
  path.append(node)
  print(f"{tab_depth}visiting {node}")
  return depth,path


# reverse level dfs using recursion that groups nodes
# in each level in a dictionary from bottom up using depth tracker
# also returns max_depth to loop through dict keys
def reverse_level(node,links,depth=0,max_depth=0,levels=None):
  if levels is None:
    levels = {}
  # tab_depth set according to depth of node
  tab_depth = "\t"*depth
  if node in links:
    # depth incremented at start of each subtree
    depth += 1
    for next in links[node]:
      depth,max_depth,levels = reverse_level(next,links,depth,max_depth,levels)
    # depth decremented to reset for next substree
    depth -= 1
    # can print parent nodes (nodes with children) here
    # print(f"depth: {depth} leader: {node}")
  # nodes added to dict according to level AFTER recursion (reverse order)
  if depth in levels:
    levels[depth].append(node)
  else:
    levels[depth] = [node]
  # set max_level
  if depth > max_depth:
    max_depth = depth
  # print in reverse order with tab_depth indicating levels
  print(f"{tab_depth}visiting {node}")
  return depth,max_depth,levels


links = get_adjacency_list(edges)
print(f"links: {links}")
root = 0
print(f"path: {dfs_simple(0,links)}")
# print(f"discovered: {dfs_discover(0,links)}")
# depth,path = dfs_recursive(0,links)
# print(f"path: {path}")

# simple_reverse_dfs(root,links)
# depth,path = reverse_dfs(root,links)
# print(f"path: {path}")

# depth,max_depth,levels = reverse_level(root,links)
# print(f"max_depth: {max_depth} levels: {levels}")


# [0, 2, 6, 9, 10, 5, 1, 4, 8, 3, 7]
# [0, 1, 3, 7, 4, 8, 2, 5, 6, 9, 10]
# [0, 1, 3, 7, 4, 8, 2, 5, 6, 9, 10]