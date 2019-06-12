#coding=utf-8
#边界条件处理还不明白

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return None

        start, end = 0, len(nums) - 1
        #get the len(nums) - n's smallest val
        return self.quickSelect(nums, start, end, len(nums) - n)

    def quickSelect(self, nums, start, end, n):
        """
        相等说明找到了
        """
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end)//2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
"""
left和right之间可能会有一个数：因为若left==right，然后left++，right--
那二者间就会有一个数了

所以最坏情况下数组被分成3个部分：
[start, right], [right, left], [left, end]

下面就是落在这3个区间的3种情况
"""
"""
最后退出的情况应该是右指针在左指针左边一格
这时如果右指针还大于等于k，说明kth在左半边
这时如果左指针还小于等于k，说明kth在右半边
如果这个分界点是k，说明分界点的数就是第k个数。
"""

        if n <= right: #左边                     #Notes:
            return self.quickSelect(nums, start, right, n) #because n won't affect sorting
        if n >= left:#右边                                      #we are only dividing array to
            return self.quickSelect(nums, left, end, n)    #(n-1) numbers < nums[n] < (n+1) numbers
                                                           #so we just pass it into recursion
        return nums[right + 1]#中间，或者nums[n]也行，因为n=right+1

"""
solu 2: using heapq. but will use O(n) extra space
"""
import heapq

class Solution2:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not n or not nums:
            return -1

        if n > len(nums):
            return -1

        queue = []

        for num in nums:
            heapq.heappush(queue, -num)

        while n > 1:
            -heapq.heappop(queue)
            n -= 1

        return -heapq.heappop(queue)

#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    n = 5
    nums = [9,3,2,4,8]
    print(solu.kthLargestElement(n, nums))

