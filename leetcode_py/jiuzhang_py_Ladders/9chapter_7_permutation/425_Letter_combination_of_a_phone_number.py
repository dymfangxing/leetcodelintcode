#coding=utf-8

KEYBOARD = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code her
        if not digits:
        	return []

        results = []
        self.dfs(digits, 0, '', results)
        return results

    def dfs(self, digits, index, str, results):
    	if len(str) == len(digits):
    		results.append(str)
    		return

    	for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, str + letter, results)


"""
solu 2: 写得麻烦一点
"""

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def __init__(self):
        self.panel = {
            '2': "abc",
            '3': "def",
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
    def letterCombinations(self, digits):
        # write your code here
        if digits is None:
            return []
            
        if len(digits) == 0:
            return []
            
        results = []
        
        self.dfs(digits, 0, [], results)
        
        return results
        
    def dfs(self, digits, start, subset, results):
        if len(subset) == len(digits):
            s = ''.join(subset)
            results.append(s)
            return

        string = self.panel[digits[start]]

        for c in string:
            subset.append(c)
            self.dfs(digits, start + 1, subset, results)
            subset.pop()

if __name__ == '__main__':
    solu = Solution()
    digits = "23"
    result = solu.letterCombinations(digits)
    print("result is: ", result)