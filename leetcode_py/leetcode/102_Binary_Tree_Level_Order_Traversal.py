#coding=utf-8
# Definition for a binary tree node.
#reference： https://blog.csdn.net/Bone_ACE/article/details/46718683

#BFS
#coding=utf-8
from collections import deque
"""
在构建Tree时请用deque，因为要pop queue里的第一个元素，造成全部左移，时间复杂度O(N)
实际上，只要用Queue，就用deque
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque(list())

    def add(self, val):
        node = TreeNode(val)

        if self.root is None:
            self.root = node
            self.queue.append(node)
        else:
            temp = self.queue[0]
            if temp.left == None:
                temp.left = node
                self.queue.append(node)
            elif temp.right == None:
                temp.right = node
                self.queue.append(node)
                self.queue.popleft()

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        queue = deque([root])
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


if __name__ == '__main__':
    elems = [3,9,20,None,None,15,7]
    #elems = [3,9,20,8,2,15,7]

    tree = Tree()          #新建一个树对象

    for elem in elems:                  
        tree.add(elem)           #逐个添加树的节点

    solu = Solution()
    print(solu.levelOrder(tree.root))