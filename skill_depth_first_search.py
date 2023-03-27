from collections import defaultdict

# depth-first search uses an adjacency list representation to traverse and search a graph from a starting node and checking each node once until all unchecked nodes are checked

def depth_first_search():
    # directed graph and adjacency list representation
    class Graph:
        # constructor
        def __init__(self):
	          # default dictionary to store graph
		        self.graph = defaultdict(list)

	      # function to add an edge to graph
        def addEdge(self, u, v):
		        self.graph[u].append(v)

	      # function used by depth-first search
        def DFSUtil(self, v, visited):
		        # mark current node as visited and print
		        visited.add(v)
		        print(v, end=' ')
		        # Recur all adjacent vertices
		        for neighbour in self.graph[v]:
			          if neighbour not in visited:
				            self.DFSUtil(neighbour, visited)

	      # depth-first search traversal using recursive DFSUtil()
        def DFS(self, v):
            # store visited vertices
            visited = set()
            # call recursive DFSUtil() to print traversal
            self.DFSUtil(v, visited)

    # Driver code
    # create graph
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(3)

