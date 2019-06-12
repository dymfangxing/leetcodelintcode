# -*- coding: utf-8 -*- 
#Hint： 使用一个双向环形链表，把most frequent node放在tail的prev，
#超过capacity时删除head的next
"""
思路：

使用一个双向环形链表，有一个head，一个tail，
head.next永远指向least recent visit node
tail.prev永远指向most recent visit node
再加一个dict存这个node是否存在:key就是node的key，val是这个node。这样当删除的时候，
                            查找要删除的节点的time complexity是O(1)

get()时：当key存在时，先从环形linked list里remove掉这个node，再添加到tail.prev

set()时:当key存在时，先从环形linked list里remove掉这个node，再添加到tail.prev
        当key不存在时，创建node，加到dict里去，然后
              若len(hash) < capacity, 直接加环形链表的tail.prev
              若len(hash) == capacity, 先删掉head.next,再添加到tail.prev

所以还需要2个helper函数：removeNode() 和 pushToTail()
"""

class doubleLinkedList:
    def __init__(self, key=None, val=None, prev=None, next=None):
        # do intialization if necessary
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hashMap = {}#use key to fetch node in linkedlist
        self.head = doubleLinkedList(-1, -1)
        self.tail = doubleLinkedList(-1, -1)
        """
        注意！！环形链表，头尾要互相连
        """
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]
        self._remove_node(node)
        self._move_to_tail(node)

        return node.val

    def set(self, key, value):
        # write your code here
        if key in self.LRUDict:
            node = self.LRUDict[key]
            node.val = value
            self._removeNode(node)
            self._pushToTail(node)
        else:
            if len(self.LRUDict) == self.capacity:
                del self.LRUDict[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                
            node = DoubleLinkedList(key, value)
            self.LRUDict[key] = node
            self._pushToTail(node)

    def _move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next =node
        node.next = self.tail

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev




class DoubleLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.head = DoubleLinkedList(None, None)
        self.tail = DoubleLinkedList(None, None)
        self.tail.prev = self.head
        self.head.next = self.tail
        
        self.LRUDict = {}
        self.capacity = capacity

    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pushToTail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
        
    
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.LRUDict:
            return -1
        
        node = self.LRUDict[key]
        self._removeNode(node)
        self._pushToTail(node)

        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.LRUDict:
            node = self.LRUDict[key]
            node.val = value
            self._removeNode(node)
            self._pushToTail(node)
        else:
            if len(self.LRUDict) == self.capacity:
                del self.LRUDict[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                
            node = DoubleLinkedList(key, value)
            self.LRUDict[key] = node
            self._pushToTail(node)

