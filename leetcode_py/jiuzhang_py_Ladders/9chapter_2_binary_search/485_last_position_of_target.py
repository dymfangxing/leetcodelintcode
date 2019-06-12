class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums or not target: 
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end

        if nums[start] == target:
            return start

        return -1

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    test_array = [1,2,2,4,5,5]
    target = 5
    print(solu.lastPosition(test_array, target))

