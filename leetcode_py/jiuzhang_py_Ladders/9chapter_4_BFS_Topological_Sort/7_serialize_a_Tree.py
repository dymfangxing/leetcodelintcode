#coding=utf-8

from collections import deque

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return ""
            
        queue = deque([root])
        results = []
        
        
        while queue:
            node = queue.popleft()
        """
        一次性把左右子树都提出来，清掉
        """
            if node:
                results.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                results.append(None)
                
        return results
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
            
        root = TreeNode(data.pop(0))
        queue = deque([root])
       

        while data:
            cur_node = queue.popleft()
        """
        一次性把左右子树都填上
        """
            left_val = data.pop(0)
            
            if left_val:
                left_node = TreeNode(left_val)
                cur_node.left = left_node
                queue.append(left_node)
                
            right_val = data.pop(0)
            
            if right_val:
                right_node = TreeNode(right_val)
                cur_node.right = right_node
                queue.append(right_node)
                
        return root
        
if __name__ == '__main__':
    #elems = [3,9,20,"#","#",15,7]
    #elems = [3,9,20,8,2,15,7]
    elems = [1,"#",2]
    solu = Solution()

    root = solu.deserialize(elems)
    data = solu.serialize(root)
    print("final data is: ", data)