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
        self.LRUDict = dict()
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.LRUDict:
            return -1
        
        node = self.LRUDict(key)
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
            node = self.LRUDict(key)
            self._removeNode(node)
            node.val = value
            self._pushToTail(node)
        else:
            node = DoubleLinkedList(key, val)
            self.LRUDict[key] = node

            if len(self.LRUDict) == self.capacity:
                headNext = head.next
                head.next = headNext.next
                headNext.next.prev = head

                headNext.next = None
                headNext.prev = None
                del self.LRUDict[headNext.key]

                _pushToTail(node)
            else:
                self._pushToTail(node)

    def _removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.prev, node.next = None, None

    def _pushToTail(self, node):
        tailPrev = self.tail.prev
        node.next = self.tail
        node.prev = tailPrev
        tailPrev.next = node
        self.tail.prev = node
