'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 1

'''

parameters = [
  {
    "s": "aabbaccc"
  },
  {
    "s": "ababcdcdababcdcd"
  },
  {
    "s": "abcabcdede"
  },
  {
    "s": "abcabcabcabcdededededede",
  },
  {
    "s": "xababcdcdababcdcd"
  }
]

expected_results = [
  7,
  9,
  8,
  14,
  17
]


# compare characters in string in 1, 2s, 3s...n/2
def get_best_compression(string):
  # print(f"string: {string} len: {len(string)}")
  best_compression = string
  # cut string into 1s, 2s, 3s...n/2 to find matching characters
  for cut_length in range(1, len(string)):
    # move accross string in 1s, 2s, 3s... (ie, cut)
    cut_location = cut_length
    # set first group of characters to check duplicates against 
    match = string[:cut_length]
    count = 1
    compression_string = ""
    # loop until end of string reached
    while cut_location + cut_length <= len(string):
      # increment count while parsed character identical to previous...
      if match == string[cut_location:cut_location + cut_length]:
        count += 1
      # ...once parsed character fails to match...
      else:
        # ...if more than one character matches then concatenate
        # count to string (after converting to string)
        if count > 1:
          compression_string += str(count)
        # ...concatenate count to bef...  
        compression_string += match
        # print(f"cut_length: {cut_length} compression_string: {compression_string}")
        # ...reset count to 1 for next parsing...
        count = 1
        # ...reset bef to current non-identical character
        match = string[cut_location:cut_location + cut_length]
          
      # advance to next charter in string
      cut_location += cut_length
    # last character cannot be checked so do separate check... 
    if count > 1:
      compression_string += str(count)
    compression_string += string[cut_location - cut_length:]
    # ...and store compressed string if shorter than previous string
    if len(compression_string) < len(best_compression):
      best_compression = compression_string

  return len(best_compression)


def problem(**kwargs):
  s = kwargs["s"]

  result = get_best_compression(s)
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

