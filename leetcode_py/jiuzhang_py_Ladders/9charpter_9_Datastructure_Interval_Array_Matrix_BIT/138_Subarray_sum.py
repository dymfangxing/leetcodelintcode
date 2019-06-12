# -*- coding: utf-8 -*- 

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

#TLE
    def subarraySum(self, nums):
        # write your code here
        results = []

        for i in range(len(nums)):
            total_sum = 0
            for j in range(i, len(nums)):
                total_sum += nums[j]
                if total_sum == 0:
                    results.append(i)
                    results.append(j)
                    return results

        return -1

#hint: Use prefix sum to create a hash, prefix sum is the key, index is value.
#      if 某一段[l, r]的和为0， 则其对应presum[l-1] = presum[r]. (只有如此，相互减去才为0)
#      presum 为数组前缀和。只要保存每个前缀和，找是否有相同的前缀和即可。



    def subarraySum(self, nums):
        #when not picking anything
        prefixSum_Hash = {0: -1}
        #prefixSum_Hash = {}
        prefixSum = 0

        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum in prefixSum_Hash:
                return prefixSum_Hash[prefixSum] + 1, i
            prefixSum_Hash[prefixSum] = i

        return -1, -1


if __name__ == '__main__':
    solu = Solution()
    #arr = [-3,1,2,-3,4]
    arr = [1,0,1]
    result = solu.subarraySum(arr)
    print("result is: ", result)