#coding=utf-8

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
Hint: 请用lowerBound/upperBound的方法

Solu 1: DFS

Solu 2: BFS iterators
Use two stacks from:

a) left
b) right

to traverse elements and put into results array
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):


"""
solu 1: 暴力法：用inorder把tree存入一个array（这样空间和时间都O(n)了）。
        然后像做460：find k closest elements那样左右指针移动找值

        找到最后一个小于target的值，然后两边扩散
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        nums =[]
        self.inorder(root, nums)
        left = self.findLeftIndex(nums, target)
        right = left + 1
        results = []
        for _ in range(k):
            if self.isLeftCloser(nums, left, right, target):
                results.append(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1
        return results

    def isLeftCloser(self, arr, left, right, target):
        if left < 0:
            return False
        if right >= len(arr):
            return True

        return abs(arr[left] - target) <  abs(arr[right] - target)

    """
    这是最后一个< target的值
    """
    def findLeftIndex(self, arr, target):
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right)//2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid
                
        if arr[right] < target:
            return right
        
        if arr[left] < target:
            return left
            
        return -1

    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)


"""
solu 0: use heapq
"""

import heapq

class Solution0:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.queue = []
        self.helper(root, target)
        
        result = []
        
        while k > 0:
            _, val = heapq.heappop(self.queue)
            result.append(val)
            k -= 1
        return result
        
    def helper(self, root, target):
        if root:
            self.helper(root.left, target)
            heapq.heappush(self.queue, (abs(root.val - target), root.val))
            self.helper(root.right, target)