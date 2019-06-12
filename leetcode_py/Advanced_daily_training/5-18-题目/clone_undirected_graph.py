#coding=utf-8
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