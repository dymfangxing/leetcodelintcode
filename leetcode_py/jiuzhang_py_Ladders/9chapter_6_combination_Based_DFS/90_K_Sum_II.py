#coding=utf-8

class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if A is None or k is None or target is None:
            return []
            
        A.sort()
        results = []
        
        self.dfs(A, k, target, 0, [], results)
        
        return results
        
    def dfs(self, A, k, target, start, subset, results):
        if target == 0 and len(subset) == k:
            results.append(list(subset))
        
        for i in range(start, len(A)):
            if target < A[i]:
                return
            subset.append(A[i])
            self.dfs(A, k, target - A[i], i + 1, subset, results)
            subset.pop()
