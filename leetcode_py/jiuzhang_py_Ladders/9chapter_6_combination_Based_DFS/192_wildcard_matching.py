"""
Example:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") ->false
"""

class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        #self.result = None
        #self.matched = None
        return self.helper(0, s, 0, p, {})


    def helper(self, srcSplit, s, patternSplit, p, memo):
        if (srcSplit, patternSplit) in memo:
        	return memo[(srcSplit, patternSplit)]

        if srcSplit == len(s):
        	#if src is empty, pattern has to either empty,
            #or all char in pattern have to be *
            #then that means src and pattern matches
            for index in range(patternSplit, len(p)):
                if p[index] != '*':
                    return False
            return True
        #if src is not empty, but pattern is empty
        #that means they are not matching
        if patternSplit == len(p):
        	#it cannot match anything?
            return False
        
    	if p[patternSplit] == '*':
    	    matched = self.helper(srcSplit, s, patternSplit + 1, p, memo) or \
    		     self.helper(srcSplit + 1, s, patternSplit, p, memo)
        else:
            matched = self.helper(srcSplit + 1, s, patternSplit + 1, p, memo) and \
        	      self.charMatch(s[srcSplit], p[patternSplit])

        memo[(srcSplit, patternSplit)] = matched
        return matched

    def charMatch(self, s, p):
        return s == p or p == '?'

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    s = "aab"
    p = "*ba"
    result = solu.isMatch(s,p)
    print("result is: ", result)
