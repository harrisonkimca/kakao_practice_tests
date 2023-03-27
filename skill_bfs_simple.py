
info = [
  0,0,1,1,1,0,1,0,1,0,1,1
]

edges = [
  [0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]
]

#           0
#        /     \
#       1       2
#      / \     / \
#     3   4   5   6 
#    /     \       \
#   7       8       9
#                    \
#                    10
#
# {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [7], 4: [8], 6: [9], 9: [10]}


def get_adjacency_list(edges):
  child_nodes = {}
  for node in edges:
    if node[0] in child_nodes:
      child_nodes[node[0]].append(node[1])
    else:
      child_nodes[node[0]] = [node[1]]
  return child_nodes

# bfs iterative version using while loop/queue
# https://favtutor.com/blogs/breadth-first-search-python
def bfs_tree(root,links):
  # 'recursion' by deferring nodes to queue
  queue = [root]
  visited = set()
  path = []
  while queue:
    # bfs pops from front of queue
    cur = queue.pop(0)
    # print(f"cur: {cur}")
    path.append(cur)
    if cur in links and cur not in visited:
      for next_node in links[cur]:
        queue.append(next_node)
        # print(f"queue: {queue}")
      visited.add(cur)
  return path
  
# https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/?ref=rp
# https://stackoverflow.com/questions/73200007/using-breadth-first-search-for-unweighted-edges-in-a-2d-matrix
# (adopted from above two links)
def bfs_board(board,start,end):
  rows = len(board)
  cols = len(board[0])
  r,c = start
  # all moves (incl. diagonal moves)
  dx = [0,1,0,-1,-1,1,1,-1]
  dy = [-1,0,1,0,-1,-1,1,1]
  # moves list and initiate visited matrix
  dirs = ["U","R","D","L","UL","UR","DR","DL"]
  visited = [[False]*cols for i in range(rows)]
  # initiate queue with start node, empty moves list & path
  queue = [(r,c,[],[start])]
  # mark start node as visited
  visited[r][c] = True
  
  while queue:
    # find all possible moves of current node
    cur = queue.pop(0)
    r,c,moves,path = cur
    node = (r,c)
    # print(f"board[{r}][{c}]: {board[r][c]} moves:{moves} path: {path}")
    if node == end:
      return moves, path
    # generate all possible moves from dx/dy lists
    for i in range(8):
      rr = r + dy[i]
      cc = c + dx[i]
      # check boundaries
      if (rr < 0 or cc < 0):
        continue
      if (rr >= rows or cc >= cols):
        continue
      # check if already visited
      if visited[rr][cc]:
        continue
      # check if valid square
      if board[rr][cc] == '#':
        continue
      # add neighboring node to queue
      # *** update moves and path lists using concatenation
      # *** concatenation copies and extends moves & path lists
      queue.append((rr,cc,moves+[dirs[i]],path+[(rr,cc)]))
      visited[rr][cc] = True


# https://stackoverflow.com/questions/73200007/using-breadth-first-search-for-unweighted-edges-in-a-2d-matrix
from collections import deque

def puzzle(board,source,destination):
  cols = len(board[0])
  rows = len(board)
  currentRow,currentCol = source

  # up, down, right, left
  dx = [-1, +1, 0, 0]
  dy = [0, 0 , +1, -1]
  dirs = "UDRL"
  # matrix of true/false
  visited = [[False]*cols for i in range(rows)]
  
  queue = deque()
  # intiate queue with start position
  queue.append((currentRow,currentCol, ""))
  visited[currentRow][currentCol] = True

  while queue:
    r,c,moves = queue.popleft()
    path = (r,c)
    # generate path from moves string when end reached
    if path == destination:
      path = [source]
      r,c = source
      for move in moves:
        # map moves list to board using indices
        i = dirs.index(move)
        r += dx[i]
        c += dy[i]
        path.append((r,c))
      return path, moves
    # generate tree nodes from all possible moves
    for neighbor in range(0,4):
      # children nodes neighboring squares
      rr = r + dx[neighbor]
      cc = c + dy[neighbor]
      # check borders
      if (rr < 0 or cc < 0):
        continue
      if (rr >= rows or cc >= cols):
        continue
      if visited[rr][cc]:
        continue
      # skip squares with #
      if board[rr][cc] == '#':
        continue
      # add child nodes to queue
      # *** concantenate new move to
      # *** copy and extend moves list
      # *** (need to copy for each move)
      queue.append((rr,cc,moves+dirs[neighbor]))
      # toggle child nodes as visited
      visited[rr][cc] = True



links = get_adjacency_list(edges)
print(f"links: {links}")
root = 0
print(f"path: {bfs_tree(root,links)}")

board = [
  [25,24,23,'#',21],
  [20,'#',18,17,16],
  [15,14,13,12,'#'],
  ['#', 9, 8, 7, 6],
  [5, 4, 3, '#', 1]
]

start = (0,0)
end = (4,4)
# moves, path = bfs_board(board,start,end)
# print(f"moves: {moves} path: {path}")

source = (0,0)
destination = (4,4)
maze= [
  ['O', '#', 'O', 'O', 'O'],
  ['O', 'O', 'O', '#', 'O'],
  ['O', '#', '#', 'O', 'O'],
  ['#', 'O', '#', 'O', '#'],
  ['O', '#', '#', 'O', 'O']
]

# path,moves = puzzle(maze,source,destination)
# print(f"moves: {moves} path: {path}")
  
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
