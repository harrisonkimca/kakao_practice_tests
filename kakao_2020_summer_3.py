'''

kakao 2020 summer intern test

https://tech.kakao.com/2020/07/01/2020-internship-test/

Problem 3

'''

parameters = [
  {
    "gems": [
      "DIA",
      "RUBY",
      "RUBY",
      "DIA",
      "DIA",
      "EMERALD",
      "SAPPHIRE",
      "DIA"
    ]
  }, {
    "gems": [
      "AA",
      "AB",
      "AC",
      "AA",
      "AC"
    ]
  }, {
    "gems": [
      "XYZ",
      "XYZ",
      "XYZ"
    ]
  }, {
    "gems": [
      "ZZZ",
      "YYY",
      "NNNN",
      "YYY",
      "BBB"
    ]
  }
]

expected_results = [
  [3, 7],
  [1, 3],
  [1, 1],
  [1, 5]
]

"""
1st: Accuracy passed, Efficiency not.
I thought I wouldn't pass the efficiency... I solved this completely with nogada
First of all, 0.5 sole, required time: 15 minutes
"""

def solution_bruteforce(gems):
  jewelry = list(set(gems))
  answer = [0, 99999]
  if len(jewelry) == 1:
    answer = [1, 1]
  else:
    for idx in range(len(gems)):
      l = jewelry.copy()
      for j in range(idx, len(gems)):
        if gems[j] in l:
          l.remove(gems[j])
        if len(l) == 0:
          if answer[1] - answer[0] > j - idx:
            answer = [idx+1, j+1]
          break
  return answer

"""
2nd: Using the dictionary type definitely saved a lot of time. Accuracy code is about 22 ms taking the longest (up to 3300 for 1 byte)
But this also times out... (Teke 5,7,8,10,11,12,13,14,15)

The conclusion seems to be to reduce the number of sorts.

"""

def solution_dict(gems):
  jewelry = list(set(gems))  # type of jewelry
  answer = [0, 99999]
  if len(jewelry) == 1:
    answer = [1, 1]
  else:
    dic = {}
    for idx in range(len(gems)):
      dic[gems[idx]] = idx

      if len(dic) == len(jewelry):
        # If the lengths match and there is a change in the smallest index
        sorted_dic = sorted(dic.items(), key=lambda item: item[1])
        if sorted_dic[len(dic) - 1][1] - sorted_dic[0][1] < answer[1] - answer[0]:
          answer = [sorted_dic[0][1] + 1, sorted_dic[len(dic) - 1][1] + 1]
          dic.pop(sorted_dic[0][0])

  return answer

def problem(**kwargs):
  gems = kwargs["gems"]

  result = solution_bruteforce(gems)
  # result = solution_dict(gems)
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
