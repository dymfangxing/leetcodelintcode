#graph defines as:
#{
# 1: set([2, 4]), 
# 2: set([1, 3]), 
# 3: set([2, 4]), 
# 4: set([1, 3])
#}
from collections import defaultdict
import copy

def circle_dectector(graph, initNode):
    graph = copy.deepcopy(graph)

    stack = [initNode]
    visited = set()

    #dfs
    while stack:
    	print stack
    	vertex = stack.pop()
    	visited.add(vertex)
        edges = graph[vertex]
        for edge in edges:
            if edge in visited:
                return True
            else:
        	    stack.append(edge)
        	    #because it is mutual, so if you append this edge in 
        	    #stack, u have to remove vertex from its graph
        	    graph[edge].remove(vertex)

    return False


def build_graph(edges):
    '''
    graph={}
    for from_point,to_point in edges:
        if from_point not in graph:
            graph[from_point]=set()
        if to_point not in graph:
            graph[to_point]=set()
        graph[from_point].add(to_point)
        graph[to_point].add(from_point)
    '''
    graph = defaultdict(set)
    for from_point,to_point in edges:
    	graph[from_point].add(to_point)
    	graph[to_point].add(from_point)
    return graph
        
#edges=[[1,2],[2,3],[3,4],[4,1]]
edges=[[1,2],[2,3],[3,4],[4,5]]
graph=build_graph(edges)
print "graph is: ", graph
print "if it is a cycle: ", circle_dectector(graph, 1)
#print(circle_dectector(edges),1)
print graph
