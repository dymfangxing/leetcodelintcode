#coding=utf-8


"""
Implementation of BIT (Binary Indexed Tree)
"""

"""
对self.BIT来说，

当i是奇数：BIT[i] =A[i]
当i为偶数时：
     如果i是2的整数幂（2，4，8，16，32，。。。），
     BIT[i] = A[0] + A[1] + A[2] + ... + A[i - 1]
     
     否则，BIT[i] = A[i] + A[i - 1]
"""

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0 for i in range(len(nums))]
        self.bitree = [0 for i in range(len(nums) + 1)]
        
        #Initicate with updating bitree array using self.update
        for i in range(len(nums)):
            self.update(i, nums[i])
            

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[i]
        self.arr[i] = val
        index = i + 1
        
        while index <= len(self.arr):
            self.bitree[index - 1] += delta
            index += self.lowbit(index)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getPrefixSum(j) - self.getPrefixSum(i - 1)
        
    def getPrefixSum(self, i):
        sum = 0
        index = i + 1 
        while index > 0:
            sum += self.bitree[index - 1]
            index -= self.lowbit(index)
            
        return sum 
        
    def lowbit(self, x):
        return x&(-x)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)