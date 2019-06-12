#coding=utf-8
"""
九章算法：https://www.jiuzhang.com/tutorial/algorithm/403
"""
"""
Preorder

思路
遍历顺序为根、左、右

1. 如果根节点非空，将根节点加入到栈中。
2. 如果栈不空，弹出出栈顶节点，将其值加加入到数组中。
     i. 如果该节点的右子树不为空，将右子节点加入栈中。
     ii. 如果左子节点不为空，将左子节点加入栈中。
3. 重复第二步，直到栈空。
"""
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        stack = []
        preorder = []

        if not root:
            return preorder

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return preorder

"""
附 recursive解法：
"""
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        self.preorder = []
        self.helper(root)
        
        return self.preorder
        
    def helper(self, root):
        if root is None:
            return
        
        self.preorder.append(root.val)
        self.helper(root.left)
        self.helper(root.right)


"""
Inorder：

遍历顺序为左、根、右

其实就是BST Iterator

1. 如果根节点非空，将根节点加入到栈中。
2. 如果栈不空，取栈顶元素（暂时不弹出），
   i. 如果左子树已访问过，或者左子树为空，则弹出栈顶节点，将其值加入数组，如有右子树，将右子节点加入栈中。
   ii. 如果左子树不为空，则将左子节点加入栈中。
3.重复第二步，直到栈空。

"""
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        stack = []
        inorder = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            """
            每次拿栈底元素的值
            """
            inorder.append(node.val)

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                """
                如果stack[-1].right == node，即node是stack[-1]的右节点，
                那说明stack[-1]已经visit过啦，所以直接弹出，不要计算了
                """
                while stack and stack[-1].right == node:
                    node = stack.pop()

        return inorder
"""
附 recursive解法：
"""
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        self.result = []
        self.helper(root)
        
        return self.result
        
    def helper(self, root):
        if not root:
            return
        
        self.helper(root.left)
        self.result.append(root.val)
        self.helper(root.right)

"""
Postorder: 

思路
遍历顺序为左、右、根

1. 如果根节点非空，将根节点加入到栈中。

2. 如果栈不空，取栈顶元素（暂时不弹出），

   i. 如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），
   则弹出栈顶节点，将其值加入数组，

   ii. 如果左子树不为空，切未访问过，则将左子节点加入栈中，并标左子树已访问过。

   iii. 如果右子树不为空，切未访问过，则将右子节点加入栈中，并标右子树已访问过。

3. 重复第二步，直到栈空。
"""
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
"""
巧妙方法：把postOrder reverse一下：

postorder是：

self.helper(root.left)
self.helper(root.right)
root.val

那么reverse就是：
root.val
self.helper(root.right)
self.helper(root.left)

这不就和preorder很像了嘛：

所以stack里先放root，再放left，再放right

最后的result再reverse一下就搞定啦

还可以用deque来存results，appendleft来添加element，因为deque是双向链表，这样不用reverse了.

思路来自花花的解法：https://www.youtube.com/watch?v=A6iCX_5xiU4
"""
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                               
        result.reverse()
        
        return result
"""
deque的解法
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        result = deque()
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.appendleft(node.val)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)

        return list(result)

"""
附 recursive解法：
"""
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        self.results = []
        self.helper(root)
        
        return self.results
        
    def helper(self, root):
        if not root:
            return
        
        self.helper(root.left)
        self.helper(root.right)
        self.results.append(root.val)