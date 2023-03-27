'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 3

'''

parameters = [
  {
    "relation": [
      ["100","ryan","music","2"],
      ["200","apeach","math","2"],
      ["300","tube","computer","3"],
      ["400","con","computer","4"],
      ["500","muzi","music","3"],
      ["600","apeach","music","2"]
    ]
  }
]

expected_results = [
  2
]

import itertools

def solution(relation):
  col_len = len(relation[0])  # column length
  arrs = [i for i in range(col_len)]  # 0~n-1
  combs = []
  answers = []
  for i in range(1, col_len + 1):
    comb_list = list(itertools.combinations(arrs, i))
    if not comb_list:
        continue
    combs.append(comb_list)

  for comb in combs:  # A triple for statement can be used to access combinations...
    for idx in comb:  # (1,2), (1,2,3) # col case by case
      dic = {}  # Dictionaries for determining candidate keys
      is_ck = True  # Is it a candidate key

      for rel in relation:  # by row
        string = ""
        for i in idx:
          string += rel[i] + ","
        if string in dic or string == "":  # duplicate identification
          is_ck = False
          break
        else:
          dic[string] = 1

      if is_ck:  # Once uniquely distinguished
        answer_string = ""
        for i in idx:
          answer_string += str(i)
        is_answer = False
        if len(answers) == 0:  # if empty
          is_answer = True
        else:
          for string in answers:  # Judgment of minimality compared to lesser
            is_answer = False
            for i in range(len(string)):
              if string[i] not in answer_string:
                is_answer = True
                break
            if not is_answer:
              break
        if is_answer:
          answers.append(answer_string)

  return len(answers)

def problem(**kwargs):
  relation = kwargs["relation"]

  result = solution(relation)
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

