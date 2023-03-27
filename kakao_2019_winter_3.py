'''

kakao 2019 winter intern test

https://tech.kakao.com/2020/04/01/2019-internship-test/

Problem 3

'''

parameters = [
  {
    "user_id": [
      "frodo",
      "fradi",
      "crodo",
      "abc123",
      "frodoc"
    ],
    "banned_id": [
      "fr*d*",
      "abc1**"
    ]
  }, {
    "user_id": [
      "frodo",
      "fradi",
      "crodo",
      "abc123",
      "frodoc"
    ],
    "banned_id": [
      "*rodo",
      "*rodo",
      "******"
    ]
  }, {
    "user_id": [
      "frodo",
      "fradi",
      "crodo",
      "abc123",
      "frodoc"
    ],
    "banned_id": [
      "fr*d*",
      "*rodo",
      "******",
      "******"
    ]
  }
]

expected_results = [
  2,
  2,
  3
]

# Failed to pass test cases 1,5,6,9
# I handled it by removing duplicates at the end, but why not?
# I did not consider the case of ****** from the beginning. solve.
banned_star = []
ans = []

def count(banned_id, user_id, banidx, isfound, cnt):
  # end condition (if searched to the end)
  if banidx == len(banned_star):
    if cnt == len(banned_star):
      answer = isfound[:]
      ans.append(answer)
    return
  usr_idx = 0
  for usr in user_id:  # while traversing the user_id...
    # ..check if they are the same length
    if len(usr) == len(banned_id[banidx]):  
      flag = False
      # *banned_id only
      if len(banned_star[banidx]) == 0:
        flag = True
      else:
        for num in banned_star[banidx]:
          # stop if different IDs during matching
          if usr[num] != banned_id[banidx][num]:  
            flag = False
            break
          else:
            flag = True
      if isfound[usr_idx] == 0 and flag:
        isfound[usr_idx] = 1
        # find the next ID
        count(banned_id, user_id, banidx + 1, isfound, cnt + 1)  
        isfound[usr_idx] = 0
      usr_idx += 1

def solution(user_id, banned_id):
  # *I try to compare it with the ID by storing the idx, not the .
  for ban in banned_id:
    num = []
    for idx in range(len(ban)):
      if ban[idx] != '*':
        num.append(idx)
    banned_star.append(num)

  # look around banned_id number 0
  usr_idx = 0
  isfound = [0 for _ in range(len(user_id))]
  # while traversing the user_id...
  for usr in user_id:
    # ...check if they are the same length
    if len(usr) == len(banned_id[0]):  
      flag = False
      # *banned_id only
      if len(banned_star[0]) == 0:  
        flag = True
      else:
        for num in banned_star[0]:
          # stop if different IDs during matching
          if usr[num] != banned_id[0][num]:  
            flag = False
            break
          else:
            flag = True
      if isfound[usr_idx] == 0 and flag:
        isfound[usr_idx] = 1
        # find the next ID
        count(banned_id, user_id, 1, isfound, 1)  
        isfound[usr_idx] = 0
    usr_idx += 1
  # if there are identical banned_ids, duplicates are processed because duplicate cases are checked. to Set.
  answer = len(set(list(map(tuple, ans))))
  return answer

def problem(**kwargs):
  user_id = kwargs["user_id"]
  banned_id = kwargs["banned_id"]

  result = solution(user_id, banned_id)
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

