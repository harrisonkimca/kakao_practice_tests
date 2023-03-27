'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 5

'''

parameters = [
  {
    "nodeinfo": [
      [5,3],
      [11,5],
      [13,3],
      [3,5],
      [6,1],
      [1,3],
      [8,6],
      [7,2],
      [2,2]
    ]
  }
]

expected_results = [
  [
    [7,4,6,9,1,8,5,2,3],
    [9,6,5,8,1,4,3,2,7]
  ]
]

# 6,7 runtime error? -> It was a recursion limit problem.
# This is something I couldn't solve in time and solved it overtime.
import sys

sys.setrecursionlimit(20000)
pre_nodes = []
post_nodes = []

class Node:
  def __init__(self, x, idx):
    self.left = None
    self.right = None
    self.x = x
    self.idx = idx

class Tree:
  def __init__(self, root):
    self.root_node = root
    self.current_node = None

  def insert(self, x, idx):
    self.current_node = self.root_node
    while True:
      if self.current_node.x < x:  # x it goes to the right because the value is higher.
        if self.current_node.right is not None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(x, idx)
          break
      else:  # go left
        if self.current_node.left is not None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(x, idx)
          break

  def preOrder(self, node):
    pre_nodes.append(node.idx)
    if node.left is not None:
      self.preOrder(node.left)
    if node.right is not None:
      self.preOrder(node.right)

  def postOrder(self, node):
    if node.left is not None:
      self.postOrder(node.left)
    if node.right is not None:
      self.postOrder(node.right)
    post_nodes.append(node.idx)

def solution(nodeinfo):
  # if length is 1
  if len(nodeinfo) == 1:
    return [[1], [1]]

  nodes = []
  for i in range(len(nodeinfo)):
    x = nodeinfo[i][0]
    y = nodeinfo[i][1]
    nodes.append((y, x, i + 1))
  nodes.sort(reverse=True)  # Sort by highest y-value.
  tree = Tree(Node(nodes[0][1], nodes[0][2]))

  for i in range(1, len(nodes)):
    tree.insert(nodes[i][1], nodes[i][2])

  answer = []
  tree.preOrder(tree.root_node)
  tree.postOrder(tree.root_node)
  answer.append(pre_nodes)
  answer.append(post_nodes)
  return answer

def problem(**kwargs):
  nodeinfo = kwargs["nodeinfo"]

  result = solution(nodeinfo)
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

