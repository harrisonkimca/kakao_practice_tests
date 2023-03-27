'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 5

'''

parameters = [
  {
    "n": 5,
    "build_frame": [
      [1,0,0,1],
      [1,1,1,1],
      [2,1,0,1],
      [2,2,1,1],
      [5,0,0,1],
      [5,1,0,1],
      [4,2,1,1],
      [3,2,1,1]
    ]
  }, {
    "n": 5,
    "build_frame": [
      [0,0,0,1],
      [2,0,0,1],
      [4,0,0,1],
      [0,1,1,1],
      [1,1,1,1],
      [2,1,1,1],
      [3,1,1,1],
      [2,0,0,0],
      [1,1,1,0],
      [2,2,0,1]
    ]
  }
]

expected_results = [
  [
    [1,0,0],
    [1,1,1],
    [2,1,0],
    [2,2,1],
    [3,2,1],
    [4,2,1],
    [5,0,0],
    [5,1,0]
  ], [
    [0,0,0],
    [0,1,1],
    [1,1,1],
    [2,1,1],
    [3,1,1],
    [4,0,0]
  ]
]

# When a pole can be installed
# 1. There is a pillar under me. 2. There is a beam under me. 3. Below me is the floor.
def check_tower(bo,tower,x,y): # Can a tower stand at these (x,y) coordinates?
  if y == 2:  # If y = 2, it is true because bottom is the floor.
    return True
  if tower[y-1][x] == 1:  # There is a pillar underneath so you can stand it.
    return True
  if bo[y][x] == 1 or bo[y][x-1] == 1:    # There is a beam below.
    return True
  return False

# If beams can be installed
# 1. There is a pillar at the bottom left. 2. There is a column on the lower right. 3. There are beams on both sides.
def check_bo(bo,tower,x,y): # Whether a beam can stand at this (x,y) coordinate.
  if tower[y-1][x] == 1:  # Case 1
    return True
  if tower[y-1][x+1] == 1:    # Case 2
    return True
  if bo[y][x-1] == 1 and bo[y][x+1] == 1: # Case 3
    return True
  return False

# When towers can be deleted
# 1. If there is a tower above it, it must be able to stand on it.
# 2. If there is a beam above it, it must be able to stand on it.
def solution(n, build_frame):
  answer = []
  bo = [[0 for _ in range(n + 4)] for _ in range(n + 4)]
  tower = [[0 for _ in range(n + 4)] for _ in range(n + 4)]

  # Adding the coordinates by 2, let's free the -2 +2 operation.
  # In the case of a column, let the y-coordinate be a vertical straight line.
  # Let the x-coordinate you see be a horizontal straight line
  for frame in build_frame:
    x = frame[0] + 2
    y = frame[1] + 2
    a = frame[2]
    b = frame[3]

    if b == 1:  # When installing
      if a == 0 and check_tower(bo,tower,x,y): # If it is a column
          tower[y][x] = 1
      elif a == 1 and check_bo(bo,tower,x,y): # if seen
          bo[y][x] = 1
    else:   # When to delete
      if a == 0:  # When deleting a tower
        tower[y][x] = 0 # Try deleting it once.
        if tower[y+1][x] == 1 and not check_tower(bo,tower,x,y+1):  # If there is a tower above
            tower[y][x] = 1 # Failed to delete
            continue
        if bo[y+1][x] == 1 and not check_bo(bo, tower, x, y+1):# If the beam above is to the right
            tower[y][x] = 1  # Failed to delete
            continue
        if bo[y+1][x-1] == 1 and not check_bo(bo, tower, x-1, y+1):  # If the beam is to the left
            tower[y][x] = 1  # Failed to delete
            continue
      elif a == 1:    # When deleting a beam
        bo[y][x] = 0    # delete it once
        if tower[y][x] == 1 and not check_tower(bo,tower,x, y): # If there is a tower on the top left
            bo[y][x] = 1
            continue
        if tower[y][x+1] == 1 and not check_tower(bo,tower,x+1,y):  # If there is a tower on the top right
            bo[y][x] = 1
            continue
        if bo[y][x-1] == 1 and not check_bo(bo,tower,x-1,y):
            bo[y][x] = 1
            continue
        if bo[y][x+1] == 1 and not check_bo(bo,tower,x+1,y):
            bo[y][x] = 1
            continue

  for x in range(2, len(bo)):
    for y in range(2, len(bo)):
      if tower[y][x] == 1:
        answer.append([x - 2, y - 2, 0])
      if bo[y][x] == 1:
        answer.append([x - 2, y - 2, 1])

  return answer

def problem(**kwargs):
  n = kwargs["n"]
  build_frame = kwargs["build_frame"]

  result = solution(n, build_frame)
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

