#coding=utf-8

"""
Hint:
在插入subset的地方做filter

如果i != start 且 nums[i] == nums[i-1], 说明nums[i]不用再加进来了，重复了

try: [1,2,2,2,3] as an example
"""
class Solution:
    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
        	return None

        nums.sort()
        results = []
        subset = []
        self.dfs(nums, 0, subset, results)
        return results


    def dfs(self, nums, start, subset, results):
    	results.append(list(subset))

    	for i in range(start, len(nums)):
            #i != start => gurantee the previous num is not picked before
            #and this num equals to previous one
            # => this num may cause duplicated and needs to be skip
            #skip: you pick 2nd number but not pick the 1st number, which both
            #are the same
            #example: [1 ,2, 2'', 2''', 2'''']
            #if prefix is [1,2], start is 2'', no problem
            #but for 2''' and 2'''',  they are duplicated and have to skip
            """
            意思是除了重复元素的第一个要保留，其他都不要。

            类似permutation II里的memo[i-1] = False
            """
    		if i != start and nums[i] == nums[i - 1]:
    			continue
    		subset.append(nums[i]) #[1] - > [1,2] 
            #1) in above step you can think like you have covered
            #all possible solutions for prefix starts with [1,2]
            #[ 1,2,3],[1,2,4], [1,2,3,4]...
            #2) i + 1 is to avoid we pick [2], and [2] wants to pick "1" again,
            # which is duplicated with [1,2]
    		self.dfs(nums, i + 1, subset, results) #[1,2] -> [1, 2, 3], [1,2, 4], ...
    		subset.pop() #[1, 2] -> [1]

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    nums = [1, 2, 2]
    result = solu.subsetsWithDup(nums)
    print("subsets is: ", result)