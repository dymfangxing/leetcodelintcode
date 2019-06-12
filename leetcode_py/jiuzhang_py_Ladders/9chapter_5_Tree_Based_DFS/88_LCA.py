"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#https://www.jiuzhang.com/solutions/lowest-common-ancestor#tag-highlight-lang-python
#hint: divide and conquer.
#4 conditions
#divide into 2 subtrees, if left is not none, return left;
#if right is not none, return right
#if A&B at left and right, return root
#if A or B is root, return root

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
用这个答案： divide and conquer
"""
def lowestCommonAncestor(self, root, A, B):
    # write your code here
    if root is None:
        return None
        
    left = self.lowestCommonAncestor(root.left, A, B)
    right = self.lowestCommonAncestor(root.right, A, B)

    if root is A or root is B:
        return root
        
    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    if right is not None:
        return right
    return None

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None

        #No brainer divided tree into 2 subtrees
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        #condition 1: root is A or root is B, return root
        if root is A or root is B:
            return root
        #condition 2: if find node in both left and right, means ancestor is root
        if left is not None and right is not None:
            return root
        #condition 3: if only left has ancestor, return left
        if left is not None:
            return left
        #condition 4: if only right has ancestor, return right
        if right is not None:
            return right

"""
九章算法的答案
"""
    def lowestCommonAncestor(self, root, A, B):
        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B
        if root is None:
            return None
        
        if root == A or root == B:
            return root
        
        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)
        
        # A 和 B 一边一个
        if left_result and right_result: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result
        
        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result
        
        # 左右子树啥都没有
        return None