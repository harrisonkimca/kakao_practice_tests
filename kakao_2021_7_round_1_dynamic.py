'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 7

'''

# test 0
#
#         1
#        /|\
#       3 5 9
#        /|  \
#       4 10  7
#         /|\
#        2 6 8  
#
# best(D) =  min(
#             minimum(A)                          -> 14 = 14
#            )
#
# best(C) =  min(
#             minimum(C) ++ best(D),             -> 17 + 14 = 31
#             leader(D)                          -> 17 = 17
#            )
#
# best(B) =  min(
#             minimum(B)                         -> 13 = 13
#            )
#
# best(A) =  min(
#             minimum(A) ++ best(B) ++ best(C),  -> 14 + 13 + 17 = 44
#             leader(B) ++ best(C),              -> 28 + 17 = 45
#             leader(C) ++ best(B) ++ best(D)    -> 19 + 13 + 14 = 46
#            )
#
#  General case (nodes B & D):
#    minimum(current_node) ++ best(nodes with children)
#  Check overlap cases (nodes C & A):
#    leader(nodes with children) 
#        ++ best(other nodes with children)
#        ++ best(children of children with children)
#
# test 1
#
#         1
#        / \
#       2   4
#      / \
#     3   5
#
# test 2
#
#         1
#        / \
#       2   4
#      / \
#     3   5
#
# test 3
#
#         1
#         |
#         4
#         |
#         3
#         |
#         2

parameters = [
  {
    "sales": [14,17,15,18,19,14,13,16,28,17],
    "links": [
      [10,8],
      [1,9],
      [9,7],
      [5,4],
      [1,5],
      [5,10],
      [10,6],
      [1,3],
      [10,2]
    ]
  }, {
    "sales": [5,6,5,3,4],
    "links": [
      [2,3],
      [1,4],
      [2,5],
      [1,2]
    ]
  }, {
    "sales": [5,6,5,1,4],
    "links": [
      [2,3],
      [1,4],
      [2,5],
      [1,2]
    ]
  }, {
    "sales": [10,10,1,1],
    "links": [
      [3,2],
      [4,3],
      [1,4]
    ]
  }
]

expected_results = [
  44,
  6,
  5,
  2
]


def get_teams(root,sales,links):
  teams = {}
  for employee in links:
    if employee[0] in teams:
      teams[employee[0]]['members'].append(employee[1])
    else:
      teams[employee[0]] = {'members': [employee[1]]}
  for key in teams:
    teams[key]['minimum'] = {'node': key, 'value': sales[key-1]}
    for member in teams[key]['members']:
      if sales[member-1] < teams[key]['minimum']['value']:
        teams[key]['minimum']['value'] = sales[member-1]
        teams[key]['minimum']['node'] = member ## on the whiteboard this is called argmin
  return teams


# Use recursive DFS and teams dictionary to traverse tree
# Use teams dictionry to track information (ie, no return value):
    # - children nodes, minimum value, best value
# Keep track of depth to help with print display: 
    # - tab_depth = "\t"*depth
def dfs(node,teams,sales,depth=0): # node = A
  tab_depth = "\t"*depth
  print(f"{tab_depth}initially visiting: {node}")
  if node in teams:
    depth += 1
    for next in list(teams[node].values())[0]:
      depth = dfs(next,teams,sales,depth)
    depth -= 1
    print(f"{tab_depth}calculating for: {node}")
    # Calculate general solution: 
      # - intiate solutions list with minimum of current group
      # - add best value for all children groups
            # -> min(A) ++ best(B) ++ best(C)...
    solutions = [ # solution = list of nodes
        [teams[node]['minimum']['node']]
    ]
    for member in teams[node]['members']:
      if member in teams:
        solutions[0].extend(teams[member]['best']['nodes'])
        # Calculate overlap solutions:
          # - begin with leader of each group
          # - add best value of all other nodes with children
                # -> leader(B) ++ best(C)...
          # - add best value of all other children of children
                # -> leader(C) ++ best(B) ++ best(D)...
        leader = [member]
        for child in teams[node]['members']:
          # add other nodes with children to subtree list
          if child in teams and child not in leader:
            leader.extend(teams[child]['best']['nodes'])
        # add children of children nodes to subtree list
        for child_of_child in teams[member]['members']:
          if child_of_child in teams:
            leader.extend(teams[child_of_child]['best']['nodes'])
        solutions.append(leader)
    print(f"{tab_depth}node: {node} solutions: {solutions}")
    # Set best nodes/total_value as minimal value of solutions list
    min_value = float('inf')
    for solution in solutions:
      solution_value = 0
      solution_nodes = []
      for n in solution:
        solution_value += sales[n-1]
        solution_nodes.append(n)
      if solution_value < min_value:
        min_value = solution_value
        teams[node]['best'] = {
          'nodes': solution_nodes,
          'total_value': solution_value
        }
  return depth


def problem(**kwargs):
  sales = kwargs["sales"]
  links = kwargs["links"]
  
  root = 1
  teams = get_teams(root,sales,links)
  # print(f"teams: {teams}")
  
  dfs(root,teams,sales)
  print(teams)

  return teams[root]['best']['total_value']

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")