#coding=utf-8
"""
思想：用m1，m2来表示两个点，根据m1，m2来判断上升或下降，找到peak
"""
"""
2019年5月九章推荐答案，不用m1,m2了，就用一个m。因为就一个peak，只需找到第一个使得 nums[i] > nums[i + 1] 的 i。

"""
   def mountainSequence(self, nums):
        if not nums:
            return -1
            
        # find first index i so that nums[i] > nums[i + 1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # mid + 1 保证不会越界
            # 因为 start 和 end 是 start + 1 < end
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        
        return max(nums[start], nums[end])
"""
我5-28二刷时自己写的的答案，也过了
"""
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            m1 = start + (end - start)//2
            m2= m1 + (end - m1)//2
            
            if nums[m1] < nums[m2]:
                start = m1
            else:
                end = m2
                
        return max(nums[start], nums[end])


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    # Use two mid to check which range this max num is at
    #The key of binary search is not to find a target, but to find a region which closest
    #to the target(s)
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
        ##注意：要这样去减，不要写成(left+right)//2，因为有可能除不尽，最后搞错
            m1 = left + (right - left)//2
            m2 = right - (right - m1)//2

            if nums[m1] > nums[m2]:
                right = m2 - 1
            elif nums[m1] < nums[m2]:
                left = m1 + 1
            else:  #because finally there are two elements left in this array (we find two close elements)
                   #then we just have to get the max num btw these two elements.
                left = m1
                right = m2

        return max(nums[left], nums[right])


if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    test_array = [1,2,2,4,5,5,2,1,0]
    test_array1 = [10, 9, 8, 7]
    print(solu.mountainSequence(test_array))
    print(solu.mountainSequence(test_array1))