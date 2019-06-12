#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
"""
Use this tree as an example to analyze easily:

               4
              / \
             3   5
            /
           1  
            \
             2
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []

        while root is not None:
        	self.stack.append(root)
        	root = root.left

    def hasNext(self):
    	if len(self.stack) > 0:
    		return True

    def next(self):
        node = self.stack[-1]
        #if node has right -> put right in, and put all left after this right in
        #because the very left one will be the next node
        if node.right:
        	temp = node.right
        	self.stack.append(temp)
        	while temp.left is not None:
        		self.stack.append(temp)
        		temp = temp.left
        else:
        #else, the next node will be the first left parent node
        	temp = self.stack.pop()
             while self.stack and self.stack[-1].right is temp:
             	temp = self.stack.pop()

        return node