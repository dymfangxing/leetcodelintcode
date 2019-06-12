#coding=utf-8

from collections import defaultdict

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    #solu 1: Pure DFS
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
            
        results = []
        self.dfs(nums, 0, [], results)
        
        return results
        
    def dfs(self, nums, start, subset, results):
        if len(subset) == len(nums):
            results.append(list(subset))
            
        for i in range(len(nums)):
            if nums[i] not in subset:
                subset.append(nums[i])
                self.dfs(nums, i + 1, subset, results)
                subset.pop()

    #solu 2: DFS with memo
    def permute2(self, nums):
        # write your code here
        results = []
        memo = [None for _ in range(len(nums))]
        self.dfs(nums, [], results, memo)
        
        return results

    def dfs(self, nums, subset, results, memo):
        if len(subset) == len(nums):
            results.append(list(subset))
            return

        for i in range(len(nums)):
            """
            使用memo，让选过的就表再选进来了
            """
            if memo[i] == True:
                continue
            subset.append(nums[i])
            memo[i] = True
            self.dfs(nums, subset, results, memo)
            memo[i] = False
            subset.pop()


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3]
    result = solu.permute2(nums)
    print("result is: ", result)
