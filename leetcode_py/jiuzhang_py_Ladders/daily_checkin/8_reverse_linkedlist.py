#coding=utf-8
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solu:
    def reverse1(self, head):
        cur = None

        while head:
            temp = head.next
            head.next = cur
            cur = head
            head = temp

        return cur