#coding=utf-8
"""
转化为找第一个< nums[end]的数
"""
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None
        
        start, end = 0, len(nums) - 1
        target = nums[end]

        while start + 1 < end:
            mid = (start + end)//2
            """
            比如：4,5,6,7,0,1,2
            这时start=mid
            """
            if nums[mid] > target:
                start = mid
            """
            比如99，100，0，1，2，3，4，5，6，7，8，9，10，。。。
            这时end=mid
            """
            else:
                end = mid

        return min(nums[start], nums[end])




if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    test_array = [4, 5, 6, 7, 0, 1, 2]
    #test_array1 = [10, 9, 8, 7]
    print(solu.findMin(test_array))
    #print(solu.mountainSequence(test_array1))