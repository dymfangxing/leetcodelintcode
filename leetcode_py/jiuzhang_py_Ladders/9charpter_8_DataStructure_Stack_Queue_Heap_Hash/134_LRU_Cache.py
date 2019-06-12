# -*- coding: utf-8 -*- 
"""
用双指针的版本，比较容易理解
Hint:
https://www.jianshu.com/p/537fb52872c9
https://www.youtube.com/watch?v=8j4nHj92uRA
1)如果满了，删掉最尾端的元素
2）recent visit元素在head
"""

"""
1)set的pair总在最head
2)get将后面的pair移动到head
3)当set时，若capacity已满，pop out tail的pair，再将pair加到head

solu1:
无论set/get，只要有值，都需要重新排序: HashMap + double-linkedlist

solu2:
use single linkedlist: hash map always remembers cur node's prev node
"""
"""
HashMap + Linkedlist(node)

node's key is HashMap's key, which is used to find this node in HashMap;
so when you push a node into LRU:
Be aware that key maps with curr tail, so tail.next will always be the node
we are looking for (or we won't be able to remove it)

push: push node to the end

self.hashMap[node.key] = self.tail
self.tail.next = node
self.tail = self.tail.next

pop: pop the head node out

get(): if has it, find it in linkedlist by HashMap, pop() to the end 
       if not have it, return None
set(): if not have it:
                      if capacity not full, add new to the end
                      or if capacity is full, pop up head, add new to end


head does not store any val, tail stores val 
"""


"""
Try it with bi-dirctional linkedlist?
should be easier
"""
class LinkedNode(object):
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.head = LinkedNoe()
        self.head = self.tail
        self.Hash_table = {}
        self.capacity = capacity

    def pushBack(self, node):
        self.Hash_table[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    #if capacity is full, pop head out
    def popFront(self):
        del self.Hash_table[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash_table[self.head.next.key] = self.head

    def kickToTail(self, prev):
        node = prev.next

        if node == self.tail:
            return

        prev.next = node.next
        self.hash[node.next.key] = prev
        node.next = None
        self.pushBack(node)


    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):


"""
class LinkedNode(object):

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        self.hash_table = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

#push: push node to tail
    def push(self, node):
        self.hash_table[node.key] = self.tail
        self.tail.next = node
        self.tail = node

#pop: pop head node out    
    def pop(self):
        del self.hash_table[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash_table[self.head.next.key] = self.head

#visit: if node exists, move it to head
    def visit(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next:
            self.hash_table[node.next.key] = prev
            node.next = None
        self.push(node)

#if not exists, return -1; else, move it to head and return val
    def get(self, key):
        if key not in self.hash_table.keys():
            return -1
        self.visit(self.hash_table[key])
        return self.hash_table[key].next.value

#if key exists, reset val; else,  
    def set(self, key, value):
        if key in self.hash_table.keys():
            self.visit(self.hash_table[key])
            self.hash_table[key].next.value = value
        else:
            self.push(LinkedNode(key, value))
            if len(self.hash_table) > self.capacity:
                self.pop()
"""
        # write your code here

