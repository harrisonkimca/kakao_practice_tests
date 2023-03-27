'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 7

'''

parameters = [
  {
    "board": [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,4,0,0,0],
      [0,0,0,0,0,4,4,0,0,0],
      [0,0,0,0,3,0,4,0,0,0],
      [0,0,0,2,3,0,0,0,5,5],
      [1,2,2,2,3,3,0,0,0,5],
      [1,1,1,0,0,0,0,0,0,5]
    ]
  }
]

expected_results = [
  2
]

def check_block(row, col, board):
  # horizontal
  if row < len(board)-1:
    # left-L
    if board[row][col-1] == -1 and col > 1:
      # check surrounding blocks all from same shape and not all -1's
      if (
        board[row][col-2] == 
        board[row+1][col-2] ==
        board[row+1][col-1] ==
        board[row+1][col]
      ) and board[row][col-2] > 0 and board[row+1][col-2] > 0 and board[row+1][col-1] > 0 and board[row+1][col] > 0:
        # delete shape
        board[row][col-2] = 0
        board[row][col-1] = 0
        board[row][col] = 0
        board[row+1][col-2] = 0
        board[row+1][col-1] = 0
        board[row+1][col] = 0
        # return True to increment max_block counter
        return True
        
    # right-L
    if board[row][col-1] == -1 and col > 0 and col < (len(board[row])-1):
      if (
        board[row][col+1] == 
        board[row+1][col-1] ==
        board[row+1][col] ==
        board[row+1][col+1]
      ) and board[row][col+1] > 0 and board[row+1][col-1] > 0 and board[row+1][col]> 0 and board[row+1][col+1] > 0:
        board[row][col-1] = 0
        board[row][col] = 0
        board[row][col+1] = 0
        board[row+1][col-1] = 0
        board[row+1][col] = 0
        board[row+1][col+1] = 0
        return True
    # upside-T
    if board[row][col-2] == -1 and col > 1:
      if (
        board[row][col-1] == 
        board[row+1][col-2] ==
        board[row+1][col-1] ==
        board[row+1][col]
      ) and board[row][col-1] > 0 and board[row+1][col-2] > 0 and board[row+1][col-1] > 0 and board[row+1][col] > 0:
        board[row][col-2] = 0
        board[row][col-1] = 0
        board[row][col] = 0
        board[row+1][col-2] = 0
        board[row+1][col-1] = 0
        board[row+1][col] = 0
        return True
        
  # vertical
  if row < len(board)-2:
    # left-L
    if board[row+1][col] == -1 and col > 0:
      if (
        board[row][col-1] ==
        board[row+1][col-1] ==
        board[row+2][col-1] ==
        board[row+2][col]
      ) and board[row][col-1] > 0 and board[row+1][col-1] > 0 and board[row+2][col-1] > 0 and board[row+2][col] > 0:
        board[row][col-1] = 0
        board[row][col] = 0
        board[row+1][col-1] = 0
        board[row+1][col] = 0
        board[row+2][col-1] = 0
        board[row+2][col] = 0
        return True
    # right-L
    if board[row+1][col] == -1 and col < (len(board[0])-1):
      if (
        board[row][col+1] ==
        board[row+1][col+1] ==
        board[row+2][col+1] ==
        board[row+2][col]
      ) and board[row][col+1] > 0 and board[row+1][col+1] > 0 and board[row+2][col+1] > 0 and board[row+2][col] > 0:
        board[row][col] = 0
        board[row][col+1] = 0
        board[row+1][col] = 0
        board[row+1][col+1] = 0
        board[row+2][col] = 0
        board[row+2][col+1] = 0
        return True

def print_board(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] >= 0:
        print(" ", end="")
      print(board[row][col], end="")      
    print("")

def get_max_blocks(board):
  max_blocks = 0
  finished = False # so the loop will run the first time
  # loop until no blocks can be dropped
  while not finished:
    # CHECK AT BEGINNING: toggle to end while loop
    finished = True
    for col in range(len(board[0])):
      print_board(board)
      input()
      for row in range(len(board)):
        if board[row][col] != 0:
          if row > 0:
            board[row-1][col] = -1
            # if block dropped then toggle to continue while loop
            finished = False
            # check returns True if block deleted
            check = check_block(row-1, col, board)
            # if check is True then increment max_block counter
            if check:
              max_blocks += 1
          # break if non-zero hit or non-zero at top
          break
        # falls to bottom with no non-zero
        elif row == len(board) - 1:
          board[row][col] = -1
          finished = False
          break
  return max_blocks

def problem(**kwargs):
  board = kwargs["board"]

  return get_max_blocks(board)

for test_index in range(len(expected_results)): 
  if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

