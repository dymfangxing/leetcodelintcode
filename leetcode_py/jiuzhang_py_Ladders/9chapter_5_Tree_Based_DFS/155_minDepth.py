#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        return self.helper(root)
        
    def helper(self, root):
        if root is None:
            return 0
            
        leftMin = self.helper(root.left)
        rightMin = self.helper(root.right)
        
        """
        如果一边没有叶子节点，那不管怎么样都要另一边的depth
        """
        if leftMin == 0 and rightMin != 0:
            return rightMin + 1
        if rightMin == 0 and leftMin != 0:
            return leftMin + 1
            
        return min(leftMin, rightMin) + 1