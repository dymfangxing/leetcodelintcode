#coding=utf-8

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
    # solu1:
        if not nums:
            return []
        #receive partition's position after first partition
        position = self.partition(nums, 0, 0)
        print("after 1st partition, the arr is: ", nums)
        self.partition(nums, position, 1)
        print("after 2nd partition, the arr is: ", nums)

    def partition(self, nums, position, k):
        start, end = position, len(nums) - 1

        while start <= end:
            while start <= end and nums[start] == k:
                start += 1
            while start <= end and nums[end] > k:
                end -= 1

            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        #since start may way ahead of end, we return end + 1 for next time's partition

        return end + 1

    #solu 2: easier thinking. just twice quick select and always start from index 0

    def sortColors1(self, nums):
        if nums is None:
            return -1

        if len(nums) == 0:
            return []

        self.quickSelect(nums, 0, len(nums) - 1, 0)
        self.quickSelect(nums, 0, len(nums) - 1, 1)

        return nums

    def quickSelect(self, nums, start, end, target):
        while start <= end:
            while start <= end and nums[start] <= target:
                start += 1
            while start <= end and nums[end] > target:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

    #solu 3:


#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    colors = [1, 0, 1, 2, 0, 1, 2, 1, 2, 0, 0]
    solu.sortColors(colors)
    print(colors)

