'''

kakao 2022 summer intern test

https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/

Problem 2

'''


queue_ones = [
  [180, 5000, 10, 600],
  [120, 0, 60, 591],
  [1, 461, 1, 10]
]

queue_twos = [
  [180, 5000, 10, 600],
  [120, 0, 60, 591],
  [1, 461, 1, 10]
]

expected_results = [
  [180, 5000, 10, 600],
  [120, 0, 60, 591],
  [1, 461, 1, 10]
]


def make_queues_equal(queue_one, queue_two):
  return queue_one


for test_index in range(len(queue_ones)):
  # if test_index == 2:
    queue_one = queue_ones[test_index]
    queue_two = queue_twos[test_index]
    
    result = make_queues_equal(queue_one, queue_two)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
