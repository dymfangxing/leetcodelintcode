"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
"""
Hint: Actually I prefer this JACA solution since it is easier to understand:

link:
https://www.jiuzhang.com/solutions/lowest-common-ancestor-iii#tag-other-lang-java

Also paste it in below python solution
"""

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if root is None:
            return None

        FoundA, FoundB, LCA_node = self.helper(self, root, A, B)

        if FoundA and FoundB:
            return LCA_node
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        leftFoundA, leftFoundB, leftNode = helper(root.left, A, B)
        rightFoundA, rightFoundB, rightNode = helper(root.left, A, B)

        FoundA = leftFoundA or rightFoundA or leftNode == root
        FoundB = leftFoundB or rightFoundB or rightNode == root

        #condition 1: root is A or B
        if root == A or root == B:
            return FoundA, FoundB, root

        #condition 2: Each A and B is at left/right, return root
        if leftNode is not None and rightNode is not None:
            return FoundA, FoundB, root
        #condition 3: Only A or B is found, return that node
        if leftNode is not None:
            return FoundA, FoundB, leftNode
        if rightNode is not None:
            return FoundA, FoundB, rightNode
        #condition 4: found nothing
        return FoundA, FoundB, None


#Use global var solu
class Solution2:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.foundA = False
        self.foundB = False
        
        result = self.helper(root, A, B)
        
        if self.foundA and self.foundB:
            return result
        else:
            return None
            
    def helper(self, root, A, B):
        if root is None:
            return None

        #No brainer divided tree into 2 subtrees
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)

        #condition 1: root is A or root is B, return root
        if root is A or root is B:
            self.foundA = self.foundA or root == A
            self.foundB = self.foundB or root == B
            return root
        #condition 2: if find node in both left and right, means ancestor is root
        if left is not None and right is not None:
            return root
        #condition 3: if only left has ancestor, return left
        elif left is not None:
            return left
        #condition 4: if only right has ancestor, return right
        elif right is not None:
            return right
        #nothing at left/right
        else:
            return None

"""
三刷:使用全局变量但是更容易懂：
"""
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.foundA = False
        self.foundB = False

        result = self.helper(root, A, B)
        
        if self.foundA and self.foundB:
            return result
        else:
            return None
        
        
    def helper(self, root, A, B):
        if root is None:
            return None

        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        
        if root is A:
            self.foundA = True
            return root
        if root is B:
            self.foundB = True
            return root
            
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right

        return None