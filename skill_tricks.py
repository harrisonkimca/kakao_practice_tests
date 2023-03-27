# print 2d array into board

board = [
      [0, 0, 0, 1, 1],
      [0, 0, 0, 1, 0],
      [0, 1, 0, 1, 1],
      [1, 1, 0, 0, 1],
      [0, 0, 0, 0, 0]
    ]  

# print board as 2D vs single-line list of lists
def print_board(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] >= 0:
        print(" ", end="")
      print(board[row][col], end="")      
    print("")

# pause loop using 'input()'
def pause_loop():
  for i in range(5, 105, 5):
    print(i)
    print("Press enter!")
    input()


print_board(board)
pause_loop()
