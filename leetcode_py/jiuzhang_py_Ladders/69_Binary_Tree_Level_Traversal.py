"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#Hint: only use one queue, you have to remember the length of 
#each level and only

from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        queue = deque(list([root]))
        results = []
        
        while queue:
            level_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_result.append(node.val)
            results.append(level_result)
        
        return results
