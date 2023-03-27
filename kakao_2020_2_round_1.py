'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 2

Find correct parentheses.

balanced parentheses string: "(()))("
valid parentheses string: "(())()"

1. If the input is an empty string, it returns an empty string.
2. Split the string w into two "balanced parentheses strings" u, v. However, u must be a "balanced parentheses string" that can no longer be broken down, and v can be an empty string.
3. If string u is "a valid parentheses string", repeat step 1 for string v.
  3-1. Concatenates the result string to u and returns it.
4. If the string u is not a "valid parentheses string", follow the steps below.
  4-1. Append '(' as the first character to an empty string.
  4-2. Concatenates the resulting strings recursively from step 1 on the string v.
  4-3. Add ')' again.
  4-4. Removes the first and last characters of u, reverses the parentheses in the rest of the string, and appends them to the end.
  4-5. Return the generated string.

'''

parameters = [
  {
    "p": "(()())()"
  },
  {
    "p": ")("
  },
  {
    "p": "()))((()"
  }
]

expected_results = [
  "(()())()",
  "()",
  "()(())()"
]


def recursive(parentheses):
  # if input string empty then return empty string
  if len(parentheses) == 0:
    return ""

  u = ""
  v = ""
  left_count = 0
  right_count = 0
  # split into balanced parentheses strings u, v
  is_correct = True
  # determine if parentheses input is valid or not
  for index in range(len(parentheses)):
    print(f"input: {parentheses[index]}")
    if parentheses[index] == '(':
      left_count += 1
    else:
      right_count += 1
    u += parentheses[index]
    if left_count < right_count:
      is_correct = False    
    if left_count == right_count:
      v = parentheses[index+1:]
      break

  # check if 'u'' string is valid parentheses string
  is_correct = True
  left_count = 0
  right_count = 0
  for index in range(len(u)):
    if left_count < right_count:
      is_correct = False
      break
    if u[index] == '(':
      left_count += 1
    else:
      right_count += 1

  # if 'u'' string is a valid parentheses string
  if is_correct:
    return u + recursive(v)
  # else fix 'u' string by following steps in number 4 
  else:
    string = '('
    string += recursive(v)
    string += ')'
    u = u[1:-1]
    for idx in range(len(u)):
      if u[idx] == '(':
        string += ')'
      elif u[idx] == ')':
        string += '('
      else:
        string += u[idx]
    return string


def problem(**kwargs):
  p = kwargs["p"]

  result = recursive(p)
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

