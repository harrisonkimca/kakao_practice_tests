teams = [[8, 6, 2], [9, 5, 3], [7], [4, 10]]

# https://stackoverflow.com/questions/71081437/how-to-generate-combinations-of-elements-of-different-lists
def find_teams_recursive(teams):
  if len(teams) == 0:
    return [[]]
  result = []   
  groups = find_teams_recursive(teams[1:])
  for x in teams[0]:
    for y in groups:
      # *y accepts any number of remaining values in teams[0]
      # print(f"[x, *y]: {[x, *y]}")
      result.append([x, *y])
  return result

# https://stackoverflow.com/questions/37348906/convert-this-single-line-nested-for-loop-to-multi-line-in-python
# iterative expands 'list comprehension' of itertools production function
def find_teams_iterative(teams):
  if len(teams) == 0:
    return [[]]
  result = [[]]
  for team in teams:
    nresult = []
    for x in result:
      for y in team:
        print(f"x+[y]: {x+[y]}")
        nresult.append(x+[y])
    result = nresult
  return result

# itertools product function is a generator that uses 'list comprehension'
# https://docs.python.org/3/library/itertools.html#itertools.product
def product(*args, repeat=1):
  # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
  # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
  pools = [tuple(pool) for pool in args] * repeat
  result = [[]]
  for pool in pools:
      # list comprehension
      result = [x+[y] for x in result for y in pool]
      # print(f"result: {result}")
  for prod in result:
      yield tuple(prod)

def product_simplified(teams):
  result = [[]]
  for team in teams:
      # list comprehension
      result = [x+[y] for x in result for y in team]
  for prod in result:
      yield prod


# result = find_teams_recursive(teams)
result = find_teams_iterative(teams)
# result = list(product(*teams))
# result = list(product_simplified(teams))
print(f"teams: {result}")

# print generator
# print(*(product(*teams)))
