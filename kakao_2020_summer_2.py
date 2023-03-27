'''

kakao 2020 summer intern test

https://tech.kakao.com/2020/07/01/2020-internship-test/

Problem 2

'''

parameters = [
  {
    "expression": "100-200*300-500+20"
  }, {
    "expression": "50*6-3*2"
  }
]

expected_results = [
  60420,
  300
]

def solution(expression):
  calc_list = []
  num_list = []
  num = ''
  answer = 0
  for e in expression:
    if e == '+':
      calc_list.append(e)
      num_list.append(int(num))
      num = ''
    elif e == '-':
      calc_list.append(e)
      num_list.append(int(num))
      num = ''
    elif e == '*':
      calc_list.append(e)
      num_list.append(int(num))
      num = ''
    else:
      num += e

  calc = list(set(calc_list))  # number of operators
  num_list.append(int(num))
  one_len = [0]
  two_len = [[0, 1], [1, 0]]
  three_len = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

  fact = []
  if len(calc) == 1:
    fact = one_len
  elif len(calc) == 2:
    fact = two_len
  else:
    fact = three_len

  if len(calc) == 1:
    idx = 0
    while idx < len(calc_list):
      if calc[0] == '-':
        num_list[idx + 1] = num_list[idx] - num_list[idx + 1]
      elif calc[0] == '+':
        num_list[idx + 1] = num_list[idx] + num_list[idx + 1]
      else:
        num_list[idx + 1] = num_list[idx] * num_list[idx + 1]
      idx += 1

    answer = max(abs(num_list[len(calc_list)]), answer)
  else:
    for f in fact:  # Where operators are considered
      cl = calc_list.copy()
      nl = num_list.copy()
      for op in f:  # Where to look for operator precedence
        # Search according to priority.
        idx = 0
        pop_list = []
        while idx < len(cl):
          if cl[idx] == calc[op]:  # If the priority is right
            if calc[op] == '-':
              val = nl[idx] - nl[idx + 1]
            elif calc[op] == '+':
              val = nl[idx] + nl[idx + 1]
            else:
              val = nl[idx] * nl[idx + 1]
            pop_list.append(idx)
            nl[idx + 1] = val
          idx += 1

        pop_list.sort()
        minus = 0
        for p in pop_list:
          del nl[p - minus]
          del cl[p - minus]
          minus += 1
      answer = max(abs(nl[0]), answer)
  return answer


def problem(**kwargs):
  expression = kwargs["expression"]

  result = solution(expression)
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
