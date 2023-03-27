'''

kakao 2019 winter intern test

https://tech.kakao.com/2020/04/01/2019-internship-test/

Problem 5

'''

parameters = [
  {
    "stones": [
      2,
      4,
      5,
      3,
      2,
      1,
      4,
      2,
      5,
      1
    ],
    "k": 3
  }
]

expected_results = [
  3
]

# code that only passed accuracy
def solution_bruteforce(stones, k):
  if len(stones) == k:
    answer = max(stones)
    return answer
  if k == 1:
    answer = min(stones)
    return answer
  arr = []
  for idx in range(len(stones)):
    num = [stones[idx], idx]
    arr.append(num)

  arr.sort()  # sorting is done only once
  before = 0
  answer = 0
  idxarr = [0 for _ in range(len(arr))]

  for num in arr:
    if before != num[0]:    # number has grown
      cont = 1
      for i in range(len(arr) - 1):
        if idxarr[i] != 0 and idxarr[i+1] != 0:
          cont += 1
        else:
          cont = 1
        if cont == k:
          return answer
      before = num[0]
      answer = num[0]
    idxarr[num[1]] = 1

# A problem that can be solved using binary search
# was difficult to solve
def solution_binary_search(stones, k):
 answer = 0
 left = 0
 right = max(stones)
 while left <= right:
   mid = int( (left+right) / 2)
   arr = []
   count = 0
   for stone in stones:
     arr.append(stone - mid)
   print(arr)

   for num in arr:
     if count < k:
       if num <= 0:
         count += 1
       else:
         count = 0
   if count < k:  # possible
     left = mid+1
   else: # impossible
     right = mid-1
     answer = mid
 return answer

def problem(**kwargs):
  stones = kwargs["stones"]
  k = kwargs["k"]

  # result = solution_bruteforce(stones, k)
  result = solution_binary_search(stones, k)
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

