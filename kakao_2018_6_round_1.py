'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 6

'''

parameters = [
  {
    "m": 4,
    "n": 5,
    "board": [
      "CCBDE",
      "AAADE",
      "AAABF",
      "CCBBF"
    ]
  },
  {
    "m": 6,
    "n": 6,
    "board": [
      "TTTANT",
      "RRFACC",
      "RRRFCC",
      "TRRRAA",
      "TTMMMF",
      "TMMTTJ"
    ]
  }
]

expected_results = [
  14,
  15
]

def solution(m, n, board):
  answer = 0
  board2 = []
  for b in board:
    board2.append(list(b))
  board = board2

  while True:
    count = 0
    pop_list = []
    # Board circuit
    for y in range(m-1):
      for x in range(n-1):
        if board[y][x] == " ":
          continue 
        if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
          count +=1
          pop_list.append((y,x))
          pop_list.append((y, x+1))
          pop_list.append((y+1, x))
          pop_list.append((y+1, x+1))         
    if count == 0:  # When there's nothing more to explode
      break

    pop_list = list(set(pop_list)) # deduplication
    answer += len(pop_list) # Add the number of blocks to be erased to the correct answer

    # clear block
    for (y,x) in pop_list:
      board[y][x] = " "
  
    # Make the blocks above fall down.
    for x in range(n):
      for y in range(m-1,-1,-1):
        if board[y][x] == " ":  # drop down
          for k in range(y, -1,-1):
            if board[k][x] != " ":
              board[y][x] = board[k][x]
              board[k][x] = " "
              break
  return answer

def problem(**kwargs):
  m = kwargs["m"]
  n = kwargs["n"]
  board = kwargs["board"]

  result = solution(m, n, board)
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

