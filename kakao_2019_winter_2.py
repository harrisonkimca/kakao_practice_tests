'''

kakao 2019 winter intern test

https://tech.kakao.com/2020/04/01/2019-internship-test/

Problem 2

'''

parameters = [
  {
    "s": "{{2},{2,1},{2,1,3},{2,1,3,4}}"
  }, {
    "s": "{{1,2,3},{2,1},{1,2,4,3},{2}}"
  }, {
    "s": "{{20,111},{111}}"
  }, {
    "s": "{{123}}"
  }, {
    "s": "{{4,2,3},{3},{2,3,4,1},{2,3}}"
  }
]

expected_results = [
  [2,1,3,4],
  [2,1,3,4],
  [111,20],
  [123],
  [3,2,4,1]
]

# The implementation of the String To Arr function took the longest time.
# There are many ways to shorten the time, but I use isfind to do it like DP.
# Time taken: 15 minutes?
def stringtoarr(inp):
  arr = []
  idx = 0
  num = []
  for c in range(len(inp)):
    if inp[c] == '{':
      continue
    elif inp[c] == '}':
      if idx != 0:
        num.append(int(inp[c - idx:c]))
        idx = 0
      if len(num) != 0:
        arr.append(num)
        num = []
    elif inp[c] == ',':
      if idx != 0:
        num.append(int(inp[c - idx:c]))
        idx = 0
    else:
      idx += 1
  return arr

def solution(s, arr):
  arr = stringtoarr(s)
  arr.sort(key=len)
  answer = []
  isfind = [0 for _ in range(100001)]
  for numarr in arr:
    for num in numarr:
      if isfind[num] == 0:
        isfind[num] = 1
        answer.append(num)
  return answer

def problem(**kwargs):
  s = kwargs["s"]

  arr = []
  result = solution(s, arr)
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

