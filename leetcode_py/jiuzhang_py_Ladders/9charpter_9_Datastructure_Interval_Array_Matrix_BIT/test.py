# -*- coding: utf-8 -*- 

"""
思路：从每个数组中找出一定数量的小的数，最后凑起来总数正好是一半

因为题目时间复杂度要求是log(m+n)，所以要binary search

否则就两个数组分别遍历呗，时间复杂度就是O(m+n)
"""

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        if not nums:
            return 0

        """
        size = 0
        for num in nums:
            size += len(num)
        """

        size = sum(len(num) for num in nums)
        
        if size == 0:
            return 0.0

        if size % 2 == 1:
            return self.findNum(nums, size//2 + 1) * 1.0
        else:
            return (self.findNum(nums, size//2 + 1) + self.findNum(nums, size//2)) /2.0

    """
    问题：如何保证start或者end一定是nums里的数？
    因为start或者end是由middle来的，而middle是（start + end）//2来的，这个数不一定在nums里啊……


    """ 

    def findNum(self, nums, k):
        start, end = self.findRange(nums)

        while start + 1 < end:
            middle = start + (end - start)//2

            if self.countNum(nums, middle) >= k:
                end = middle
            else:
                start = middle

            print("start: ", start)
            print("end: ", end)
            #print("middle: ", middle)

        if self.countNum(nums, start) == k:
            return start

        return end

    def countNum(self, nums, target):
        count = 0

        for num in nums:
            count += self.findSmallerNum(num, target)

        return count

    def findSmallerNum(self, num, target):
        if not num:
            return 0

        start, end = 0, len(num) - 1

        while start + 1 < end:
            mid = start + (end - start)//2

            if num[mid] <= target:
                start = mid
            else:
                end = mid
        
        
        #最后两个数，先看nums[end]是不是小于target，
        #如果是，返回end+1 （因为是从0开始取n个数，所以end其实是n-1）

        #再看start，返回start + 1

        #如果start和end都 > target，返回0，说明这个arr里全大于target
   
        if num[end] <= target:
            return end + 1

        if num[start] <= target:
            return start + 1
 
        return 0

    def findRange(self, nums):
        start = min(num[0] for num in nums if len(num))
        end = max(num[-1] for num in nums if len(num))

        return start, end

if __name__ == '__main__':
    solu = Solution()
    #list1 = [[9,100],[3,4],[1,2],[5,6],[7,8]]
    list1 = [[1,2,3,4,5,5], [7,8,9,10,11]]

    result = solu.findMedian(list1)
    print("result is: ", result)