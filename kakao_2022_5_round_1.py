'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 5

'''

# basic depth first search + sheep, wolves, nodes are part of the state + early termination whenever wolves >= sheep
# extra: try a recursive version
# stack = [(root,next_nodes, initial_sheep,initial_wolves,path)] 
# frontier = data structure holding the next possible nodes (ie, stack)

# Example 2
#
#             0
#             S
#         /       \
#        1         2
#        W         S
#      /  \       /  \
#     3    4     5    6 
#     W    W     S    W
#   /        \          \
#  7          8          9
#  S          S          W
#                         \
#                         10
#                          S
#
# dfs 0 - 1 - 3 - 7 - 4 - 8 - 2 - 5 - 6 - 9 - 10
# ans 0 - 2 - 5 - 1 - 4 - 8 - 3 - 7

# Build dfs using frontier to visit next nodes (including all possible nodes from the perspective of each node and not just child nodes). A frontier is a data structure (such as a stack) that can hold all of the next possible nodes. Next possible nodes not only include child nodes but also nodes that could be chosen to visit next. For example, from node 0's perspective its children are node 1 with the possibility of going to node 2 AND node 2 with the possibility of going to node 1. This means if the current node is 1, the frontier would include the child nodes 3 and 4 but also node 2 as another possible path and, likewise, if the current node was 2, the frontier would include the child nodes 5 and 6 as well as node 1 as another possible path. The 'state' of the current node could then be defined as the next_nodes, number of sheep and number of wolves (and path) at the current node. The current node and its state can be stored in the stack and popped from the stack for the dfs. 

# Algorithm pattern (iterative):
# 1. The algorithm begins by initiating the stack with the root node as the current node, adding the root node's children to the curr_next_nodes list (node 1 and node 2), starting the sheep and wolf count with root node's sheep (sheep = 1, wolf = 0) and using the root as the first node in the search path
# 2. The while loop traverses the tree by popping off the stack to update the cur_node, curr_next_nodes, curr_sheep, curr_wolf and path for the next set of nodes taken from the cur_node's curr_next_nodes list  
# 3. The for_loop moves through each node in the curr_next_nodes list and first checks the next_node for the early termination condition (sheep >= wolf) before copying the original curr_next_nodes list to create the (copied) next_next_nodes list (copied to prevent altering the original curr_next_nodes list). 
# 4. Each element in the curr_next_nodes list adds its state to the stack by replacing cur_node with the next_node, next_next_nodes with next_node's frontier, updating the next_node's sheep and wolf count with the next_node's sheep/wolf and adding next_node to the search path list 
# 5. NEXT_NEXT_NODE: The next_next_node list creates the frontier by adding all possible nodes or the nodes in copied next_next_node list excluding the next_node being used to replace the cur_node and any children of the next_node (only the other possible nodes if the next_node has no children)
# 6. EARLY TERMINATION CONDITION: The algorithm will try all combinations of nodes (taken as a complete set of nodes vs single nodes along a path) where sheep >= wolf and will terminate the search for additional nodes when this condition is not met

#   QUESTION: DO YOU USE FRONTIER FOR ALL DFS/BFS? OR JUST FOR THIS CASE? (IE, ALL POSSIBLE NODES AND NOT JUST THE CHILDREN?)

# Notables:
# 1. Think of the frontier as moving from one CLUSTER of next_nodes to another CLUSTER of next_nodes rather than just moving to the next set of child nodes (ie, all possible nodes + child nodes)
# 2. Naming the main variables with the CURRENT label (ie, cur_node, cur_next_node, cur_sheep and cur_wolf) and then using the .pop() and .copy() methods on the original list is a common pattern to update the variables (ie, next_node, next_next_nodes, next_sheep, next_wolf) to avoid altering the original list where the variables are taken from [can also use stack[-1] to just read the last element in the stack to set the variables and using the .pop() method only after the last element is not needed anymore]


# 0 is sheep and 1 is wolf
infos = [
  [0,0,1,1,1,0,1,0,1,0,1,1],
  [0,1,0,1,1,0,1,0,0,1,0]
]

edgess = [
  [ [0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9] ],
  [ [0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[ 6,9],[9,10] ]
]

expected_results = [
  5,
  5
]


def get_adjacency_list(edges):
  child_nodes = {}
  for node in edges:
    if node[0] in child_nodes:
      child_nodes[node[0]].append(node[1])
    else:
      child_nodes[node[0]] = [node[1]]
  return child_nodes


# dfs (iterative)
def traverse_tree_iterative(root,links,info):
  # state = (current_node,next_nodes,sheep,wolf,path)
  stack = [(root,links[root],info[root]^1,info[root],[root])]
  best_sheep = 0
  best_path = []
  count = 0
  while stack:
    # print(f"stack: {stack}")
    curr_node,curr_next_nodes,curr_sheep,curr_wolf,curr_path = stack.pop()
    for index, next_node in enumerate(curr_next_nodes):
      next_sheep = curr_sheep + (info[next_node]^1)
      next_wolf = curr_wolf + info[next_node]
      if next_sheep != next_wolf:        
        next_next_nodes = curr_next_nodes.copy()
        next_path = curr_path.copy()
        # if next_node has a child
        if next_node in links:
          next_next_nodes = (
            next_next_nodes[:index] + 
            next_next_nodes[index+1:] +
            links[next_node]
            )
        # if no child then just add
        # next_next_node (no child nodes)
        else: 
          next_next_nodes = (
            next_next_nodes[:index] + 
            next_next_nodes[index+1:])
        next_path.append(next_node)
        
        stack.append((
          next_node,
          next_next_nodes,
          next_sheep,
          next_wolf,
          next_path
        ))
        print(f"search_path: {next_path}")
  
        if next_sheep > best_sheep:
          if len(stack) > 1:
            best_path = stack[-1][-1]
          best_sheep = next_sheep
  return best_sheep, best_path


# dfs (recursive)
def dfs_recursive(links,info,state,best_sheep,best_path):
  node,nodes,sheep,wolf,path = state.pop()
  if sheep > best_sheep:
    best_sheep = sheep
    if len(path) > 1:
      best_path = path
  # loop through frontier of nodes
  for index, next in enumerate(nodes):
    next_sheep = sheep + (info[next]^1)
    next_wolf = wolf + info[next]
    if sheep != wolf:
      next_nodes = nodes.copy()
      next_path = path.copy()
      if next in links:
        # next_nodes = links[next]
        next_nodes = (
          next_nodes[:index] +
          next_nodes[index+1:] +
          links[next]
          )
      else:
        # next_nodes = []
        next_nodes = (
          next_nodes[:index] +
          next_nodes[index+1:]
        )
      next_path.append(next)
      state.append((next,next_nodes,next_sheep,next_wolf,next_path))
      print(f"search_path: {next_path}")
      # recursive call drills down each subtree until no more child nodes
      state,best_sheep,best_path = dfs_recursive(links,info,state,best_sheep,best_path)
  # return done outside of recursive call stack
  return state,best_sheep,best_path


def collect_sheep(info, edges, results):
  links = get_adjacency_list(edges)
  print(f"links: {links}")
  root = 0
  
  # iterative solution
  # best_sheep, best_path = traverse_tree_iterative(root,links,info)
  # print(f"best_sheep: {best_sheep} best_path: {best_path}")

  # recursive solution
  state = []
  best_sheep = 0
  best_path = []
  
  state.append((root,links[root],info[root]^1,info[root],[root]))
  state, best_sheep, best_path = dfs_recursive(links,info,state,best_sheep,best_path)
  print(f"best_sheep: {best_sheep} best_path: {best_path}")

  return best_sheep

for test_index in range(len(infos)):
  # if test_index == 1:
    info = infos[test_index]
    edges = edgess[test_index]
    results = expected_results[test_index]
    
    result = collect_sheep(info,edges,results)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")