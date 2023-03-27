'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 3

'''

parameters = [
  {
    "key": [
      [0, 0, 0],
      [1, 0, 0],
      [0, 1, 1]
    ],
    "lock": [
      [1, 1, 1],
      [1, 1, 0],
      [1, 0, 1]
    ]
  }
]

expected_results = [
  True
]

def generate_lock(key, lock):
  m = len(key)
  n = len(lock)
  tmp = [[0] * (2 * m - 2 + n) for _ in range(2 * m - 2 + n)]
  for y in range(m - 1, m + n - 1):
    for x in range(m - 1, m + n - 1):
      tmp[y][x] = lock[y - (m - 1)][x - (m - 1)]
  return tmp

# rotate 90 degrees
def rotate(key):
  tmp = [[0] * len(key) for _ in range(len(key))]
  for y in range(len(key)):
    for x in range(len(key)):
      tmp[x][len(key) - 1 - y] = key[y][x]
  return tmp

def solution(key, lock):
  n = len(lock)
  lock_count = 0
  for y in range(n):
    for x in range(n):
      if lock[y][x] == 0:
        lock_count += 1
  new_lock = generate_lock(key, lock)
  m = len(key)
  for _ in range(4):
    key = rotate(key)
    for start_y in range(n+m-1):
      for start_x in range(n+m-1):
        flag = True
        key_count = 0
        for ky in range(m):
          if not flag:
            break
          for kx in range(m):
            if key[ky][kx] + new_lock[start_y+ky][start_x+kx] == 2:
                flag = False
                break
            if m-1<= start_y+ky < m+n-1 and m-1 <= start_x + kx < m+n-1 and key[ky][kx] == 1:
                key_count += 1
        if flag and key_count == lock_count:
            return True
  answer = False
  return answer


def problem(**kwargs):
  key = kwargs["key"]
  lock = kwargs["lock"]

  result = solution(key, lock)
  
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

