"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
Solution 1: back trace/ traversal
"""
class Solution():
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.maxSize = 0
        if not root:
            return 0
        self.dfs(root, 1)
        return self.maxSize

    def dfs(self, root, depth):
        if root is None:
            return
        
        if depth > self.maxSize:
            self.maxSize = depth

        self.dfs(root.right, depth+1)
        self.dfs(root.left, depth+1)

"""
solution 2: divide conquer
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        return self.helper(root)
        
    def helper(self, root):
        if root is None:
            return 0
            
        leftMin = self.helper(root.left)
        rightMin = self.helper(root.right)
            
        return max(leftMin, rightMin) + 1