"""
solu 1: cannot AC 'cuz of TLC
"""

from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque([])
        self.size = size
        #self.total_sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        total_sum = 0.0
        if len(self.queue) < self.size:
            self.queue.append(val)
            #total_sum += self.queue[i for i in range(len(self.queue))]
            for i in range(len(self.queue)):
                total_sum += self.queue[i]
            return total_sum / len(self.queue)

        self.queue.popleft()
        self.queue.append(val)
        #total_sum += self.queue[i for i in range(self.size)]
        for i in range(self.size):
            total_sum += self.queue[i]

        return total_sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)




"""
solu 2: use a global var to remember sum and avoid for loop each time
"""
from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque([])
        self.size = size
        self.total_sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.total_sum += val
            return self.total_sum / len(self.queue)

        discard = self.queue.popleft()
        self.total_sum -= discard
        self.queue.append(val)
        self.total_sum += val

        return self.total_sum / self.size

    def next2(self, val):
        # write your code here
        if len(self.queue) == self.size:
            self.total_sum -= self.queue.popleft()

        self.queue.append(val)
        self.total_sum += val

        return self.total_sum / len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)