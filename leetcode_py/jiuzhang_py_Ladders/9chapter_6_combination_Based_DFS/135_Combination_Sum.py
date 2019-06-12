#coding=utf-8
"""
注意3点：

1）因为数组里的数是可以反复取的，所以candidates要排序且去重，避免最后结果有重复
2）找target - num[i], 当target == 0 时subset.append, 
   当target < num[i]时，return，因为找不到了
3）因为数字可以反复取，所以传index的时候不用index+1了，还是从这一点继续找
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates is None or target is None:
            return None

        candidates = sorted(list(set(candidates)))
        subset = []
        results = []

        self.helper(candidates, 0, target, subset, results)

        return results

    def helper(self, nums, index, target, subset, results):
        if target == 0:
            results.append(list(subset))

        #for loop range(start, end) means start from prefix(nums[start]), 
        #prefix(nums[start + 1]), ... prefix(nums)
        for i in range(index, len(nums)):
            if target < nums[i]:
                return
            subset.append(nums[i])
        #next line means: for each prefix, add the next num to this subset
        #not i + 1 because number can be used repeated
            self.helper(nums, i, target - nums[i], subset, results)
            subset.pop()

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    nums = [8,2,2,2,2,3,6,7]
    target = 7
    result = solu.combinationSum(nums, target)
    print("combinationSum is: ", result)