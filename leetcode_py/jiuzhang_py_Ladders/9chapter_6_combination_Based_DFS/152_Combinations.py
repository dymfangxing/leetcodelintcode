#coding=utf-8
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if n is None or k is None:
            return []
        
        nums = [ele for ele in range(1, n + 1)]
        nums.sort()
        results = []
        self.dfs(nums, k, 0, [], results)
    
        return results
    
    def dfs(self, n, k, start, subset, results):
        if len(subset) == k:
            results.append(list(subset))
        
        for i in range(start, len(n)):
            subset.append(n[i])
            self.dfs(n, k, i + 1, subset, results)
            subset.pop()

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    n = 4
    k = 2
    result = solu.combine(n, k)
    print("combination is: ", result)