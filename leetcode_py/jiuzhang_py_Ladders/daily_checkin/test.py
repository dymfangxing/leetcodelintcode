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
        nums = list(set(nums))
        return nums


if __name__ == '__main__':
    A = [3,2,1,3,2]
    results = Solution().subsets(A)
    print("All subsets are: ", results)     
