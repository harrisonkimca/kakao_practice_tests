'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 5

'''

parameters = [
  {
    "ks": 3,
    "nums": [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
    "linkss": [
      [-1, -1],
      [-1, -1],
      [-1, -1],
      [-1, -1],
      [8, 5],
      [2, 10],
      [3, 0],
      [6, 1],
      [11, -1],
      [7, 4],
      [-1, -1],
      [-1, -1]
    ]
  }, {
    "ks": 1,
    "nums": [6, 9, 7, 5],
    "linkss": [
      [-1, -1],
      [-1, -1],
      [-1, 0],
      [2, 1]
    ]
  }, {
    "ks": 2,
    "nums": [6, 9, 7, 5],
    "linkss": [
      [-1, -1],
      [-1, -1],
      [-1, 0],
      [2, 1]
    ]
  }, {
    "ks": 4,
    "nums": [6, 9, 7, 5],
    "linkss": [
      [-1, -1],
      [-1, -1],
      [-1, 0],
      [2, 1]
    ]
  }
]

expected_results = [
  40,
  27,
  14,
  9
]

'''
ks = [
  3,
  1,
  2,
  4
]

nums = [
  [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
  [6, 9, 7, 5], 
  [6, 9, 7, 5],
  [6, 9, 7, 5]
]

linkss = [
  [
    [-1, -1],[-1, -1],[-1, -1],[-1, -1],[8, 5],[2, 10],[3, 0],[6, 1],[11, -1],[7, 4],[-1, -1],[-1, -1]
  ], [  
    [-1, -1],[-1, -1],[-1, 0],[2, 1]
  ], [
    [-1, -1],[-1, -1],[-1, 0],[2, 1]
  ], [
    [-1, -1],[-1, -1],[-1, 0],[2, 1]
  ]
]

expected_results = [
  40,
  27,
  14,
  9
]
'''

# basic code for tree traversal (not being used)
def traverse_children(root,links):  
  stack = [root]
  while stack:
    curr = stack.pop()
    for child in links[curr]:
      if child >= 0:
        stack.append(child)

# find all possible combinations to split the tree
# k is number of edges/splits per combination
def find_combinations(lst,k):                   # O(number of combinations* k times nested loop)
  combinations_list = []
  n = len(lst)
  if k > n:
    return combinations_list
  edges = list(range(k))
  combinations_list.append(edges.copy())
  while True:
    max_reached = True
    for i in reversed(range(k)):
      if edges[i] != i + n - k:
        max_reached = False
        break
    if max_reached:
      return combinations_list
    edges[i] += 1
    for j in range(i+1, k):
      edges[j] = edges[j-1] + 1
    combinations_list.append(edges.copy())
  return combinations_list

# traverse each subtree of the split to find total values
def find_value(root,num,links,combo_list):                # O(number of nodes)
  stack = [root]
  sum = num[root]
  while stack:
    curr = stack.pop()
    for child in links[curr]:
      if child >= 0 and child not in combo_list:
        sum += num[child]
        stack.append(child)
  return sum

def minimize_split(k,num,links):
  # in one pass through links, construct a dictionary that maps from nodes -> parents
  parents = {}
  for i, node in enumerate(links):              # O(number of nodes)
    if node[0] >= 0:
      parents[node[0]] = i
    if node[1] >= 0:
      parents[node[1]] = i
  print(f"parents:{parents}")

  # find the root
  for i, _ in enumerate(links):                 # O(number of nodes)
    if i not in parents:
      root = i
  print(f"root:{root}")
      
  # get the edges from links
  edges = []
  for edge in links:                            # O(number of nodes)
    if edge[0] >= 0:
      edges.append(edge[0])
    if edge[1] >= 0:
      edges.append(edge[1])
  print(f"edges:{edges}")
      
  # get all of the possible combinations of splits/edges depending on k
  combinations = find_combinations(edges,k-1)   # O(number of combinations * k) 
                                                # number of combinations = n! / (n-k)!k!
  # generate values for all possible splits
  results = []
  for split in combinations:                    # O(number of combinations)
    combo_value = []
    root_value = find_value(root,num,links,split)         # O(number of combinations * number of nodes)
    combo_value.append(root_value)
    for combo in split:                         # O(number of combinations * k)
      node_value = find_value(combo,num,links,split)      # O(k * number of nodes in subtree (nodes/k?) * number of combinations) --> THIS IS THE BOTTLE NECK
      combo_value.append(node_value)
    results.append(combo_value)

  # find the lowest max value for all possible splits
  max_value_per_split = []
  for item in results:                          # O(number of combinations)
    max_value_per_split.append(max(item))       # O(number of combinations * k)
  result = min(max_value_per_split)             # O(number of combinations)
  return result
'''
for test_index in range(len(ks)):
  # if test_index == 3:
    k = ks[test_index]
    num = nums[test_index]
    links = linkss[test_index]
    
    result = minimize_split(k,num,links)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
'''
def problem(**kwargs):
  k = kwargs["ks"]
  num = kwargs["nums"]
  links = kwargs["linkss"]

  result = minimize_split(k,num,links)
  return result

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

  