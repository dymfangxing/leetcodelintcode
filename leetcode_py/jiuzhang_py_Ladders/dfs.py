#This graph looks like:
#              0
#             / \
#            1   2
#           /   / \
#          3   5   4
#                   \
#                    6
vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

#another example use set to generate graph with a hash
#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs_withSet(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited) #this line do the for loop does in another example
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
#
def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]
    #adjacencyList is now [[],[],[],[],[],[]]
    print(len(edgeList))


#This adjacenctList is like a graph structure:
#graph = {0:[1,2], 1:[0, 3], 2:[0, 4, 5], 3:[1], 4:[2,6], 5:[2], 6:[4]}
#
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
        #adjacencyList[edge[0]] means each vertex's index in adjacencyList
        #append(edge[1]) means append each edge's (a tuple) value
        #into each vetex
        print("adjacencyList is: ", adjacencyList)

    while stack:
    	#check if current has child, 
    	#if so, put them into stack
    	#then append current into visitedVertex list
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

#dfs(graphs, 0)
print(dfs(graphs, 0))

graph1 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(dfs_withSet(graph1, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}

