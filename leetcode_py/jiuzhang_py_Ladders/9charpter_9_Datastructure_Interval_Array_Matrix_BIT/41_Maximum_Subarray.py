
# -*- coding: utf-8 -*- 

#Hint: use two vars to always remember the min prefix sum
#      and the global max val 
#使用前缀和的方法，计算每个位置为结尾的 subarray 的最大值是多少。


"""
solu 1:dp

dp存每一个index时,只要dp[i-1]>0,就dp[i] = dp[i-1] + nums[i]（因为后面可能有很大的正整数，还是能很大）
                      否则清零dp[i] = num[i]
最后返回max(dp)

"""
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
            
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
            
        return max(dp)

"""
solu 2: prefix sum
"""
"""
遍历整个array，不断更新presum，最大值和最小presum
每个prefix sum都可能是最小
minvalue初始值为0因为如果只有一个值，那这个array最大值为这个值本身
先更新max再更新min，因为subarray自己减去自己的空sub情况不考虑在内
"""

import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        min_prefix_sum, max_prefiex_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_prefiex_sum

if __name__ == '__main__':
    solu = Solution()
    #arr = [-3,1,2,-3,4]
    arr = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    result = solu.maxSubArray(arr)
    print("result is: ", result)
