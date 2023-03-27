'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 1

Neo and Frodo are playing a game of replacing numbers with strings as shown below. At this time, complete a function that returns the original number meaning when a string with some digits has been changed to an English word or remains unchanged is given as a parameter .s

Return integers when some numbers are changed to strings:

"one4seveneight" -> 1478
"23four5six7" -> 234567
"2three45sixseven" -> 234567
"123" -> 123

'''

parameters = [
  {
    "s": "one4seveneight"
  },{
    "s": "23four5six7"
  },{
    "s": "2three45sixseven"
  },{
    "s": "123"
  }
]

expected_results = [
  1478,
  234567,
  234567,
  123
]


def string_to_num(input_string):
  output_string = ""
  check_string = ""

  words2num = {
    'zero':'0', 
    'one':'1', 
    'two':'2', 
    'three':'3', 
    'four':'4', 
    'five':'5', 
    'six':'6', 
    'seven':'7', 
    'eight':'8', 
    'nine':'9'
  }

  for character in input_string:
    if character.isdigit():
      output_string += character
    else:
      check_string += character
      if check_string in words2num:
        add = words2num[check_string]
        output_string += add
        add = ""
        check_string = ""
  return int(output_string)


def problem(**kwargs):
  s = kwargs["s"]

  string = string_to_num(s)
  return string

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
