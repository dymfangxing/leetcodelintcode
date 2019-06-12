# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
1) BFS: put each level's node into the queue and append the last one into result
"""
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        cur_level = deque([root])
        result = []
        
        while cur_level:
            for node in range(len(cur_level)):
                temp = cur_level.popleft()
                if temp.left:
                    cur_level.append(temp.left)
                if temp.right:
                    cur_level.append(temp.right)

            result.append(temp.val)
            
        return result

"""
2) DFS
"""