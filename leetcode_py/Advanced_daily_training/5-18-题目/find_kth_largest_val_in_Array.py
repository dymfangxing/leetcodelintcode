#coding=utf-8

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or not n:
            return -1
            
        if n > len(nums):
            return -1
        
        start, end = 0, len(nums) - 1
        return self.helper(nums, start, end, len(nums) - n)

    def helper(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[left + (right - left)//2]
        
        while left <= right:
            while nums[left] < pivot and left <= right:
                left += 1
            while nums[right] > pivot and left <= right:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if left <= k:
            return self.helper(nums, left, end, k)
        if right >= k:
            return self.helper(nums, start, right, k)
            
        return nums[k]
