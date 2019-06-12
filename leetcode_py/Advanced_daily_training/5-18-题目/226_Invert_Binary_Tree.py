#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):

"""
BFS
"""
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root
            
"""
recursive: preorder
"""
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
            return None
        
        temp = root.right
        root.right = root.left
        root.left = temp
        
        left = self.helper(root.left)
        right = self.helper(root.right)