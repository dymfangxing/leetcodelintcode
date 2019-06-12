#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
1) BFS: put each level's node into the queue and append the last one into result
"""
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        cur_level = deque([root])
        result = []
        
        while cur_level:
            for node in range(len(cur_level)):
                temp = cur_level.popleft()
                if temp.left:
                    cur_level.append(temp.left)
                if temp.right:
                    cur_level.append(temp.right)

            result.append(temp.val)
            
        return result

"""
2) DFS: 需要一个全局maxDepth记录当前maxDepth，先遍历右子节点，再遍历左边
如果当前depth > maxDepth,则将该节点push进queue，更新maxDepth
"""

class Solution(object):
    def __init__(self):
        self.maxDepth = 0
        self.result = []

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        "当root不为None时，maxDepth为1，以此开始，同时传入当前节点的depth"
        self.dfs(root, 1)
        
        return self.result
    
    def dfs(self, root, depth):
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.result.append(root.val)

        if root.right:
            """
            回溯，也可以直接写成：
            self.dfs(root.right, depth + 1)
            """
            depth += 1
            self.dfs(root.right, depth)
            depth -= 1

        if root.left:
            depth += 1
            self.dfs(root.left, depth)
            depth -= 1

"""
优化一下，用len(result)来表示当前maxDepth，当depth > len(result)时，add node：
"""
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        self.dfs(root, 1, result)
        
        return result
    
    def dfs(self, root, depth, result):
        if depth > len(result):
            result.append(root.val)

        if root.right:
            self.dfs(root.right, depth+1, result)

        if root.left:
            self.dfs(root.left, depth+1, result)
