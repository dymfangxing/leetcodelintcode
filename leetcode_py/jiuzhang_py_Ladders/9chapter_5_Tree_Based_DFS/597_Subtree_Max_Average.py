#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
hint: 类似max sum of subtree
"""
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        curSum, numOfNodes, maxAverage, node = self.helper(root)
        return node
        
    def helper(self, root):
        if root is None:
            return 0, 0, -sys.maxsize, None
            
        leftSum, numOfLeft, leftMaxAverage, leftNode = self.helper(root.left)
        rightSum, numOfRight, rightMaxAverage, rightNode = self.helper(root.right)
        
        rootSum = leftSum + rightSum + root.val
        numOfRoot = numOfLeft + numOfRight + 1
        rootAverage = rootSum/(numOfRoot)
        
        if leftMaxAverage == max(leftMaxAverage, rightMaxAverage, rootAverage):
            return rootSum, numOfRoot, leftMaxAverage, leftNode
            
        if rightMaxAverage == max(leftMaxAverage, rightMaxAverage, rootAverage):
            return rootSum, numOfRoot, rightMaxAverage, rightNode
            
        return rootSum, numOfRoot, rootAverage, root