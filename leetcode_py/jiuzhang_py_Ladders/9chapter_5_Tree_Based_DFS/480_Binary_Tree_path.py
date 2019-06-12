#coding=utf-8

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
    def binaryTreePaths(self, root):
        if root is None:
            return []

        path = [str(root.val)]
        results = []

        self.dfs(root, results, path)

        return results

    def dfs(self, node, results, path):
        if node.left is None and node.right is None:
            results.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, results, path)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, results, path)
            path.pop()
        

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #root = TreeNode(10)
    root = None
    paths = solu.binaryTreePaths(root)
    print("paths is: ", paths)