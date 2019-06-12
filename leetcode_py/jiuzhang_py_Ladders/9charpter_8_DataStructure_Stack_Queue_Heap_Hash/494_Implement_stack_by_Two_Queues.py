from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque([]])
        self.queue2 = deque([])
        #queue1 = []
        #queue2 = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if self.isEmpty():
            return

        while len(self.queue1) > 1:
            temp = self.queue1.popleft()
            self.queue2.append(temp)

        result = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.isEmpty():
            return
        
        return self.queue1[len(self.queue1) - 1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not len(self.queue1)
