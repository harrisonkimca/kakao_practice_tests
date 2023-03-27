'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 2

To prevent corona virus infection, test takers must keep a distance and wait, but since this is a development job interview, the following rules are guiding them to sit at a distance in the waiting room.

1. There are 5 waiting rooms, each of which is 5×5 in size.
2. In order to maintain a distance, please do not sit with a Manhattan distance of 2 or less between test takers.
3. However, it is allowed if the seats where the test takers are seated are blocked by a partition.

✔Manhattan distance: If two tables T1 and T2 are located in matrices (r1, c1) and (r2, c2) respectively, then the Manhattan distance between T1 and T2 is |r1 – r2| + |c1 – c2|.

"POOOP" 
"OXXOX" 
"OPXPX" 
"OOXOX" 
"POXXP"

"PXPXP" 
"XPXPX" 
"PXPXP" 
"XPXPX" 
"PXPXP"

'''

parameters = [
  {
    "places": ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
  }, {
    "places": ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
  }, {
    "places": ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"]
  }, {
    "places": ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
  }, {
    "places": ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
  }
]

expected_results = [
  1,
  0,
  1,
  1,
  1
]


def check_row(scan, selector):
  if scan[0] == 'P':
    if scan[1] == 'P':
      selector = 0
    elif scan[2] == 'P' and scan[1] != 'X':
      selector = 0
  return selector

def check_column(scan, selector):
  if scan[0] == 'P':
    if (scan[1] == 'P' or (scan[1] != 'X'and scan[2] == 'P')):
      selector = 0
    elif (scan[4] == 'P' and (scan[1] != 'X' and scan[3] != 'X')):
      selector = 0
  return selector

def check_room(room):
  selector = 1
  for j, row in enumerate(room):
    # print(f"row: {row}")
    for k, seat in enumerate(row):
      # print(f"seat: {seat}")
      # row_right
      if(k+3 <= len(row)):
        scan = []
        scan.append(row[k])
        scan.append(row[k+1])
        scan.append(row[k+2])
        # print(scan)
        selector = check_row(scan, selector)
        # print(f"row_selector: {selector}")
      # row_left
      if(k+3 >= len(row)):
        scan = []
        scan.append(row[k])
        scan.append(row[k-1])
        scan.append(row[k-2])
        # print(scan)
        selector = check_row(scan, selector)
        # print(f"row_selector: {selector}")
      # column_down_right
      if(j+3 <= len(room) and k+2 <= len(row)):
        scan = []
        scan.append(room[j][k])
        scan.append(room[j+1][k])
        scan.append(room[j+2][k])
        scan.append(room[j][k+1])
        scan.append(room[j+1][k+1])
        # print(scan)
        selector = check_column(scan, selector)
        # print(f"column_selector: {selector}")
      # column_up_right
      if(j+3 >= len(room) and k+2 <= len(row)):
        scan = []
        scan.append(room[j][k])
        scan.append(room[j-1][k])
        scan.append(room[j-2][k])
        scan.append(room[j][k+1])
        scan.append(room[j-1][k+1])
        # print(scan)
        selector = check_column(scan, selector)
        # print(f"column_selector: {selector}")
      # column_down_left
      if(j+3 <= len(room) and k+4 >= len(row)):
        scan = []
        scan.append(room[j][k])
        scan.append(room[j+1][k])
        scan.append(room[j+2][k])
        scan.append(room[j][k-1])
        scan.append(room[j+1][k-1])
        # print(scan)
        selector = check_column(scan, selector)
        # print(f"column_selector: {selector}")
      # column_up_left
      if(j+3 >= len(room) and k+4 >= len(row)):
        scan = []
        scan.append(room[j][k])
        scan.append(room[j-1][k])
        scan.append(room[j-2][k])
        scan.append(room[j][k-1])
        scan.append(room[j-1][k-1])
        # print(scan)
        selector = check_column(scan, selector) 
        # print(f"column_selector_last: {selector}")
  return selector

# NOTES
# complex conditions need full conditions e.g. first_row[i] == 'P' and first_row[i+1] == 'P'
# validation pattern: assume valid at the start e.g. valid = True, until found to be invalid
# loop with access to the index: for i, value in enumerate(array)
# list splicing: array[start_index:end_index]


def problem(**kwargs):
  places = kwargs["places"]

  check_seats = check_room(places)
  return check_seats

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
