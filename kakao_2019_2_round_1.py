'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 2

'''

parameters = [
  {
    "N": 5,
    "stages": [2,1,2,6,2,4,3,3]
  },
  {
    "N": 4,
    "stages": [4,4,4,4,4]
  }
]

expected_results = [
  [3,4,2,1,5],
  [4,1,2,3]
]

def solution(N, stages):
  answer = []
  dic = {}
  for s in stages:
    if s in dic:
      dic[s] += 1
    else:
      dic[s] = 1

  percents = []
  app = len(stages)
  for i in range(1, N + 1):  # 1~N Stage
    if i in dic:
      unclear = dic[i]
      percent = unclear / app
      app -= unclear
      percents.append((percent, i))
    else:
      percents.append((0, i))
  percents.sort(reverse=True)

  same = []
  for i in range(len(percents)):
    if i == 0:
      same.append(percents[i][1])
      continue

    if percents[i][0] == percents[i - 1][0]:  # 이전꺼랑 확률이 같으면
      same.append(percents[i][1])
    else:  # 다르면
      # 같은 것이 있었을 때, 확률이 같은 것을 역순으로 집어넣기
      while len(same) != 0:
          val = same.pop()
          answer.append(val)
      same.append(percents[i][1])

  while len(same) != 0:
    val = same.pop()
    answer.append(val)

  return answer

def problem(**kwargs):
  N = kwargs["N"]
  stages = kwargs["stages"]

  result = solution(N, stages)
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

