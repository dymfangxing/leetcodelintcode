#coding=utf-8
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
"""
思路：把A所有可能的parent都放到一个dict里，然后遍历B的所有可能parent，返回第一个与A重复的node
如果一个都木有，就返回root
"""

class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        if not root:
            return
        
        dict_table = {}

        while A is not root:
            dict_table[A] = True
            A = A.parent

        while B is not root:
            if B in dict_table:
                return B
            B = B.parent 

        return root

