#coding=utf-8
"""
Definition for a undirected graph node
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
        
        cloned_node = UndirectedGraphNode(node.label)

        """
        visited is a hash map which store new graph's nodes with its label as the index
        """
        visited = {}
        visited[node.label] = cloned_node

        queue = deque([node])

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor.label not in visited:
                    queue.append(neighbor)
                    visited[neighbor.label] = UndirectedGraphNode(neighbor.label)
                visited[node.label].neighbors.append(visited[neighbor.label])

        return cloned_node

"""
my solu:
BFS，用一个hashtable来存cloned graph

1) queue用来放original graph里的每个node
2）hashtable存cloned_graph，用unique label来做索引

"""
    def cloneGraph2(self, node):
        # write your code here
        if not node:
            return node
        
        root = UndirectedGraphNode(node.label)  
        hashTable = {}
        hashTable[root.label] = root
        
        queue = deque([node])
        
        while queue:
            cur_node = queue.popleft()
            copied_node = hashTable[cur_node.label]
            for neighbor in cur_node.neighbors:
                if neighbor.label not in hashTable:
                    node = UndirectedGraphNode(neighbor.label)
                    hashTable[node.label] = node
                    queue.append(neighbor)
                copied_node.neighbors.append(hashTable[neighbor.label])
                
        return root

"""
三刷
1）自己定义好数据结构
2）hash table用来存已经访问过的node,并且用来找到被复制的node，用来让其neighbors被copy
"""
#coding=utf-8
"""
Definition for a undirected graph node
"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque

class Solution:
    def cloneGraph(self, root):
        if not root:
            return root

        clone = UndirectedGraphNode(root.label)
        dict_table = {root.label:clone}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor.label not in dict_table:
                    dict_table[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                dict_table[node.label].neighbors.append(neighbor)

        return clone

def printGraph(node):
    q ,vis = [],set([node])
    q.append(node)
    while q:
        cur = q.pop(0)
        print '  ',cur.label
        for i in cur.neighbors:
            print i.label
            if i not in vis:
                q.append(i)
                vis.add(i)
 
 
 
if __name__ ==  '__main__':
    s=Solution()
    one = UndirectedGraphNode(1)
    two = UndirectedGraphNode(2)
    three =UndirectedGraphNode(3)
    one.neighbors.append(one)
    one.neighbors.append(two)
    two.neighbors.append(three)
    #printGraph(one)
    printGraph( s.cloneGraph(one))
