# -*- coding: utf-8 -*- 

"""
二刷
"""

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
    因为：
    1) start 和 end 间一定有在nums里的数，
    2）只有start和end相邻时才退出

    所以退出的时候，或者start 这个数带入后==k，或者end。所以check的时候先check start

    举个例子，list 1,5,9,13,你要找到第3个数，当前mid是7，
    你的小于等于mid的count是2，你要增大mid，直到mid等于list中的某个值，
    这个case是9，你的count一直没变还是2，比如mid是8时，count还是2。

    所以说只有mid变为list中的某个值时，才会改变count，这也是你最后会记录的值
    """ 

    def findNum(self, nums, k):
        start, end = self.findRange(nums)

        while start + 1 < end:
            middle = start + (end - start)//2

            if self.countNum(nums, middle) >= k:
                end = middle
            else:
                start = middle

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

"""
hint: 2 binary search: hard! need to redo it
"""
class Solution1:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        if not nums:
            return 0.0
        '''
        size =0 
        for num in nums:
            size += len(num)
        '''
        size = sum(len(num) for num in nums)

        if size == 0: #if nums is not empty but all of num is empty like:[[], [], [], []]
            return 0.0

        if size%2 == 1:
            return self.findKValue(nums, size//2 + 1) * 1.0 #size//2 + 1 is the kth 比如size=7，size//2 + 1 = 4,即要找的数
        else:   #size=8，则要找中间两数和/2,即第4个和第5个的和除以2
            return (self.findKValue(nums, size//2 + 1) + self.findKValue(nums, size//2))/2.0

    def findKValue(self, nums, k):
        start, end = self.findRange(nums)
        print("start, end are: ", start, end)
        
        #mid = (start + end)//2
        #pick all vals larger than start and smaller than end
        while start + 1 < end:
            mid = (start + end)//2
            #如果超过k个数字了，缩小target的值
            if self.countNum(nums, mid) >= k:
                end = mid
            else:  #如果不到k个数字了，增大target的值
                start = mid
        #check if start or end matches
        if self.countNum(nums, start) == k:
            return start

        return end

    def countNum(self, nums, val):
        count = 0

        for num in nums:
            count += self.findInArray(num, val)

        return count

    def findInArray(self, num, val):
        if not num:
            return 0

        start, end = 0, len(num) - 1

        while start + 1 < end:
            mid = (start + end)//2

            if val < num[mid]:
                end = mid
            else:
                start = mid

        """
        最后得到start,end两个数:
        如果nums[start] > val, 说明start之前的都是符合要求的，从
        start + 1开始不符合（也就是第start个），所以返回第start个

        如果nums[end] > val, 说明end之前的都是符合要求的，从
        end + 1开始不符合（也就是第end个），所以返回第end个

        否则，说明end也符合的，所以返回第end+1个
        """
        if num[start] > val:
            return start

        if num[end] > val:
            return end

        return end + 1 #this means all elements in this array are less than val

    def findRange(self, nums):
        start = min(num[0] for num in nums if len(num))
        end = max(num[-1] for num in nums if len(num))

        return start, end


if __name__ == '__main__':
    solu = Solution()
    list1 = [[9,100],[3,4],[1,2],[5,6],[7,8]]

    result = solu.findMedian(list1)
    #print("result is: ", result)
