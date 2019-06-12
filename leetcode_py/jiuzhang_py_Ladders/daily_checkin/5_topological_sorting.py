"""
Definition for a Directed graph node
"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
    	node_indegree = self.getIndegree(graph)
    	"""
    	for node in node_indegree:
    	    print(node_indegree[node])
    	"""
    	start = [x for x in graph if node_indegree[x] == 0]
    	queue = deque(start)
    	order = []

    	while queue:
    		node = queue.popleft()
    		order.append(start)

    		for neighbor in node.neighbors:
    			node_indegree[neighbor] -= 1
    			if node_indegree[neighbor] == 0:
    				queue.append(neighbor)

    	return order

    def getIndegree(self, graph):
    	node_indegree = {x : 0 for x in graph}

    	for node in graph:
            for vertex in node.neighbors:
            	node_indegree[vertex] += 1

    	return node_indegree


if __name__ == '__main__':
    #elems = [3,9,20,"#","#",15,7]
    #elems = [3,9,20,8,2,15,7]
    '''
    creating graph
    '''
    node0 = DirectedGraphNode(0)
    node1 = DirectedGraphNode(0)
    node2 = DirectedGraphNode(0)
    node3 = DirectedGraphNode(0)
    node4 = DirectedGraphNode(0)
    node5 = DirectedGraphNode(0)

    node0.neighbors = [node1, node2, node3]
    node1.neighbors = [node4]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node4, node5]

    graph = [node0, node1, node2, node3, node4, node5]

    '''
    end
    '''
    solu = Solution()

    order = solu.topSort(graph)
    #print("final order is: ", order)