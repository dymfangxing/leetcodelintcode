"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
hint: use BST inorder traversal is inorder feature
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.lastValue = None
        self.isBST = True
        self.helper(root)
        return self.isBST
        
    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        if self.lastValue is not None and self.lastValue >= root.val:
            self.isBST = False
            return
        self.lastValue = root.val
        self.helper(root.right)
        
"""
solu 2：我的解法：与上面一样，但需要注意：flag and lastVal都需要是global的！而不是局部变量传参进去
这个类似于inorder时候的存每个节点的result array，但因为array是传值进去的，可以作为参数传进去
如果只是个变量，传进去的是引用
"""     
    def isValidBST(self, root):
        # write your code here
        self.flag = True
        self.lastVal = None
        
        if root is None:
            return self.flag
            
        self.helper(root)
        return self.flag
        
    def helper(self, root):
        if root:
            self.helper(root.left)
            if self.lastVal is not None:
                if root.val <= self.lastVal:
                    self.flag = False
                    return
            self.lastVal = root.val
            self.helper(root.right)