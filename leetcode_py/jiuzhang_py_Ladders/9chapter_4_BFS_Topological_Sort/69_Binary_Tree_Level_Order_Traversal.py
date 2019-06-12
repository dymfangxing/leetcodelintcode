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
        self.queue = deque(list())#deque([]) is also OK

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

"""
solu 1: BFS
"""
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



if __name__ == '__main__':
    elems = [3,9,20,None,None,15,7]
    #elems = [3,9,20,8,2,15,7]

    tree = Tree()

    for elem in elems:                  
        tree.add(elem)

    solu = Solution()
    print(solu.levelOrder(tree.root))
