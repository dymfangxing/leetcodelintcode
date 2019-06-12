import heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

#Hint: use heap
#      but make sure that if two nodes' node.val is equal,
#      then heap will compare node, which cannot be compared.
#      so we add a sequence ID to let them compare that 
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return
        heap = []
        dummyNode = traversalNode = ListNode(-1)

        for ll in lists:
            if ll:
                self.heapNodePush(heap, ll)

        while len(heap) > 0:
            node = heapq.heappop(heap)[2]

            traversalNode.next = node
            traversalNode = traversalNode.next
            
            if traversalNode.next:
                self.heapNodePush(heap, traversalNode.next)

        return dummyNode.next

    def heapNodePush(self, heap, node):
        self.sequenceID += 1
        heappush(heap, (node.val, self.sequenceID, node))