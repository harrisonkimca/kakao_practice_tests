'''

kakao 2019 winter intern test

https://tech.kakao.com/2020/04/01/2019-internship-test/

Problem 4

'''

parameters = [
  {
    "k": 10,
    "room_number": [
      1,
      3,
      4,
      1,
      3,
      1
    ]
  }
]

expected_results = [
  [1,3,4,2,5,6]
]

# It seemed like it was timed out...
# Perfect accuracy, zero efficiency. -> 0.5 points
def solution_list(k, room_number):
  # point to the smallest number from room 1 to room k
  rooms = [i for i  in range(k+2)]    
  # initialize up to k+1 so that whatever the value of k is, there is no runtime error
  answer = []
  for num in room_number:
    if num == rooms[num]:
      answer.append(num)
      rooms[num] = rooms[num+1]
    else:
      while num != rooms[num]:
        rooms[num] = rooms[num+1]
        num = rooms[num+1]
      answer.append(rooms[num])
      rooms[num] = rooms[num+1]
  return answer

# correct answer code
# It seems to have the same feel as my code, but the key is to use a dictionary and send it right away
# And not chasing, but updating everything with the correct answer.
def solution_dict(k, room_number):
  rooms = {}
  answer = []
  for num in room_number:
    n = num
    visit = [n]
    while n in rooms:
      n = rooms[n]
      visit.append(n)
    answer.append(n)
    for v in visit:
      rooms[v] = n+1
  return answer

def problem(**kwargs):
  k = kwargs["k"]
  room_number = kwargs["room_number"]

  # result = solution_list(k, room_number)
  result = solution_dict(k, room_number)
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

