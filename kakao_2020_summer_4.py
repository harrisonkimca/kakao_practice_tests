'''

kakao 2020 summer intern test

https://tech.kakao.com/2020/07/01/2020-internship-test/

Problem 4

'''

parameters = [
  {
    "board": [
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]
  }, {
    "board": [
      [0,0,0,0,0,0,0,1],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,1,0,0],
      [0,0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0,1],
      [0,0,1,0,0,0,1,0],
      [0,1,0,0,0,1,0,0],
      [1,0,0,0,0,0,0,0]
    ]
  }, {
    "board": [
      [0,0,1,0],
      [0,0,0,0],
      [0,1,0,1],
      [1,0,0,0]
    ]
  }, {
    "board": [
      [0,0,0,0,0,0],
      [0,1,1,1,1,0],
      [0,0,1,0,0,0],
      [1,0,0,1,0,1],
      [0,1,0,0,0,1],
      [0,0,0,0,0,0]
    ]
  }
]

expected_results = [
  900,
  3800,
  2100,
  3200
]

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# (y,x)
isvisited = [[0 for _ in range(26)] for _ in range(26)]  # whether to visit
dp = [[987654321 for _ in range(26)] for _ in range(26)]
answer = 987654321


# Why does it keep running in an infinite loop?

def solution(board):
  isvisited[0][0] = 1
  isvisited[0][1] = 1
  dfs(0, 1, 0, 100, board)
  isvisited[0][1] = 0
  isvisited[1][0] = 1
  dfs(1, 0, 1, 100, board)
  return answer

def dfs(y, x, pre_dir, value, board):
  if board[y][x] == 1:
    return

  # Is it okay if I add this?
  if dp[y][x] >= value:
    dp[y][x] = value
  else:
    return

  end = len(board) - 1
  global answer

  if y == end and x == end:
    answer = min(answer, value)
    print(answer)
    return

  for direct in range(4):
    ny = y + d[direct][0]
    nx = x + d[direct][1]
    if 0 <= ny < len(board) and len(board) > nx >= 0:  # when in the map
      if isvisited[ny][nx] == 0 and board[ny][nx] == 0:
        isvisited[ny][nx] = 1
        if pre_dir == direct:  # Straight
          dfs(ny, nx, direct, value + 100, board)
        else:  # break
          dfs(ny, nx, direct, value + 600, board)
        isvisited[ny][nx] = 0

def problem(**kwargs):
  board = kwargs["board"]

  result = solution(board)
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
