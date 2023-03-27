'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 1

'''

parameters = [
  {
    "orders": [
      "ABCFG",
      "AC",
      "CDE",
      "ACDE",
      "BCFG",
      "ACDEH"
    ],
    "course": [2,3,4]
  }, {
    "orders": [
      "ABCDE",
      "AB",
      "CD",
      "ADE",
      "XYZ",
      "XYZ",
      "ACD"
    ],
    "course": [2,3,5]
  }, {
    "orders": [
      "XYZ",
      "XWY",
      "WXA"
    ],
    "course": [2,3,4]
  }
]

expected_results = [
  ["AC", "ACDE", "BCFG", "CDE"],
  ["ACD", "AD", "ADE", "CD", "XYZ"],
  ["WX", "XY"]
]


def problem(**kwargs):
  orders = kwargs["orders"]
  course = kwargs["course"]
  
  return course

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

