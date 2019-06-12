class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        if s is None:
            return []
            
        if len(s) == 0:
            return []
            
        s = sorted(s)
        results = []
        memo = [None for _ in range(len(s))]
        
        self.dfs(s, memo, [], results)
        
        return results
        
    def dfs(self, s, memo, subset, results):
        if len(subset) == len(s):
            new_str = "".join(subset)
            if self.isPalindromes(new_str):
                results.append(new_str)
        
        for i in range(len(s)):
            if memo[i] == True:
                continue
            
            if s[i] == s[i-1] and memo[i - 1] is False:
                continue
            
            subset.append(s[i])
            memo[i] = True
            self.dfs(s, memo, subset, results)
            memo[i] = False
            subset.pop()
    
    def isPalindromes(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    solu = Solution()
    string = "aabb"
    result = solu.generatePalindromes(string)
    print("result is: ", result)
