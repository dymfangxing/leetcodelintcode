# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
输入一个二叉树，问任意一个节点和他的祖先节点的最大的差是多少
"""

"""
Hint:

1) 由于每个节点和祖先节点的最大的差，一定出现在当前节点的min(Ancestor)和max(Ancestor)之间
2) 所以这个可以用dfs来做，每次递归的时候，把目前遇到的最小值和最大值传给子节点，就可以在一次遍历的时候找到需要求解的结果

"""

"""
solu 1: 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.maxDiff = 0
        self.dfs(root, root.val, root.val)
        
        return self.maxDiff

    def dfs(self, root, maxVal, minVal):
        if root is None:
            return

        diff1 = abs(root.val - maxVal)
        diff2 = abs(root.val - minVal)

        self.maxDiff = max(self.maxDiff, diff1, diff2)

        self.dfs(root.left, max(root.val, maxVal), min(root.val, minVal))
        self.dfs(root.right, max(root.val, maxVal), min(root.val, minVal))