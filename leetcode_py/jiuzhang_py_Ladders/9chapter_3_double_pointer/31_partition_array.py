#coding=utf-8

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
            
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        """
        当nums[start] = k = nums[end]时, 因为nums[start] < k时才会移动，所以start不移动了；
        但因为nums[end] >= k也会移动，所以end还要移动的，所以我们就返回start，这样位置就是对的
        """
        return start


#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    test_arrary = [0, 1, 0, 3, 12]
    print(solu.partitionArray(test_arrary, 3))
    test_arrary1= [5,4,3,2,1]
    print(solu.partitionArray(test_arrary1, 3))
