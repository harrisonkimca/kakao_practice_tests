'''

kakao 2021 winter intern test

https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/

Problem 3

Angmond, an intern at Needworks that develops business software, was tasked with writing a program that selects, adds, deletes, and restores table rows based on commands. The detailed requirements are as follows:

Row   Name
0     Muzi
1     Con
2     Apeach
3     Jay-G
4     Frodo
5     Neo
6     Tube
7     Ryan

Only a single row can be selected at a time and it cannot exceed the range of the table (row 0 to the last row). At this time, edit the table using the following commands.

- "U X": Selects the row X space above the currently selected row.

- "D X": Selects the row X space below the currently selected row.

- "C": Deletes the currently selected row and selects the row immediately below it. However, if the deleted row is the last row, the row immediately above is selected.

- "Z": Recovers the most recently deleted row. However, the currently selected row is not changed.

Input values are an integer, n, indicating the number of rows of the original table; an integer, k, indicating the position of the initially selected row; and a string array containing the commands to execute on the original table. The output returns a string where 'O' indicates a row being displayed and an 'X' indicates a deleted row after all the commands in command string array are executed on the original table. 

Example: 

n  k  cmd                                                        result
8  2  ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]              "OOOOXOOO"
8  2  ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]    "OOXOXOOO"

'''

parameters = [
  {
    "ns": 8,
    "ks": 2,
    "cmds": ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
  }, {
    "ns": 8,
    "ks": 2,
    "cmds": ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
  }
]

expected_results = [
  "OOOOXOOO",
  "OOXOXOOO"
]


def move(n, direction, current, number, rows):
  if direction == 'up':
    move = -1
  elif direction == 'dn':
    move = 1
  next = current + move
  count = 0
  while count !=number:
    scan = rows[next%n]
    if scan != 'X':
      count += 1
    current = (current + move)%n
    next += move
  return current

def not_last(current,rows):
  for row in rows[(current+1):]:
    if row == 'O':
      return True

def table_result(n, k, cmd):
  rows = ['O'] * n
  stack = []
  current = k
  for command in cmd:
    com = command.split()
    if com[0] == 'D':
      current = move(n, 'dn', current, int(com[1]), rows)
    elif com[0] == 'U':
      current = move(n, 'up', current, int(com[1]), rows)
    elif com[0] == 'C':
      rows[current] = 'X'
      stack.append(current)
      if not_last(current,rows):
        current = (current+1)%n
      else:
        current = (current-1)%n
    elif com[0] == 'Z':
      rows[stack.pop()] = 'O'
    else:
      print("Incorrect input. Please try again.")
    
  result = ''.join(map(str,rows))
  return result


def problem(**kwargs):
  n = kwargs["ns"]
  k = kwargs["ks"]
  cmd = kwargs["cmds"]

  result = table_result(n,k,cmd)
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

