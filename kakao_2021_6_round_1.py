'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 6

'''

parameters = [
  {
    "board": [
      [1,0,0,3],
      [2,0,0,0],
      [0,0,0,2],
      [3,0,1,0]
    ],
    "r": 1,
    "c": 0
  },{
    "board": [
      [3,0,0,2],
      [0,0,1,0],
      [0,1,0,0],
      [2,0,0,3]
    ],
    "r": 0,
    "c": 1 
  }
]

expected_results = [
  14,
  16
]


from collections import deque
import copy

def find_ctrl_moves(cur):
  r = cur[0]
  c = cur[1]
  board = cur[2]
  
  rCtrl = []
  cCtrl = []
  # up
  upRow = 0
  upCol = 0
  for up in range(r-1,-1,-1):
    upRow = 0-r
    upCol = 0
    if board[up][c] != 0:
      upRow = up-r
      upCol = 0
      break
  # print(f"up: {upRow}")
  rCtrl.append(upRow)
  cCtrl.append(upCol)
  # forward
  fdRow = 0
  fdCol = 0
  for fd in range(c+1,len(board[r])):
    fdRow = 0
    fdCol = len(board[r])-1-c
    if board[r][fd] != 0:
      fdRow = 0
      fdCol = fd-c
      break
  # print(f"fd: {fdCol}")
  rCtrl.append(fdRow)
  cCtrl.append(fdCol)
  # down
  dnRow = 0
  dnCol = 0
  for dn in range(r+1,len(board)):
    dnRow = len(board)-1-r
    dnCol = 0
    if board[dn][c] != 0:
      dnRow = dn-r
      dnCol = 0
      break
  # print(f"dn: {dnRow}")
  rCtrl.append(dnRow)
  cCtrl.append(dnCol)
  # back
  bkRow = 0
  bkCol = 0
  for bk in range(c-1,-1,-1):
    # print(f"BK: {bk}")
    bkRow = 0
    bkCol = 0-c
    if board[r][bk] != 0:
      bkRow = 0
      bkCol = bk-c
      break
  # print(f"bk: {bkCol}")
  rCtrl.append(bkRow)
  cCtrl.append(bkCol)

  return rCtrl,cCtrl


def bfs(board,r,c):
  queue = deque([(r,c,board,None,None,[(r,c)],0)])
  visited = []
  
  while queue:
    
    # visit the current state
    cur = queue.popleft()
    r,c,board,faceup_r,faceup_c,path,count = cur
    state = (r,c,board,faceup_r,faceup_c)
    
    # check to see if we've already visited this state (i.e. check for cycles)
    if state not in visited:
      
      # check to see if we hit the goal state
      all_zeros = True
      for row in board:
        for square in row:
          if square != 0:
            all_zeros = False
            break
      if all_zeros:
        return path,count

      # next states for the movement moves
      rCtrl, cCtrl = find_ctrl_moves(state)
      dy = [-1,0,1,0] + rCtrl
      dx = [0,1,0,-1] + cCtrl      
      for i in range(8):
        rr = r + dy[i]
        cc = c + dx[i]
        
        rows = len(board)
        cols = len(board[0])
        if (rr < 0 or cc < 0):
          continue
        if (rr >= rows or cc >= cols):
          continue
        
        next = (rr,cc,board,faceup_r,faceup_c,path+[(rr,cc)],count+1)
        queue.append(next)
      
      # next states for the enter move
      if board[r][c] != 0:
        if faceup_r is not None and faceup_c is not None:
          if board[r][c] == board[faceup_r][faceup_c]:
            new_board = copy.deepcopy(board)
            new_board[r][c] = 0
            new_board[faceup_r][faceup_c] = 0
            next = (r,c,new_board,None,None,path+['Enter'],count+1)
          else:
            next = (r,c,board,None,None,path+['Enter'],count+1)
        else:
          next = (r,c,board,r,c,path+['Enter'],count+1)
        queue.append(next)
      
      # finished visiting the current state
      visited.append(state)

# def problem(**kwargs):
#   board = kwargs["board"]
#   r = kwargs["r"]
#   c = kwargs["c"]
#   from collections import deque
#   import copy
#   queue = deque([(board,r,c,-1,-1,[])])
#   visited = []
#   while True:
#     board,r,c,faceup_r,faceup_c,moves = queue.popleft()
#     if (board,r,c,faceup_r,faceup_c) not in visited:
#       if is_end_state(board):
#         return len(moves)
#       for move in get_valid_moves(board,r,c):
#         next_board = copy.deepcopy(board)
#         next_moves = moves.copy()
#         next_board,next_r,next_c,next_faceup_r,next_faceup_c = get_next_state(next_board,r,c,faceup_r,faceup_c,move)
#         next_moves.append((move,next_board,next_r,next_c,next_faceup_r,next_faceup_c))
#         queue.append((next_board,next_r,next_c,next_faceup_r,next_faceup_c,next_moves))
#       visited.append((board,r,c,faceup_r,faceup_c))

def problem(**kwargs):
  board = kwargs["board"]
  r = kwargs["r"]
  c = kwargs["c"]

  path,count = bfs(board,r,c)
  print(f"path: {path}")
  return count

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")



