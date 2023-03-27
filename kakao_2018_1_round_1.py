'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 1

'''

parameters = [
  {
    "n": 5,
    "arr1": [9, 20, 28, 18, 11],
    "arr2": [30, 1, 21, 17, 28],
  },
  {
    "n": 6,
    "arr1": [46, 33, 33 ,22, 31, 50],
    "arr2": [27 ,56, 19, 14, 14, 10]
  }
]

expected_results = [
  ["#####","# # #", "### #", "# ##", "#####"],
  ["######", "### #", "## ##", " #### ", " #####", "### # "]
]


def solution_bruteforce(n, arr1, arr2):
  answer = []
  bin_arr1 = []
  bin_arr2 = []
  for num in arr1:
    bin_num = pow(2, n - 1)  # 2 to the n-1 power
    bin_str = ""
    while True:
      if num >= bin_num:  # 1 person
        num -= bin_num
        bin_str += "#"
      else:
        bin_str += " "

      bin_num = bin_num / 2  # Divide by 2
      if bin_num == 1:
        if num == 1:
          bin_str += "#"
        else:
          bin_str += " "
        break
    bin_arr1.append(bin_str)

  for num in arr2:
    bin_num = pow(2, n - 1)  # 2 to the n-1 power
    bin_str = ""
    while True:
      if num >= bin_num:  # 1 person
        num -= bin_num
        bin_str += "#"
      else:
        bin_str += " "

      bin_num = bin_num / 2  # divide by 2
      if bin_num == 1:
        if num == 1:
          bin_str += "#"
        else:
          bin_str += " "
        break
    bin_arr2.append(bin_str)

  for i in range(len(bin_arr1)):
    idx = 0
    ans_str = ""
    while idx < n:
      if bin_arr1[i][idx] == "#" or bin_arr2[i][idx] == "#":
        ans_str += "#"
      else:
        ans_str += " "
      idx += 1
    answer.append(ans_str)
  return answer


# Bit operation solver
def solution_bit(n, arr1, arr2):
  answer = []
  for i in range(n):
    string = ''
    ans = bin(arr1[i] | arr2[i])
    ans = ans[2:]
    if len(ans) != n:
      tmp = " " * (n - len(ans))
      ans = tmp + ans
    for a in ans:
      if a == '1':
        string += '#'
      else:
        string += ' '
    answer.append(string)
  return answer

def problem(**kwargs):
  n = kwargs["n"]
  arr1 = kwargs["arr1"]
  arr2 = kwargs["arr2"]

  # result = solution_bruteforce(n, arr1, arr2)
  result = solution_bit(n, arr1, arr2)
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

