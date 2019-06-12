#coding=utf-8

#Hint: use two vars to always remember the min prefix sum
#      and the global max val 
#使用前缀和的方法，计算每个位置为结尾的 subarray 的最大值是多少。
"""
遍历整个array，不断更新presum，最大值和最小presum
每个prefix sum都可能是最小
minvalue初始值为0因为如果只有一个值，那这个array最大值为这个值本身
先更新max再更新min，因为subarray自己减去自己的空sub情况不考虑在内

min subarray[i ~ j]:

PrefixSum[j + 1] - min(PrifixSum[i ~ j])
"""

import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum

if __name__ == '__main__':
    solu = Solution()
    #arr = [-3,1,2,-3,4]
    arr = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    result = solu.maxSubArray(arr)
    print("result is: ", result)
