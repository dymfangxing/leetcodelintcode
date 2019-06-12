#coding=utf-8

#S = [1,2,3]
"""
solution:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None:
            return None

        nums.sort()
        results = []
        subset = []

        self.helper(nums, 0, subset, results)

        return results

#get each prefix array and append with the rest of the numbers
#loops in loops
    def helper(self, nums, index, subset, results):
    	results.append(list(subset))
      #for loop range(start, end) means start from prefix(nums[start]), 
      #prefix(nums[start + 1]), ... prefix(nums)
    	for i in range(index, len(nums)):
    	    subset.append(nums[i])
      #next line means: for each prefix, add the next num to this subset
            self.helper(nums, i + 1, subset, results)
            subset.pop()

if __name__ == '__main__':
    A = [3,2,1]
    results = Solution().subsets(A)
    print("All subsets are: ", results)     
