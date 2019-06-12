class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
            
        target = self.stack2.pop()
       
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
            
        return target
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack1[0]

