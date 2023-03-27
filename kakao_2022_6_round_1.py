'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 6

skill = [type, r1, c1, r2, c2, degree]
type 1 = enemy attack and degree is damage from attack
type 2 = recovery and degree is amount of recovery

Cumulative sum for a constant c added/subtracted 
across an range of elements between position a and
position b in an array can be represented by placing 
c in position a and the opposite sign in position b+1
in a new array and then calculating the cumulative sum

[ 1, 2, 4, 8, 9] --> [-1, 0, 2, 6, 9]
--> subtract 2 from elements in positions 0 to 3 

This can be represented as:
[-2, -2, -2, -2, 0]

but can also be represented by:
[-2, 0, 0, 0, 2]

and then calculating the cumulative sum of the array:
[-2, -2+0=-2, -2+0=-2, -2+0=-2, -2+2=0]
--> [-2,-2,-2,-2,0]

For example 2:

Add attacks and recoveries to empty two-dimensional array:

    0  1  2
-------------
0 | 0  0  0  0
1 | 0  0  0  0
2 | 0  0  0  0
  | 0  0  0  0

Attack 1 = [1,1,1,2,2,4]:

     0     1     2  
--------------------------
0 |  0     0     0     0
1 |  0    -4     0     4
2 |  0     0     0     0
  |  0     4     0    -4

Attack 2 = [1,0,0,1,1,2]:

      0     1     2
---------------------------
0 |  -2     0     2     0
1 |   0    -4     0     4
2 |   2     0    -2     0
  |   0     4     0    -4

Recovery 1 = [2,2,0,2,0,100]:

      0     1     2
---------------------------
0 |  -2     0     2     0
1 |   0    -4     0     4
2 | 102  -100    -2     0
  |-100   104     0    -4

Find top-to-bottom cumulative sum of matrix:

      0     1     2
---------------------------
0 |  -2     0     2     0
1 |  -2    -4     2     4
2 | 100  -104     0     4
  |   0     0     0     0

Find left-to-right cumulative sum of matrix:

      0     1     2
---------------------------
0 |  -2    -2     0     0
1 |  -2    -6    -4     0
2 | 100    -4    -4     0
  |   0     0     0     0

Add the cumulative sum matrix to the original matrix:

     1  2  3       -2  -2  0       -1   0   3
     4  5  6   +   -2  -6 -4   =    2  -1   2
     7  8  9      100  -4 -4      107   4   5

Result = 6

'''

boards = [
  [
    [5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]
  ],
  [
    [1,2,3],[4,5,6],[7,8,9]
  ]
]

skills = [
  [
    [1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1, 3,3,1]
  ],
  [
    [1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]
  ]
]

expected_results = [
  10,6
]

def get_undestroyed_buildings(board,skill):
  results = 0
  row = len(board)
  col = len(board[0])
  
  # create sum array to hold values of each move
  sum = [[0 for x in (range(col+1))] for x in (range(row+1))]
  # add moves to sum array
  for move in skill:
    if move[0] == 2:
      sum[move[1]][move[2]] += move[5]
      sum[move[3]+1][move[4]+1] += move[5]
      sum[move[1]][move[4]+1] -= move[5]
      sum[move[3]+1][move[2]] -= move[5]
    else:
      sum[move[1]][move[2]] -= move[5]
      sum[move[3]+1][move[4]+1] -= move[5]
      sum[move[1]][move[4]+1] += move[5]
      sum[move[3]+1][move[2]] += move[5]
  
  # find cumulative sum of sum array
  for x in range(col+1):
    for i in range(1,row+1):
      sum[i][x] += sum[i-1][x]
  for y in range(row+1):
    for j in range(1,col+1):
      sum[y][j] += sum[y][j-1]
  
  # add cumulative sum to start array
  for m in range(row):
    for n in range(col):
      board[m][n] += sum[m][n]
      # add all values above 0 to results
      if board[m][n] > 0:
        results += 1

  return results

for test_index in range(len(boards)):
  # if test_index == 0:
    board = boards[test_index]
    skill = skills[test_index]
    
    result = get_undestroyed_buildings(board,skill)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")


