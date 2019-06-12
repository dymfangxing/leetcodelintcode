#coding=utf-8
#类似于股票买卖，找subsequence里有几个item小于最后一个item

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        longest = 0

        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i] = 1
            #hint:对于每个数字，枚举前面所有小于自己的数字 j，Dp[i] = max{Dp[j]} + 1. 
            #如果没有比自己小的，Dp[i] = 1;
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1

            if dp[i] > longest:
                longest = dp[i]

        print(dp)

        return longest

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    nums = [5,4,1,2,3]
    result = Solution().longestIncreasingSubsequence(nums)
    print("final result 1 is: ", result)
    nums1 = [4,2,4,5,3,7]
    result = Solution().longestIncreasingSubsequence(nums1)
    print("final result 2 is: ", result)
    