'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 7

Example 2-1

MINI-MAX

A starts [1,0]
B starts [1,2]
1  1  1
A  0  B
1  1  1

A moves [0,0]
A  1  1
0  0  B
1  1  1

B moves [2,2]
A  1  1
0  0  0
1  1  B

A moves [0,1]
0  A  1
0  0  0
1  1  B

B moves [2,1]
0  A  1
0  0  0
1  B  0

A moves [0,2]
0  0  A
0  0  0
1  B  0

B moves [2,0]
0  0  A
0  0  0
B  0  0

A loses and B wins in 6 total moves so returns 6

Example 2-2

A starts [1,0]
B starts [1,2]
1  1  1
A  0  B
1  1  1

A moves [0,0]
A  1  1
0  0  B
1  1  1

B moves [0,2]
A  1  B
0  0  0
1  1  1

A moves [0,1]
0  A  B
0  0  0
1  1  1

B moves [0,1]
0  A/B  0
0   0   0
1   1   1

A loses and B wins in 4 total moves so returns 4

'''

boards = [
  [
    [1,1,1],[1,1,1],[1,1,1]
  ],
  [
    [1,1,1],[1,0,1],[1,1,1]
  ],
  [
    [1,1,1,1,1]
  ],
  [
    [1]
  ]
]

alocs = [
  [1,0],
  [1,0],
  [0,0],
  [0,0]
]

blocs = [
  [1,2],
  [1,2],
  [0,4],
  [0,0]
]

expected_results = [
  5,4,4,0
]




# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function/
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

'''
PSEUDO CODE

function minimax(board, depth, isMaximizingPlayer):

    if current board state is a terminal state :
        return value of the board
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each move in board :
            value = minimax(board, depth+1, false)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = +INFINITY 
        for each move in board :
            value = minimax(board, depth+1, true)
            bestVal = min( bestVal, value) 
        return bestVal 

[1, 1, 1]    [1, 1, 1]
[1, 0, 1]    [A, 0, B]
[1, 1, 1]    [1, 1, 1]
loc: [1, 0]
loc: [1, 2]
aloc: [2, 0]

[1, 1, 1]    [1, 1, 1]
[0, 0, 1]    [0, 0, B]
[1, 1, 1]    [A, 1, 1]
loc: [2, 0]
loc: [1, 2]
bloc: [2, 2]

[1, 1, 1]    [1, 1, 1]
[0, 0, 0]    [0, 0, 0]
[1, 1, 1]    [0, A, B]
loc: [2, 0]
loc: [2, 2]
aloc: [2, 1]

[1, 1, 1]    [1, 1, 1]
[0, 0, 0]    [0, 0, 0]
[0, 1, 1]    [0, AB, 0]
loc: [2, 1]
loc: [2, 2]
bloc: [2, 1]

[1, 1, 1]    [1, 1, 1]
[0, 0, 0]    [0, 0, 0]
[0, 1, 0]    [0, AB, 0]
loc: [2, 1]


[1, 1, 1]    [X, X, X]
[1, 0, 1]    [A, 0, B]
[1, 1, 1]    [X, X, X]

[1, 1, 1]    [A, X, X]
[1, 0, 1]    [0, 0, B]
[1, 1, 1]    [X, X, X]



'''

def checkMoveAvailable(board, loc):
  if loc[1] < (len(board[0]) - 1) and board[loc[0]][loc[1]+1] == 1:
    return True
  if loc[1] > 0 and board[loc[0]][loc[1]-1] == 1:
    return True
  if loc[0] < (len(board) - 1) and board[loc[0]+1][loc[1]] == 1:
    return True
  if loc[0] > 0 and board[loc[0]-1][loc[1]] == 1:
    return True
  else:
    return False

def makeMove(board, cur_loc, new_loc):
  board[cur_loc[0]][cur_loc[1]] = 0
  move = [new_loc[0],new_loc[1]]
  return move

def checkValidMove(board, cur_loc, new_loc):
  if (cur_loc[0] + 1) == new_loc[0] and cur_loc[1] == new_loc[1]:
    return True
  if (cur_loc[0] - 1) == new_loc[0] and cur_loc[1] == new_loc[1]:
    return True
  if cur_loc[0] == new_loc[0] and (cur_loc[1] + 1) == new_loc[1]:
    return True
  if cur_loc[0] == new_loc[0] and (cur_loc[1] - 1) == new_loc[1]:
    return True
  else:
    return False

def getAllSquares(board):
  squares = []
  if board:
    for col in range(len(board[0])):
      for row in range(len(board)):
        loc = [row, col]
        if board[row][col] == 1:
          squares.append(loc)
  return squares

def getAllMoves(board, loc):
  moves = []
  for square in getAllSquares(board):
    if checkValidMove(board, loc, square):
      moves.append(square)
  return moves

def minimax(board, aloc, bloc, maximizingPlayer, depth, best_depth):
  print("--------------minimax--------------")
  if not checkMoveAvailable(board, aloc):
    print("base case: returning -1")
    return -1, depth-1, best_depth
  if not checkMoveAvailable(board, bloc):
    print("base case: returning 1")
    return 1, depth-1, best_depth

  if maximizingPlayer:
    bestValue = -1000
    moves = getAllMoves(board, aloc)
    print(f"amoves: {moves}")
    for move in moves:
      aloc = makeMove(board, aloc, move)
      print(f"-----a: {aloc} -----")
      print("max_board")
      for row in board:
        print(row)
      # print(f"max_board: {board}")
      value, depth, best_depth = minimax(board, aloc, bloc, False, depth+1, best_depth)
      print(f"avalue: {value} depth: {depth}")
      best_depth = max(best_depth, depth)
      bestValue = max(bestValue, value)
    return bestValue, depth-1, best_depth

  if not maximizingPlayer:
    bestValue = 1000
    moves = getAllMoves(board, bloc)
    print(f"bmoves: {moves}")
    for move in moves:
      bloc = makeMove(board, bloc, move)
      print(f"-----b: {bloc} -----")
      print("min_board")
      for row in board:
        print(row)
      # print(f"min_board: {board}")
      value, depth, best_depth = minimax(board, aloc, bloc, True, depth+1, best_depth)
      print(f"bvalue: {value} depth: {depth}")
      best_depth = max(best_depth, depth)
      bestValue = min(bestValue, value)
    return bestValue, depth-1, best_depth
  
def get_sum_of_character_moves(board, aloc, bloc):
  # encoding a and b in the board:  
    # doesn't account for a and b in the same square
    # inefficient to find a and b later
  # both solved by using aloc and bloc separately
  depth = 1
  best_depth = 0
  print("start_board:")
  for row in board:
    print(row)
  winner, depth, best_depth = minimax(board, aloc, bloc, True, depth, best_depth)
  print(f"winner: {winner} depth: {best_depth}")
  print("The total number of moves is :", best_depth)
  return best_depth

## use minimax = calculating optimal moves in adversarial games

for test_index in range(len(boards)):
  # if test_index == 1:
    board = boards[test_index]
    aloc = alocs[test_index]
    bloc = blocs[test_index]
    
    result = get_sum_of_character_moves(board,aloc,bloc)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
