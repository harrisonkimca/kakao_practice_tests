'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 3

'''

parameters = [
  {
    "cacheSize": 3,
    "cities": ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
  },
  {
    "cacheSize": 3,
    "cities": ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
  },
  {
    "cacheSize": 2,
    "cities": ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
  },
  {
    "cacheSize": 5,
    "cities": ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
  },
  {
    "cacheSize": 2,
    "cities": ["Jeju", "Pangyo", "NewYork", "NewYork"]
  }, {
    "cacheSize": 0,
    "cities": ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
  }
]

expected_results = [
  50,
  21,
  60,
  52,
  16,
  25
]

from collections import deque

def solution(cacheSize, cities):
 answer = 0
 lru = deque()
 
 if cacheSize == 0:
   return 5 * len(cities)
 
 for i in range(len(cities)):
   cities[i] = cities[i].lower()
     
 for city in cities:
   if city in lru:
     answer += 1
     lru.remove(city)
     lru.append(city)    # send to the back
   else:
     answer += 5
     if len(lru) == cacheSize:   
         lru.popleft()
     lru.append(city)
     
 return answer

def problem(**kwargs):
  cacheSize = kwargs["cacheSize"]
  cities = kwargs["cities"]

  result = solution(cacheSize, cities)
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

