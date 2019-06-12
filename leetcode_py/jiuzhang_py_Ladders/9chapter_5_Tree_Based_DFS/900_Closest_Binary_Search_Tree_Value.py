"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
这种是travesal通用写法，就是把binary tree全部遍历过一遍，所以叫traversal
过一遍，然后一个个情况处理一下

Hint:先走到最左边，记住最小值
     对应的node，然后逐个遍历每个node对比是否有更小的

     注意：如果node不存在，返回sys.maxsize，防止不能访问None node的val 
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return sys.maxsize
        #no brain divide into left and right
        leftCloset = self.closestValue(root.left, target)
        rightCloset = self.closestValue(root.right, target)
        
        leftDiff = abs(leftCloset - target)
        rightDiff = abs(rightCloset - target)
        rootDiff = abs(root.val - target)

        #left is closer
        if leftDiff == min(leftDiff, rightDiff, rootDiff):
            return leftCloset
        #right is closer   
        if rightDiff == min(leftDiff, rightDiff, rootDiff):
            return rightCloset
        #root is closer  
        return root.val