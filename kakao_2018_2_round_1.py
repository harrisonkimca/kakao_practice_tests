'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 2

'''

parameters = [
  {
    "dartResult": '1S2D*3T'
  },
  {
    "dartResult": '1D2S#10S'
  },
  {
    "dartResult": '1D2S0T'
  },
  {
    "dartResult": '1S*2T*3S'
  },
  {
    "dartResult": '1D#2S*3S'
  },
  {
    "dartResult": '1T2D3D#'
  },
  {
    "dartResult": '1D2S3T*'
  }
]

expected_results = [
  37,
  9,
  3,
  23,
  5,
  -4,
  59
]

'''
example	  dartResult	  answer	  explanation
1	        1S2D*3T	      37	      1^1 * 2 + 2^2 * 2 + 3^3
2	        1D2S#10S	    9	        1^2 + 2^1 * (-1) + 10^1
3	        1D2S0T	      3	        1^2 + 2^1 + 0^3
4	        1S*2T*3S	    23	      1^1 * 2 * 2 + 2^3 * 2 + 3^1
5	        1D#2S*3S	    5	        1^2 * (-1) * 2 + 2^1 * 2 + 3^1
6	        1T2D3D#	      -4	      1^3 + 2^2 + 3^2 * (-1)
7	        1D2S3T*	      59	      1^2 + 2^1 * 2 + 3^3 * 2
'''

def solution(dartResult):
  num = ""
  answer = 0
  numarr = []
  idx = 0
  for s in dartResult:
    if s == "S":
      now = int(num)
      num = ""
      numarr.append(now)
      answer += now
    elif s == "D":
      now = int(num)
      now = now * now
      num = ""
      numarr.append(now)
      answer += now
    elif s == "T":
      now = int(num)
      now = now * now * now
      num = ""
      numarr.append(now)
      answer += now
    elif s == "*":  # 이전 점수랑 현재 점수 더하기
      answer += numarr[-1]
      numarr[-1] = numarr[-1] * 2
      if len(numarr) > 1:
        answer += numarr[-2]
        numarr[-2] = numarr[-2] * 2
    elif s == "#":
      answer -= numarr[-1] * 2
      numarr[-1] = numarr[-1] * -1
    else:
      num += s
    print(answer)
    idx += 1
  return answer

# Code using regular expression
import re

def solution_regex(dartResult):
  p = re.compile('[0-9]+[SDT][*#]?')
  scores = p.findall(dartResult)
  total = 0
  prev_num = 0
  for score in scores:
    r = re.compile('[0-9]+')
    num = int(r.match(score).group()) # 숫자
    if score[-1] == '*':
      if score[-2] == 'D':
        num = pow(num,2)
      elif score[-2] == 'T':
        num = pow(num,3)
      num = num * 2
      total += num + prev_num
    elif score[-1] == '#':
      if score[-2] == 'D':
        num = pow(num,2)
      elif score[-2] == 'T':
        num = pow(num,3)
      num = -num
      total += num
    else:
      if score[-1] == 'D':
        num = pow(num,2)
      elif score[-1] == 'T':
        num = pow(num,3)
      total += num
    prev_num = num
  return total

def problem(**kwargs):
  dartResult = kwargs["dartResult"]

  # result = solution(dartResult)
  result = solution_regex(dartResult)
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

