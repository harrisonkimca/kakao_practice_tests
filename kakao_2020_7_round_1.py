'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 7

'''

parameters = [
  {
    "board": [
      [0, 0, 0, 1, 1],
      [0, 0, 0, 1, 0],
      [0, 1, 0, 1, 1],
      [1, 1, 0, 0, 1],
      [0, 0, 0, 0, 0]
    ]  
  }
]

expected_results = [
  7
]


# https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/?ref=rp
def isValid(board,visited,adj,chk):
  # height/width of board to check boundaries (ie, avoid index error)
  height = len(board)
  width = len(board[0])
  # next node in tree
  a,b = adj[0]
  c,d = adj[1]
  # check cells for next node in tree
  aa,bb = chk[0]
  cc,dd = chk[1]
   
  # if cell lies out of bounds
  if (a < 0 or b < 0 or c < 0 or d < 0 or 
      a >= height or b >= width or c >= height or d >= width):
    return False
  # if cell contains 1
  if board[a][b] == 1 or board[c][d] == 1:
    return False
  # if check cell contains 1
  if board[aa][bb] == 1 or board[cc][dd] == 1:
    return False
  # if cell already visited    
  if adj in visited:
    return False
  # otherwise
  return True

# https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/?ref=rp
def bfs(board,start,end):
  # first robot location
  a,b = start[0][0]
  # second robot location 
  c,d = start[0][1]
  
  queue = [start]
  # list of lists to hold all possible paths
  path = [[start]]
  visited = [start[0]]
  # index through each path generated from bfs 
  index = 0

  while queue:
    # bfs uses queue vs stack (ie, first in first out)
    cur = queue.pop(0)
    a,b = cur[0][0]
    c,d = cur[0][1]
    count = cur[1]

    # https://onestepcode.com/graph-shortest-path-python/
    # integrated from function from above link (use of path[index] to add new paths to path list)
    current_path = path[index]
    # print(f"index: {index} current_path: {current_path}")
    # build nodes of tree as all possible states 
    # (ie, possible moves including rotations)
    for i in range(8):
      # horizontal position
      if a == c:
        # left,down,right,up,
        # cw left up, cw right down, ccw left down, ccw right up
        aCol = [0,1,0,-1,-1,0,0,-1]
        bRow = [-1,0,1,0,1,0,1,0]
        cCol = [0,1,0,-1,0,1,1,0]
        dRow = [-1,0,1,0,0,-1,0,-1]
        aaCol = [0,1,0,-1,-1,0,1,-1]
        bbRow = [-1,0,1,0,0,0,0,0]
        ccCol = [0,1,0,-1,0,1,1,-1]
        ddRow = [-1,0,1,0,0,0,0,0]
      # vertical position
      else:
        # left,down,right,up,
        # cw left up, cw right down, ccw left down, ccw right up
        aCol = [0,1,0,-1,0,1,1,0]
        bRow = [-1,0,1,0,-1,0,-1,0]
        cCol = [0,1,0,-1,-1,0,0,-1]
        dRow = [-1,0,1,0,0,1,0,1]
        aaCol = [0,1,0,-1,0,0,0,0]
        bbRow = [-1,0,1,0,-1,1,-1,0]
        ccCol = [0,1,0,-1,0,0,0,0]
        ddRow = [-1,0,1,0,-1,1,0,1]
      # each node represents a possible state of the robot
      adj = ((a + aCol[i],b + bRow[i]),(c + cCol[i],d + dRow[i]))
      # also build the checks for each possible state
      chk = ((a + aaCol[i],b + bbRow[i]),(c + ccCol[i],d + ddRow[i]))
      # increment counter
      count = cur[1] + 1
      # check each node as they are made and add to queue for bfs
      if (isValid(board,visited,adj,chk)):
        queue.append((adj,count))
        visited.append(adj)
        # add neighboring (next) nodes for each level to path list
        new_path = current_path[:] # copy existing list
        new_path.append((adj,count))
        # print(f"new_path: {new_path}")
        path.append(new_path)
        # return path when goal node reached
        if end in adj:
          return path[-1][-1][1],path[-1]
    # increment path in path list
    index += 1
  # if no end node found  
  return 0,[]


def problem(**kwargs):
  board = kwargs["board"]
  start = (((0,0),(0,1)),0)
  end = (4,4)
  

  '''
  a,b,c,d = 0,0,0,1
  print("Horizontal Move Right")
  if a == c and d+1 < len(board[c]) and board[c][d+1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b+1),(c,d+1))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Horizontal Move Right\n")

  a,b,c,d = 0,1,0,2
  print("Horizontal Move Left")
  if a == c and b-1 >= 0 and board[a][b-1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b-1),(c,d-1))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Horizontal Move Left\n")

  a,b,c,d = 0,0,1,0
  print("Vertical Move Right")
  if b == d and b+1 < len(board[a]) and d+1 < len(board[c]) and board[a][b+1] != 1 and board[c][d+1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b+1),(c,d+1))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Vertical Move Right\n")

  a,b,c,d = 0,1,1,1
  print("Vertical Move Left")
  if b == d and b-1 >= 0 and d-1 >= 0 and board[a][b-1] != 1 and board[c][d-1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b-1),(c,d-1))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Vertical Move Left\n")

  print("---------------------------------\n")
  
  print("Horizontal Move Down")
  a,b,c,d = 0,0,0,1
  if a == c and a+1 < len(board) and c+1 < len(board) and board[a+1][b] != 1 and board[c+1][d] != 1:
    old = ((a,b),(c,d))
    new = ((a+1,b),(c+1,d))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Horizontal Move Down\n")

  print("Horizontal Move Up")
  a,b,c,d = 1,0,1,1
  if a == c and a-1 >= 0 and c-1 >= 0 and board[a-1][b] != 1 and board[c-1][d] != 1:
    old = ((a,b),(c,d))
    new = ((a-1,b),(c-1,d))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Horizontal Move Up\n")

  print("Vertical Move Down")
  a,b,c,d = 0,0,1,0
  if b == d and c+1 < len(board) and board[c+1][d] != 1:
    old = ((a,b),(c,d))
    new = ((a+1,b),(c+1,d))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Vertical Move Down\n")

  print("Vertical Move Up")
  a,b,c,d = 2,0,1,0
  if b == d and a-1 >= 0 and board[a-1][b] != 1:
    old = ((a,b),(c,d))
    new = ((a-1,b),(c-1,d))
    print(f"  old: {old}\n  new: {new}\n")
  else:
    print("  None Vertical Move Up\n")

  print("---------------------------------\n")

  print("Horizontal Clockwise Left Up")
  a,b,c,d = 0,0,0,1
  if a == c and a-1 >= 0 and board[a-1][b] != 1 and board[a-1][b+1] != 1:
    old = ((a,b),(c,d))
    new = ((a-1,b+1),(c,d))
    check = (a-1,b)
    print(f"  old: {old}: check: {check}\n  new: {new}\n")
  else:
    print("  None Horizontal Clockwise Left Up\n")

  print("Horizontal Clockwise Right Down")
  a,b,c,d = 4,0,4,1
  if a == c and c+1 < len(board) and board[c+1][d] != 1 and board[c+1][d-1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b),(c+1,d-1))
    check = (c+1,d)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Horizontal Clockwise Right Down\n")

  print("Vertical Clockwise Left Up")
  a,b,c,d = 0,0,1,0
  if b == d and d-1 >= 0 and board[c][d-1] != 1 and board[a][b-1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b-1),(c-1,d))
    check = (c,d-1)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Vertical Clockwise Left Up\n")

  print("Vertical Clockwise Right Down")
  a,b,c,d = 3,4,4,4
  if b == d and b+1 < len(board[a]) and board[a][b+1] != 1 and board[c][d+1] != 1:
    old = ((a,b),(c,d))
    new = ((a+1,b),(c,d+1))
    check = (a,b+1)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Vertical Clockwise Right Down\n")

  print("---------------------------------\n")
  
  print("Horizontal C-Clockwise Left Down")
  a,b,c,d = 4,0,4,1
  if a == c and a+1 < len(board) and board[a+1][b] != 1 and board[c+1][d] != 1:
    old = ((a,b),(c,d))
    new = ((a,b+1),(c+1,d))
    check = (a+1,b)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Horizontal C-Clockwise Left Down\n")

  print("Horizontal C-Clockwise Right Up")
  a,b,c,d = 0,0,0,1
  if a == c and a-1 >= 0 and board[c-1][d] != 1 and board[a-1][b] != 1:
    old = ((a,b),(c,d))
    new = ((a-1,b),(c,d-1))
    check = (c-1,d)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Horizontal C-Clockwise Right Up\n")

  print("Vertical C-Clockwise Left Down")
  a,b,c,d = 0,0,1,0
  if b == d and d-1 >= 0 and board[a][b-1] != 1 and board[a+1][b-1] != 1:
    old = ((a,b),(c,d))
    new = ((a+1,b-1),(c,d))
    check = (a,b-1)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Vertical C-Clockwise Left Down\n")

  print("Vertical C-Clockwise Right Up")
  a,b,c,d = 3,4,4,4
  if b == d and d+1 < len(board[c]) and board[c][d+1] != 1 and board[c-1][d+1] != 1:
    old = ((a,b),(c,d))
    new = ((a,b),(c-1,d+1))
    check = (c,d+1)
    print(f"  old: {old} check: {check}\n  new: {new}\n")
  else:
    print("  None Vertical C-Clockwise Right Up\n")

  '''
  
  count,path = bfs(board,start,end)
  print(f"count: {count}")
  print(f"path: {path}")

  return count

for test_index in range(len(expected_results)): 
  if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")