#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


"""
Interviewer will ask you to use non-recursive way becuase recursive way 
may cause stack overflow if depth is too much
"""

"""
solu 0: Naivly use a list A to store BST nodes inorder, then return A[k - 1]
"""
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        result = []
        self.helper(root, result)
        if len(result) < k:
            return None
        
        return result[k - 1]
        
    def helper(self, root, result):
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)
"""
solu 1: BST iterator
"""
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
    """
        resursively traverse this BST k-1 elements, then return kth element
    """
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
    """
    每个loop时，stack[-1]是我们要的数
    """
        for i in range(k - 1):
            node = stack[-1]

            if node.right is not None:
                n = node.right
                while n is not None:
                    stack.append(n)
                    n = n.left
            else:
                n = stack.pop()
    """
    如果right没有值，先弹出stack里最后一个数。然后要继续弹，因为里面有的数之前已经用过啦
    要弹出stack里的数。弹多少呢？
    要一直弹到stack[-1].right != 刚弹出来那个数

    为啥呢？
    因为之前当right有值的时候，是先把right放进来的，然后再接下去添加更多数。所以这时的right上面那个
    root已经被用过啦。所以这次要一次性都弹出去

    因为这个数可能不止一个，所以要用while一直弹
    """
                while stack and stack[-1].right == n:
                    n = stack.pop()
            """
            it means k >  # of nodes in this BST
            """
            if stack is None:
                return

        return stack[-1].val

"""
solu2: Recursive Use traverse: No advantage since it will also use O(n) space

Kinda like quickSelect

Need a dict to first get every node's num of child nodes.

Then use inOrder traverse, always check root node's left node's numOfChild

if left numOfChild + 1 == k
    found
if left numOfChild + 1 > k
    target node is on left, pass root.left 

if left numOfChild + 1 < k
    target node is on right, pass root.right and k - (left numOfChild + 1) to find
    the rest of the missing nodes.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if root is None:
            return root
        numOfNodes = {}
        self.countNodes(root, numOfNodes)
        result = self.findKsmallest(root, k, numOfNodes)
        
        return result.val
        
    def countNodes(self, root, numOfNodes):
        if root is None:
            return 0
            
        leftCnt = self.countNodes(root.left, numOfNodes)
        rightCnt = self.countNodes(root.right, numOfNodes)
        
        numOfNodes[root] = leftCnt + rightCnt + 1
        
        return leftCnt + rightCnt + 1
        
    def findKsmallest(self, root, k, numOfNodes):
        if root is None:
            return None
            
        if root.left is not None:
            leftChildrenNum = numOfNodes[root.left]
        else:
            leftChildrenNum = 0
            
        if k == leftChildrenNum + 1:
            return root 
            
        if leftChildrenNum + 1 > k:
           return self.findKsmallest(root.left, k, numOfNodes)
                    
           
        if leftChildrenNum + 1 < k:
            return self.findKsmallest(root.right, k - leftChildrenNum - 1, numOfNodes)