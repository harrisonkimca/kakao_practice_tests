'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 4

'''

parameters = [
  {
    "food_times": [3, 1, 2],
    "k": 5
  }
]

expected_results = [
  1
]

# 1st attempt, of course, timeout raw (accuracy will pass)
## This code cuts 5 minutes, how to solve the timeout?
def solution_bruteforce(food_times, k):
  time = 0
  idx = 0
  answer = 0
  dic = {}
  while True:
    if idx == len(food_times):  # 끝에 도달
      idx = 0
      continue
    if food_times[idx] == 0:
      if len(dic) == len(food_times):
        return -1
      idx += 1
      dic[idx] = 1
      continue
    if time == k:
      answer = idx + 1
      break
    food_times[idx] -= 1
    time += 1
    idx += 1

  return answer

# 2nd attempt
### The second attempt with the linked list failed to reduce the time.
class Node:
  def __init__(self, time, idx):
    self.time = time
    self.idx = idx
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self, time, idx):
    node = Node(time, idx)
    self.head = node
    self.cur = node

  def insert(self, time, idx): # append to end of linked list
    current_node = self.head
    while current_node.next is not None:
        current_node = current_node.next
    node = Node(time,idx)
    current_node.next = node
    node.prev = current_node

def solution_linked_list(food_times, k):
  linked_list = LinkedList(food_times[0], 0)
  for i in range(1,len(food_times)):
    linked_list.insert(food_times[i],i)

  cur = linked_list.head
  while k>0:
    cur.time -= 1
    k -= 1
    if cur.time == 0:
      if cur == linked_list.head:
        if cur.next is None:    # no more food to eat
          return -1
        linked_list.head = cur.next
      else:
        prev_node = cur.prev
        if cur.next is not None:    # process of deleting
          next_node = cur.next
          prev_node.next = next_node
          next_node.prev = prev_node
        else:
          prev_node.next = None

    if cur.next is None:    # to the next list
      cur = linked_list.head
    else:
      cur = cur.next

  return cur.idx + 1

# I feel like I need to solve it with this two-minute search
# 3rd attempt
## I read the explanation and solved it.
## The method is to greatly reduce the number of count branches by sorting and grouping and subtracting.
## It took a long time because I couldn't catch the index sorting at the end.
def solution_sort(food_times, k):
  q = []
  for i in range(len(food_times)):
    q.append((food_times[i],i))
  q.sort()
  food_times.sort()
  times = list(set(food_times))
  times.sort()
  idx = 0
  qlen = len(q)

  for i in range(len(times)):
    while times[i] > q[idx][0]:
      idx += 1

    if i == 0:
      minus_time = times[0]
    else:
      minus_time = times[i] - times[i-1]

    k -= minus_time * (qlen - idx)   # 한 바퀴 쭉 먹어준다.
    if k < 0:   #만약 한 바퀴 쭉 돌았을 때 끝났으면,
      k += minus_time * (qlen - idx)
      idx_arr = []
      for j in range(idx,len(q)):
        idx_arr.append(q[j][1])
      idx_arr.sort()
      ans_idx = k % (qlen - idx)
      return idx_arr[ans_idx] + 1

  return -1

def problem(**kwargs):
  food_times = kwargs["food_times"]
  k = kwargs["k"]

  # result = solution_bruteforce(food_times, k)
  # result = solution_linked_list(food_times, k)
  result = solution_sort(food_times, k)
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

