__author__ = 'Minsuk Heo'

import collections

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

#This graph looks like:
#              0
#             / \
#            1   2
#           /   / \
#          3   5   4
#                   \
#                    6

def bfs_deque(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = collections.deque([start])

    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    #This adjacenctList is like a graph structure:
    #graph = {0:[1,2], 1:[0, 3], 2:[0, 4, 5], 3:[1], 4:[2,6], 5:[2], 6:[4]}
    #
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                #queue.insert(0,neighbor)
                queue.appendleft(neighbor)
        visitedList.append(current)
    return visitedList

def bfs_defaultdict(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    #with defaultdict, u don't have to create empty []s before add nodes into it
    #adjacencyList = [[] for vertex in vertexList]
    #so basicly we only need edgeList to create this graph
    adjacencyList = collections.defaultdict(list)

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
        print("adjacencyList is: ", adjacencyList)
    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

#print(bfs(graphs, 0))
#print(bfs_deque(graphs, 0))
print(bfs_defaultdict(graphs, 0))