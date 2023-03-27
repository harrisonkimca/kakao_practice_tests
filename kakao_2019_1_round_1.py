'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 1

'''

parameters = [
  {
    "record": [
      "Enter uid1234 Muzi", 
      "Enter uid4567 Prodo",
      "Leave uid1234",
      "Enter uid1234 Prodo",
      "Change uid4567 Ryan"
    ]
  }
]

expected_results = [
  [
    "Prodo has entered",
    "Ryan has entered",
    "Prodo has left",
    "Prodo has entered"
  ]
]

def solution(record):
  answer = []
  userdic = {}  # A dictionary of {userid:name}
  for rec in record:
    inp = rec.split(' ')
    op = inp[0]
    uid = inp[1]
    if op == "Enter":
      nickname = inp[2]
      userdic[uid] = nickname
    elif op == "Change":
      nickname = inp[2]
      userdic[uid] = nickname

  for rec in record:
    inp = rec.split(' ')
    op = inp[0]
    uid = inp[1]
    if op == "Enter":
      log = userdic[uid] + " has entered"
      answer.append(log)
    elif op == "Leave":
      log = userdic[uid] + " has left"
      answer.append(log)

  return answer

def problem(**kwargs):
  record = kwargs["record"]

  result = solution(record)
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

