#coding=utf-8
"""
solu 0: 用quick select，找到k那个数的时候返回，

这样数组的右边就是都>num[k]的。

这时再sort下后半边就好了

不能用mergeSort的。因为mergeSort永远只是局部有序
"""
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if not nums or k <= 0 or k > len(nums):
            return []
        
        self.helper(nums, 0, len(nums) - 1, len(nums) - k)
        result = nums[len(nums) - k:]
        
        result.sort(reverse=True)
        
        return result
        
    def helper(self, nums, start, end, n):
        if start >= end:
            return
        
        left, right = start, end
        mid = start + (end - start)//2
        pivot = nums[mid]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if n <= right:
            return self.helper(nums, start, right, n)
        elif n >= left:
            return self.helper(nums, left, end, n)
        else:
            return
"""
solu 1.1: 用一些heapq里的固定API
"""            
    def topk(self, nums, k):
        # write your code here
        if not nums or k <= 0 or k > len(nums):
            return []
        
        heapq.heapify(nums)
        ktop = heapq.nlargest(k, nums)
        ktop.sort(reverse=True)
        
        return ktop
"""
solu 1: use heapq
"""
import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if not nums or not k:
            return

        if k > len(nums):
            return nums

        self.queue = []

        for num in nums:
            heapq.heappush(self.queue, -num)
        
        ret = []

        while k > 0:
            ret.append(-heapq.heappop(self.queue))
            k -= 1

        return ret


    def topk1(self, nums, k):
        # write your code here
        if not nums or not k:
            return

        if k > len(nums):
            return nums.sort()

        self.queue = []

        for num in nums:
            heapq.heappush(self.queue, num)

            if len(self.queue) > k:
                heapq.heappop(self.queue)
        

        self.queue.sort()
        self.queue.reverse()
        
        return self.queue


if __name__ == '__main__':
    solu = Solution()
    arr = [3,10,1000,-99,4,100]
    k = 3
    result = solu.topk1(arr, k)
    print("result is: ", result)
