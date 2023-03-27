'''

kakao 2019 winter intern test

https://tech.kakao.com/2020/04/01/2019-internship-test/

Problem 1

'''

parameters = [
  {
    "board": [
      [0,0,0,0,0],
      [0,0,1,0,3],
      [0,2,5,0,1],
      [4,2,4,4,2],
      [3,5,1,3,1]
    ],
    "moves": [
      1,
      5,
      3,
      5,
      1,
      2,
      1,
      4
    ]
  }
]

expected_results = [
  4
]

from collections import deque

def solution(board, moves):
  answer = 0
  stack = deque()
  for move in moves:
    move -= 1
    for n in range(0,len(board)):
      if board[n][move] != 0: # if you have a doll
        doll = board[n][move]
        board[n][move] = 0 # take out the doll
        stack.append(doll)  # Put the doll on the stack
        if len(stack) >= 2 and stack[-1] == stack[-2]:
          stack.pop()  # Pop two dolls
          stack.pop()
          answer += 2
        break
  return answer

# took 30 minutes for a mistake
# A stupid mistake that breaks only when the doll bursts...

def problem(**kwargs):
  board = kwargs["board"]
  moves = kwargs["moves"]

  result = solution(board, moves)
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

