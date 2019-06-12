# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        
        return root
    
    def helper(self, root):
        if root is None:
            return root
        
        root.left, root.right = root.right, root.left
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
