from collections import deque
import sys

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        minimum, subtree, sum_val = self.helper(root)
        return subtree
"""
这种是travesal通用写法，就是把binary tree全部遍历过一遍，所以叫traversal
过一遍，然后一个个情况处理一下

要返回subtree_sum,因为这个subtree_sum有可能后面的sum是要用的
"""
    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0
        #no brain divide into left and right
        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)
        
        sum_val = left_sum + right_sum + root.val
        #left is min
        if left_minimum == min(left_minimum, right_minimum, sum_val):
            return left_minimum, left_subtree, sum_val
        #right is min
        if right_minimum == min(left_minimum, right_minimum, sum_val):
            return right_minimum, right_subtree, sum_val
        #root is min
        return sum_val, root, sum_val

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #root = TreeNode(10)
    root = None
    paths = solu.findSubtree(root)
    print("paths is: ", paths)