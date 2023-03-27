'''

kakao 2020 summer intern test

https://tech.kakao.com/2020/07/01/2020-internship-test/

Problem 1

'''

parameters = [
  {
    "numbers": [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
    "hand": "right"
  }, {
    "numbers": [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
    "hand": "left"
  }, {
    "numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "hand": "right"
  }
]

expected_results = [
  "LRLLLRLLRRL",
  "LRLLRRLLLRR",
  "LLRLLRLLRL"
]


# Let 1 be (1,1), 3 be (1,3), and 9 be (3,3).
def distance(now, nex):
  y_dist = abs(now[0] - nex[0])
  x_dist = abs(now[1] - nex[1])
  return y_dist + x_dist

def solution(numbers, hand):
  left = [4, 1]  # (y,x)
  right = [4, 3]
  answer = ''
  for num in numbers:
    y = int(num / 3)
    x = num % 3
    if x == 0:
      x = 3
    else:
      y += 1

    if num == 0:
      y = 4
      x = 2
    nex = [y, x]
    # print(nex)

    if num == 1 or num == 4 or num == 7:
      left = nex
      answer += 'L'
    elif num == 3 or num == 6 or num == 9:
      right = nex
      answer += 'R'
    else:
      left_dist = distance(left, nex)
      right_dist = distance(right, nex)
      # print("left dist : ",left_dist)
      # print("right dist : ",right_dist)
      if left_dist > right_dist:
        right = nex
        answer += 'R'
      elif right_dist > left_dist:
        left = nex
        answer += 'L'
      else:
        if hand == 'right':
          right = nex
          answer += 'R'
        else:
          left = nex
          answer += 'L'
    # print("left : ", left)
    # print("right : ", right)

  return answer

def problem(**kwargs):
  numbers = kwargs["numbers"]
  hand = kwargs["hand"]

  result = solution(numbers, hand)
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
