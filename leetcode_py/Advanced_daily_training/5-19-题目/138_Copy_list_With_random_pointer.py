#coding=utf-8

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        cur = head
        """
        1) 在每个node后插入cloned node',但其random pointer指向None
        """ 
        while cur:
            node = Node(cur.val, None, None)
            node.next = cur.next
            cur.next = node
            cur = node.next
        """
        2) 给每个cloned node'的random pointer指向需要的node（当其random pointer指向某个node时）
        """ 
        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next


        """
        3) 断开每个cloned node'与原node的连接
        """
        cur = head
        clone = head.next

        while cur:
            temp = cur.next
            cur.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            cur = cur.next

        return clone


    def copySingleList(self, head):        
        copy = Node(head.val)
        temp = copy

        while head:
            head = head.next
            node = Node(head.val)
            temp.next = node
            temp = temp.next

        return copy
