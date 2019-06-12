#coding=utf-8

"""
solu 1: 把搜索问题转化成树状问题：要或不要这个数，取最后一层结果
"""
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        #nums is [] should return [[]], and it is covered in the following
        if nums is None:
        	return nums

        nums.sort()

        results = []
        subset = []

        #start: check if 0th number has to be added into subset
        """
        这个start表示目前在处理树的第几层。
        最开始是第0层，一直到第len(nums)层时，往results里加

        或者就理解成，已经走完了这个array了。
        """
        self.helper(nums, 0, subset, results)

        return results

    def helper(self, nums, start, subset, results):
    	#only last level has result we want, so we add this check
    	if start == len(nums):
            """
            这个”list”相当重要，是用来把当前subset deepcopy一个
            """
    	    results.append(list(subset))
    	    return

        """
        把一个element从nums里加进来
        """
    	subset.append(nums[start])
        """
        subset传入下一层
        """
    	self.helper(nums, start + 1, subset, results)

        """
        把这个元素从subset里弹出来
        """
    	subset.pop()
        """
        subset也传入下一层
        """
    	self.helper(nums, start + 1, subset, results)


"""
solu 2:
"""
    def subsets2(self, nums):
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
    		subset.append(nums[i])
    		self.dfs(nums, i + 1, subset, results)
    		subset.pop()

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    nums = [1, 2, 3]
    result = solu.subsets(nums)
    print("subsets is: ", result)