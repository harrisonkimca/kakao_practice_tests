'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 5

'''

parameters = [
  {
    "str1": "FRANCE",
    "str2": "french"
  },
  {
    "str1": "handshake",
    "str2": "shake hands"
  },
  {
    "str1": "aa1+aa2",
    "str2": "AAAA12"
  },
  {
    "str1": "E=M*C^2",
    "str2": "e=m*c^2"
  }
]

expected_results = [
  16384,
  65536,
  43690,
  65536
]

def solution(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  length1 = len(str1)
  length2 = len(str2)
  set1 = []
  set2 = []
  con_set = []
  for i in range(length1-1):
    if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z':
      set1.append(str1[i:i+2])

  for i in range(length2-1):
    if 'a' <= str2[i] <= 'z' and 'a' <= str2[i + 1] <= 'z':
      set2.append(str2[i:i + 2])

  set1_copy = set1.copy()
  set2_copy = set2.copy()
  for s1 in set1:
    if s1 in set2_copy:
      con_set.append(s1)
      set2_copy.remove(s1)
      set1_copy.remove(s1)

  union = set1_copy + set2_copy + con_set
  a1 = len(con_set)
  a2 = len(union)
  if a2 == 0:
    return 65536

  answer = float(a1) / float(a2) * 65536
  return int(answer)

def problem(**kwargs):
  str1 = kwargs["str1"]
  str2 = kwargs["str2"]

  result = solution(str1, str2)
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

