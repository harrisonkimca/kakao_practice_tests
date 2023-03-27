# https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
# https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
# https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/

#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
#    / \
#   7   8


from collections import deque

class Node:
  def __init__(self,data=None,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

# inorder: 4 2 1 7 5 8 3 6 None
def inorder(root):
  # base case to return
  if root is None:
    return
  # traverse left subtree
  inorder(root.left)
  # display nodes after left subtree traversed
  print(root.data,end=" ")
  # traverse right subtree
  inorder(root.right)

# preorder: 1 2 4 3 5 7 8 6 None
def preorder(root):
  # base case to return
  if root is None:
    return
  # display nodes as left subtree traversed
  print(root.data,end=" ")
  # traverse left subtree
  preorder(root.left)
  # traverse right subtree
  preorder(root.right)

# postorder: 4 2 7 8 5 6 3 1 None
def postorder(root):
  # base case to return
  if root is None:
    return
  # traverse left subtree
  postorder(root.left)
  # traverse right subtree
  postorder(root.right)
  # display nodes after subtrees traversed
  print(root.data,end=" ")

# inorderIterative: 4 2 1 7 5 8 3 6 None
def inorderIterative(root):
  # initiate empty stack
  stack = deque()
  # start from root node
  curr = root
  # loop until empty stack or curr != None
  while stack or curr:
    if curr:
      # push curr to stack
      stack.append(curr)
      # move to curr's left child 
      curr = curr.left
    # if curr = None begin popping from stack
    else:
      # check right sub tree as curr popped from stack
      curr = stack.pop()
      # print curr as popped from stack (ie,no more children)
      print(curr.data,end=" ")
      # move to curr's right child
      curr = curr.right

# preorderIterative: 1 2 4 3 5 7 8 6 None
def preorderIterative(root):
  # base case to return
  if root is None:
    return
  # initiate stack with root node
  stack = deque()
  stack.append(root)
  # loop until stack is empty
  while stack:
    # begin traversal at root node
    curr = stack.pop()
    # print curr as each node traversed
    print(curr.data,end=" ")
    # add right child to stack
    if curr.right:
      stack.append(curr.right)
    # add left child to stack
    if curr.left:
      stack.append(curr.left)

# postorderIterative: 4 2 7 8 5 6 3 1 None
def postorderIterative(root):
  # base case to return
  if root is None:
    return
  # initiate stack with root node
  stack = deque()
  stack.append(root)
  # initiate stack to store postorder traversal
  out = deque()
  # loop until stack is empty
  while stack:
    # begin traversal at root node and push node onto out stack
    curr = stack.pop()
    out.append(curr.data)
    # add left child to stack
    if curr.left:
      stack.append(curr.left)
    # add right child to stack
    if curr.right:
      stack.append(curr.right)
  while out:
    # print out node as each node popped from out stack
    print(out.pop(),end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print("inorder:",end=" ")
print(inorder(root))

print("inorderIterative:",end=" ")
print(inorderIterative(root))

print("preorder:",end=" ")
print(preorder(root))

print("preorderIterative:",end=" ")
print(preorderIterative(root))

print("postorder:",end=" ")
print(postorder(root))

print("postorderIterative:",end=" ")
print(postorderIterative(root))