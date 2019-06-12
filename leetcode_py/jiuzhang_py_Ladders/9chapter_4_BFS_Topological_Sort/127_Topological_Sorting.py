#coding=utf-8

from collections import deque

'''
neighbors means every node's out-degree
we have to first get a in-degree array depends on neighbors (edges) 
'''
#Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
neighbors = []

这个node指向的邻居列表
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
    # write your code here
        node_to_indegree = self.get_indegree(graph)
        
        for x in node_to_indegree:
            print("3: node to indegree is: ", x, node_to_indegree[x])

        start = [x for x in graph if node_to_indegree[x] == 0]
        print("start is: ", start)
        queue = deque(start)
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            #print("this node neighbors are: ", node.neighbors)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}
        '''
        for x in node_to_indegree:
            print("1: node to indegree is: ", x, node_to_indegree[x])
        '''

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
                
        return node_to_indegree
    
"""
二刷
"""

from collections import deque

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        results = []
        indegree = self.get_indegree(graph)

        start = deque(list())

        for node in graph:
            if indegree[node] == 0:
                start.append(node)

        while start:
            node = start.popleft()
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    start.append(neighbor)

            results.append(node)

        return results


    def get_indegree(self, graph):
        indegree = {x : 0 for x in graph}

        for x in graph:
            for neighbor in x.neighbors:
                indegree[neighbor] += 1

        return indegree
        
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