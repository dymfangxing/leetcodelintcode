#coding=utf-8
"""
hint:

use two heap: 
left: maxheap right:minheap
get fitst num as median

loop nums, if num < median, push to left, else, push to right

if len(left heap) + 1 < len(right heap) -> push median to left heap, heappop right heap as median;

if len(left heap) > len(right heap) -> push median to right heap, heappop left heap as median
"""
import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
            
        results = [nums[0]]
        minheap, maxheap = [], []
        self.median = nums[0]

        for i in range(1, len(nums)):
            self.add(nums[i], minheap, maxheap)
            results.append(self.median)

        return results

    def add(self, num, minheap, maxheap):
        if num < self.median:
            heapq.heappush(maxheap, -num)
        else:
            heapq.heappush(minheap, num)

        if len(minheap) < len(maxheap):
            heapq.heappush(minheap, self.median)
            self.median = -heapq.heappop(maxheap)

        if len(maxheap) + 1 < len(minheap):
            heapq.heappush(maxheap, -self.median)
            self.median = heapq.heappop(minheap)

"""
brute force solu: will TLE
"""
class Solution1:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
            
        input = []
        results = []
        
        for num in nums:
            input.append(num)
            
            size = len(input)
            if size%2 == 1:
                median = self.findNum(input, size//2 + 1)
            else:
                median = self.findNum(input, size//2)
                          
            results.append(median)
            
        return results
        
    def findNum(self, arr, k):
        arr.sort()
        return arr[k-1]


if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    nums = [4,5,1,3,2,6,0]
    result = solu.medianII(nums)
    print("result is: ", result)