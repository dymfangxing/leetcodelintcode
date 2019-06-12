"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
solu 1: BFS
"""
from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        queue = deque(list([root]))
        results = []
        
        while queue:
            level_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_result.append(node.val)
            results.append(level_result)
        
        return results


"""
solu 2: DFS: 回溯法，传入当前node depth：
1）当depth > 当前层数时，results里加入新的一层空array
2）每个遍历到的node都加入其对应的层数的array里: results[depth - 1].append(root.val)
"""
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        results = []

        if not root:
            return results
        
        self.helper(root, 1, results)
        return results

    def helper(self, root, depth, results):
        if depth > len(results):
            results.append([])
        results[depth - 1].append(root.val)
        if root.left:
            self.helper(root.left, depth + 1, results)

        if root.right:
            self.helper(root.right, depth + 1, results)
