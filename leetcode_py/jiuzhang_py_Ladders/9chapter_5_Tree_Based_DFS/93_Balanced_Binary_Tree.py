from collections import deque

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def isBalanced(self, root):
        # write your code here
        balanced, _ = self.dfs(root)

        return balanced

    def dfs(self, node):
        if node is None:
            return True, 0

            """
            这里很巧妙，一旦false了，height就永远是0了，这样因为目前height diff已经超过2了，
            set成0后，之后肯定diff更加大，最终返回肯定就是false了
            """
        balanced, leftHeight = self.dfs(node.left)
        if not balanced:
            return False, 0
        
        balanced, rightHeight = self.dfs(node.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1


if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #root = TreeNode(10)
    root = None
    paths = solu.binaryTreePaths(root)
    print("paths is: ", paths)