# -*- coding: utf-8 -*- 

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #d[i] = max(d[i - 1], d[i - 2] + a[i] if i > 0 && i - 2 >= 0)
        if not nums:
            return 0

        d = [0 for _ in range(len(nums))]
        d[0] = nums[0]

        for i in range(1, len(nums)):
            if i - 2 >= 0:
                d[i] = max(d[i - 1], d[i - 2] + nums[i])
            else:
                d[i] = max(d[i - 1], nums[i])

        #print(d)
        length = len(nums)
        return d[length - 1]


if __name__ == '__main__':
    solu = Solution()
    #arr = [1,2,3,1]
    arr = [2,7,9,3,1]
    result = solu.rob(arr)
    print("result is: ", result)