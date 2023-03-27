'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 4

Do full exploration:
1. Create new 'score' list by adding +1 to every position from 'info' list 
   until n arrows is reached (sum('score') == n)
2. Begin exploration from last position with value > 0 in 'score' list 
   (excluding position 10 or zero score value)
3. Change value in last position to zero and then add +1 to every position 
   from 'info' list for all positions after this position until n arrows is 
   reached
4. Continue this until all values in the 'score' list are zero 


Alternatively:

1. Compare every position against info list
2. Check state at each position: 
      0 or +1 better
3. Assign 0 or +1 depending on state until all n arrows used up
4. Any remaining arrows are moved to last position (value 0)
5. Make dynamic for changing value for n

'''

# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]
# result = [0,2,2,0,1,0,0,0,0,0,0]

#    [2,1,1,1,0,0,0,0,0,0,0]
#    10 9 8 7 6 5 4 3 2 1 0
# 1. [3,2,0,0,0,0,0,0,0,0,0] = 19
# 2. [3,0,2,0,0,0,0,0,0,0,0] = 18
# 3. [3,0,0,2,0,0,0,0,0,0,0] = 17
# 4. [3,0,0,0,1,1,0,0,0,0,0] = 21
# 5. [3,0,0,0,0,1,1,0,0,0,0] = 19
# 6. [3,0,0,0,0,0,1,1,0,0,0] = 17
# 7. [3,0,0,0,0,0,0,1,1,0,0] = 15
# 8. [3,0,0,0,0,0,0,0,1,1,0] = 13
# 9. [3,0,0,0,0,0,0,0,0,1,1] = 11
#10. [3,0,0,0,0,0,0,0,0,0,2] = 10
#11. [0,2,2,0,1,0,0,0,0,0,0] = 23 ***
#12. [0,0,2,2,1,0,0,0,0,0,0] = 21
#13. [0,0,0,2,1,1,1,0,0,0,0] = 22
#14. [0,0,0,0,1,1,1,1,1,0,0] = 20
#15. [0,0,0,0,0,1,1,1,1,1,0] = 15
#16. [0,0,0,0,0,0,1,1,1,1,1] = 10
#17. [0,0,0,0,0,0,0,1,1,1,2] = 6
#18. [0,0,0,0,0,0,0,0,1,1,3] = 3
#19. [0,0,0,0,0,0,0,0,0,1,4] = 1
#20. [0,0,0,0,0,0,0,0,0,0,5] = 0


# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# result = [-1]

#    [1,0,0,0,0,0,0,0,0,0,0]
#    10 9 8 7 6 5 4 3 2 1 0
# 1. [1,0,0,0,0,0,0,0,0,0,0] = 10
# 2. [0,1,0,0,0,0,0,0,0,0,0] = 9
# 3. [0,0,1,0,0,0,0,0,0,0,0] = 8
# 4. [0,0,0,1,0,0,0,0,0,0,0] = 7
# 5. [0,0,0,0,1,0,0,0,0,0,0] = 6
# 6. [0,0,0,0,0,1,0,0,0,0,0] = 5
# 7. [0,0,0,0,0,0,1,0,0,0,0] = 4
# 8. [0,0,0,0,0,0,0,1,0,0,0] = 3
# 9. [0,0,0,0,0,0,0,0,1,0,0] = 2
#10. [0,0,0,0,0,0,0,0,0,1,0] = 1
#11. [0,0,0,0,0,0,0,0,0,0,1] = 0


# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
# result = [1,1,2,0,1,2,2,0,0,0,0]

#    [0,0,1,2,0,1,1,1,1,1,1]
#    10 9 8 7 6 5 4 3 2 1 0
# 1. [1,1,2,3,1,0,0,0,0,0,1] = 40
# 2. [1,1,2,3,0,2,0,0,0,0,0] = 39
# 3. [1,1,2,3,0,0,2,0,0,0,0] = 38
# 4. [1,1,2,3,0,0,0,2,0,0,0] = 37
# 5. [1,1,2,3,0,0,0,0,2,0,0] = 36
# 6. [1,1,2,3,0,0,0,0,0,2,0] = 35
# 7. [1,1,2,3,0,0,0,0,0,0,2] = 34
# 8. [1,1,2,0,1,2,2,0,0,0,0] = 42 ***
# 9. [1,1,2,0,0,2,2,0,0,0,1] = 36
#10. [1,1,2,0,0,0,2,2,0,0,1] = 34
#11. [1,1,2,0,0,0,0,2,2,0,1] = 32
#12. [1,1,2,0,0,0,0,0,2,2,1] = 30
#13. [1,1,2,0,0,0,0,0,0,2,3] = 28
#14. [1,1,2,0,0,0,0,0,0,0,5] = 27
#15. [1,1,0,3,1,2,0,0,0,0,1] = 38
#16. [1,1,0,0,1,2,2,2,0,0,0] = 37
#17. [1,1,0,0,0,2,2,2,0,0,1] = 31
#18. [1,1,0,0,0,0,2,2,2,0,1] = 28
#19. [1,1,0,0,0,0,0,2,2,2,1] = 25
#20. [1,1,0,0,0,0,0,0,2,2,3] = 22
#21. [1,1,0,0,0,0,0,0,0,2,5] = 20
#22. [1,1,0,0,0,0,0,0,0,0,7] = 19
#23. [1,0,2,3,1,2,0,0,0,0,0] = 36
#24. [1,0,0,3,1,2,2,0,0,0,0] = 32
#25. [1,0,0,0,1,2,2,2,0,0,1] = 28
#26. [1,0,0,0,0,2,2,2,2,0,0] = 24
#27. [1,0,0,0,0,0,2,2,2,2,0] = 20
#28. [1,0,0,0,0,0,0,2,2,2,2] = 16
#29. [1,0,0,0,0,0,0,0,2,2,4] = 13
#30. [1,0,0,0,0,0,0,0,0,2,6] = 11
#31. [1,0,0,0,0,0,0,0,0,0,8] = 10
#32. [0,1,2,3,1,2,0,0,0,0,0] = 36
#33. [0,0,2,3,1,2,0,0,0,0,1] = 26
#34. [0,0,0,3,1,2,2,0,0,0,1] = 22
#35. [0,0,0,0,1,2,2,2,2,0,0] = 18
#36. [0,0,0,0,0,2,2,2,2,0,1] = 14
#37. [0,0,0,0,0,0,2,2,2,2,1] = 10
#38. [0,0,0,0,0,0,0,2,2,2,3] =  6
#39. [0,0,0,0,0,0,0,0,2,2,5] =  3
#40. [0,0,0,0,0,0,0,0,0,2,7] =  1
#41. [0,0,0,0,0,0,0,0,0,0,9] =  0


# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]
# result = [1,1,1,1,1,1,1,1,0,0,2]

#    [0,0,0,0,0,0,0,0,3,4,3]
#    10 9 8 7 6 5 4 3 2 1 0
# 1. [1,1,1,1,1,1,1,1,0,0,2] = 52
# 2. [1,1,1,1,1,1,1,0,0,0,3] = 49
# 3. [1,1,1,1,1,1,1,0,0,0,3] = 49
# 4. [1,1,1,1,1,1,1,0,0,0,3] = 49
# 5. [1,1,1,1,1,1,0,1,0,0,3] = 48
# 6. [1,1,1,1,1,1,0,0,4,0,0] = 47
# 7. [1,1,1,1,1,1,0,0,0,0,4] = 45
# 8. [1,1,1,1,1,1,0,0,0,0,4] = 45
# 9. [1,1,1,1,1,0,1,1,0,0,3] = 47
#10. [1,1,1,1,1,0,0,1,4,0,0] = 45
#11. [1,1,1,1,1,0,0,0,4,0,1] = 42
#12. [1,1,1,1,1,0,0,0,0,5,0] = 41
#13. [1,1,1,1,1,0,0,0,0,0,5] = 40
#14. [1,1,1,1,0,1,1,1,0,0,3] = 46
#15. [1,1,1,1,0,0,1,1,4,0,0] = 43
#16. [1,1,1,1,0,0,0,1,4,0,1] = 39
#17. [1,1,1,1,0,0,0,0,4,0,2] = 36
#18. [1,1,1,1,0,0,0,0,0,5,1] = 35
#19. [1,1,1,1,0,0,0,0,0,0,6] = 34
#20. [1,1,1,0,1,1,1,1,0,0,3] = 45
#21. [1,1,1,0,0,1,1,1,4,0,0] = 41
#22. [1,1,1,0,0,0,1,1,4,0,1] = 36
#23. [1,1,1,0,0,0,0,1,4,0,2] = 32
#24. [1,1,1,0,0,0,0,0,4,0,3] = 29
#25. [1,1,1,0,0,0,0,0,0,5,2] = 28
#26. [1,1,1,0,0,0,0,0,0,0,7] = 27
#27. [1,1,0,1,1,1,1,1,0,0,3] = 44
#28. [1,1,0,0,1,1,1,1,4,0,0] = 39
#29. [1,1,0,0,0,1,1,1,4,0,1] = 44
#30. [1,1,0,0,0,0,1,1,4,0,2] = 28
#31. [1,1,0,0,0,0,0,1,4,0,3] = 24
#32. [1,1,0,0,0,0,0,0,4,0,4] = 21
#33. [1,1,0,0,0,0,0,0,0,5,3] = 20
#34. [1,1,0,0,0,0,0,0,0,0,8] = 19
#35. [1,0,1,1,1,1,1,1,0,0,3] = 43
#36. [1,0,0,1,1,1,1,1,4,0,0] = 37
#37. [1,0,0,0,1,1,1,1,4,0,1] = 30
#38. [1,0,0,0,0,1,1,1,4,0,2] = 24
#39. [1,0,0,0,0,0,1,1,4,0,3] = 19
#40. [1,0,0,0,0,0,0,1,4,0,4] = 15
#41. [1,0,0,0,0,0,0,0,4,5,0] = 13
#42. [1,0,0,0,0,0,0,0,0,5,4] = 11
#43. [1,0,0,0,0,0,0,0,0,0,9] = 10
#44. [0,1,1,1,1,1,1,1,0,0,3] = 42
#45. [0,0,1,1,1,1,1,1,4,0,0] = 35
#46. [0,0,0,1,1,1,1,1,4,0,1] = 27
#47. [0,0,0,0,1,1,1,1,4,0,2] = 20
#48. [0,0,0,0,0,1,1,1,4,0,3] = 14
#49. [0,0,0,0,0,0,1,1,4,0,4] =  9
#50. [0,0,0,0,0,0,0,1,4,5,0] =  6
#51. [0,0,0,0,0,0,0,0,4,5,1] =  3
#52. [0,0,0,0,0,0,0,0,0,5,5] =  1
#53. [0,0,0,0,0,0,0,0,0,0,10] = 0


ns = [
  5,
  1,
  9,
  10
]

infos = [
  [2,1,1,1,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,2,0,1,1,1,1,1,1],
  [0,0,0,0,0,0,0,0,3,4,3]
]

expected_results = [
  [0,2,2,0,1,0,0,0,0,0,0],
  [-1],
  [1,1,2,0,1,2,2,0,0,0,0],
  [1,1,1,1,1,1,1,1,0,0,2]
]



# reset all positions after index with info[k] + 1
def fire_arrows(index,arrows,n,score,info,count):
  score[index] = 0
  position = 0
  for k in range(index + 1,len(info) - 1):
    if arrows <= n and k < len(info) - 1 and arrows >= info[k] + 1:
      score[k] = info[k] + 1
      count += 10 - k
      arrows -= score[k]
      position = k
  score[len(info) - 1] = arrows
  arrows -= score[len(info) - 1]
  return score, count, position
    
def get_full_exploration(n,info):
  print(f"n = {n}")
  print(info)
  
  # find initial score
  init_arrows = n
  init_score = [0] * len(info)
  point_count = 0
  start, points, position = fire_arrows(-1,init_arrows,n,init_score,info,point_count)
  best_points = points
  best_score = start.copy()
  # print(f"{start} = {points}")
  
  # explore from last index position of initial score 
  index = position
  for i in reversed(range(index + 1)):
    score = [0] * len(info)
    arrows = n
    new_score = []
    for j in range(len(info) - 1):
      if j < i and arrows <= n and j < len(info) - 1 and arrows >= info[j] + 1:
        score[j] = info[j] + 1
        point_count += 10 - j
        arrows -= score[j]
      if j >= i:
        new_score, new_points, position = fire_arrows(j,arrows,n,score,info,point_count)
        # print(f"{new_score} = {new_points}")
        if new_points > best_points:
          best_points = new_points
          best_score = new_score.copy()
    point_count = 0
  
  # check info list against best_score list
  check_info = 0  
  check_score = 0
  for index in range(len(info)):
    if best_score[index] > info[index]:
      check_score += 10 - index
    elif info[index] > 0 and info[index] >= best_score[index]:
      check_info += 10 - index
  if check_info >= check_score:
    return [-1]
  else:
    return best_score

def find_highest_score(n,info,results):
  highest_score = get_full_exploration(n,info)
  return highest_score

for test_index in range(len(ns)):
  # if test_index == 1:
    n = ns[test_index]
    info = infos[test_index]
    results = expected_results[test_index]
    
    result = find_highest_score(n,info,results)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")