#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
solu0: divided and conquer:

思路：
    root
    /  \
 left  right

1）左子树的尾节点指向右子树
2）根节点的右节点指向左子树 
3）根节点左子树指向None

merge的时候，先判断有没有leftTail，
有的话，先把leftTail放到右边
再看右边有没有，有就返回
要是没有，就返回这个左边的
要是都木有，就返回root
"""
    def flatten(self, root):
        # write your code here
        if root is None:
            return root
        self.helper(root)
        
        
    def helper(self, root):
        if root is None:
            return
        
        leftTail = self.helper(root.left)
        rightTail = self.helper(root.right)
        
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            
        root.left = None     
"""
注意：有rightTail要先返回rightTail,
"""
        if rightTail:
            return rightTail
        if leftTail:
            return leftTail
        return root
"""
solu1: traversal
"""
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    last_node = None

    def flatten(self, root):
        # write your code here

        if root is None:
        	return None
        
        if self.last_node is not None:
            self.last_node.right = root
            self.last_node.left = None

        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right) 

"""
solu2: BFS: Tricky. use stack, push right then left
"""
    def flatten(self, root):
        # write your code here
        if root is None:
            return root
            
        queue = [root]
        
        while queue:
            node = queue.pop()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

            node.left = None
            if len(queue) == 0:
                node.right = None
            else:
                node.right = queue[-1]