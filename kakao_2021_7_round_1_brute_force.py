'''
NOT WORKING - NEED TO USE DYNAMIC PROGRAMMING TO SOLVE

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 7

'''


#         1
#        /|\
#       3 5 9
#        /|  \
#       4 10  7
#         /|\
#        2 6 8  


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


def get_teams(links):
  teams = {}
  for employee in links:
    if employee[0] in teams:
      teams[employee[0]].append(employee[1])
    else:
      teams[employee[0]] = [employee[1]]

  teams_list = []
  for key, val in teams.items():
    teams_list.append([key]+ val)

  teams_invert = {}
  for child in links:
    if child[1] in teams_invert:
      teams_invert[child[1]].append(child[0])
    else:
      teams_invert[child[1]] = child[0]  
  for node in teams_invert:
    add_list = []
    if node in list(teams.keys()):
      print(f"teams[{node}]: {teams[node]}")
      print(f"node: {node}")
      print(f"node group: {teams[node]}")
      print(f"leader: {teams_invert[node]}")
      print(f"check: {teams[5]}")
      print(f"leader group[{teams_invert[node]}]: {teams[teams_invert[node]]}")
      add_list.append(teams_invert[node])
      for n in teams[teams_invert[node]]:
        if n != node:
          print(f"n: {n}")
          add_list.append(n)
      print(f"add_list: {add_list}")
      
      teams[node] += add_list
      print(f"teams[{node}]: {teams[node]}")
      print("")
      
  
  return teams, teams_list, teams_invert


def find_overlap(teams_dict,teams):
  result = []
  for key in teams_dict.keys():
    nresult = []
    for team in teams:
      if key in team:
        nresult.extend(team)
    result.append(nresult)
  return result

# FIND EMPLOYEE COMBINATIONS (IGNORE OVERLAP)
  
# https://stackoverflow.com/questions/71081437/how-to-generate-combinations-of-elements-of-different-lists
def find_teams_recursive(teams,teams_list,teams_invert):
  if len(teams_list) == 0:
    return [[]]
  result = []  
  groups = find_teams_recursive(teams,teams_list[1:],teams_invert)
  for x in teams_list[0]:
    # print(f"x: {x}")
    for y in groups:
      # print(f"y: {y}")
      if x not in y:
        # *y accepts any number of remaining values in teams_list[0]
        # print(f"[x, *y]: {[x, *y]}")
        result.append([x, *y])
        # print(f"result: {result}")
        
  return result

# https://stackoverflow.com/questions/37348906/convert-this-single-line-nested-for-loop-to-multi-line-in-python
# iterative expands 'list comprehension' of itertools production function
def find_teams_iterative(teams_list):
  if len(teams_list) == 0:
    return [[]]
  result = [[]]
  for team in teams_list:
    nresult = []
    for x in result:
      for y in team:
        if y not in x:
        # print(f"x+[y]: {x+[y]}")
          nresult.append(x+[y])
    result = nresult
  return result

# itertools product function is a generator that uses 'list comprehension'
# https://docs.python.org/3/library/itertools.html#itertools.product
def generate_teams(teams):
  result = [[]]
  for team in teams:
    # list comprehension
    result = [x+[y] for x in result for y in team]
  for prod in result:
    yield prod

def find_sales(team_combo,sales,overlap):
  team_sales = 0
  total_sales = []
  for team in team_combo:
    for employee in team:
      team_sales += sales[employee-1]
    total_sales.append(team_sales)
    print(f"sales: {total_sales}")

def invite_employees(sales, links):
  root = 1
  teams = get_teams(links)
  print(f"teams_dict: {teams}")
  teams = convert_teams_to_list(teams_dict)
  print(f"teams: {teams}")
  overlap = find_overlap(teams_dict, teams)
  # print(f"overlap: {overlap}")
    
  team_combos = find_teams_recursive(0,teams)
  # team_combos = find_teams_iterative(teams,overlap)
  # team_combos = list(generate_teams(teams))
  
  print(f"team_combos: {team_combos}")
  
  # find_sales(team_combos,sales,overlap)
  
  return None


def problem(**kwargs):
  sales = kwargs["sales"]
  links = kwargs["links"]
  
  root = 1
  teams, teams_list, teams_invert = get_teams(links)
  print(f"teams: {teams} teams_list: {teams_list} teams_invert: {teams_invert}")
  combos = find_teams_recursive(teams,teams_list,teams_invert)
  # combos = find_teams_iterative(teams_list)
  # print(f"combos: {combos}")
  
  # print(f"teams_dict: {teams_dict}")
  # teams = convert_teams_to_list(teams_dict)
  # print(f"teams: {teams}")
  # overlap = find_overlap(teams_dict, teams)
  # print(f"overlap: {overlap}")
    
  # team_combos = find_teams_recursive(root,teams)
  # team_combos = find_teams_iterative(teams,overlap)
  # team_combos = list(generate_teams(teams))
  
  # print(f"team_combos: {team_combos}")
  
  # find_sales(team_combos,sales,overlap)
  
  return None

for test_index in range(len(expected_results)): 
  if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")