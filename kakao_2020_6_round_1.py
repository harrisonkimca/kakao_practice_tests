'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 6

'''

parameters = [
  {
    "n": 12,
    "weak": [1, 5, 6, 10],
    "dist": [1, 2, 3, 4]
  }, {
    "n": 12,
    "weak": [1, 3, 4, 9, 10],
    "dist": [3, 5, 7]
  }
]

expected_results = [
  2,
  1
]


from itertools import permutations

def solution(n, weak, dist):
  L = len(weak)
  cand = []
  weak_point = weak + [w+n for w in weak]  # linearly

  for i, start in enumerate(weak):
    for friends in permutations(dist):  # permutation use
      count = 1
      position = start
      # Friend Combination Placement
      for friend in friends:
        position += friend
        # When the end point is not reached
        if position < weak_point[i+L-1]:
          count += 1  # add more friends
          # Move to the nearest location among weak points further away than the current location.
          position = [w for w in weak_point[i+1:i+L]
                      if w > position][0]
        else:  # reach end point
          cand.append(count)
          break
  return min(cand) if cand else -1

def problem(**kwargs):
  n = kwargs["n"]
  weak = kwargs["weak"]
  dist = kwargs["dist"]

  result = solution(n, weak, dist)
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

