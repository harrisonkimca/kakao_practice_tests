'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 1

'''

parameters = [
  {
    "no": "Example 1",
    "new_id": "...!@BaT#*..y.abcdefghijklm"
  }, {
    "no": "Example 2",
    "new_id": "z-+.^."
  }, {
    "no": "Example 3",
    "new_id": "=.="
  }, {
    "no": "Example 4",
    "new_id": "123_.def"
  }, {
    "no": "Example 5",
    "new_id": "abcdefghijklmn.p"
  }
]

expected_results = [
  "bat.y.abcdefghi",
  "z--",
  "aaa",
  "123_.def",
  "abcdefghijklmn"
]


def problem(**kwargs):
  no = kwargs["no"]
  new_id = kwargs["new_id"]
  
  return new_id

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

