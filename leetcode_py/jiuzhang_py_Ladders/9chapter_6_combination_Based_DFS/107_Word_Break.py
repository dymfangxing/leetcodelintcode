#coding=utf-8

"""
f[i] 表示前i个字符是否可以分。
从前往后枚举结尾。对于每个结尾枚举分成的最后一段的长度j。然后看f[i-j]是否可分。
"""

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            if len(s) == 0:
                return True
            else:
                return False

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                print("i is %d, j is %d, f[%d] is: %s" %(i, j, i-j, f[i-j])) 
                if not f[i - j]:
                    continue
                print("i is %d, j is %d, s[%d] is: %s" %(i, j, i-j, s[i-j])) 
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        
        return f[n]



if __name__ == '__main__':
    solu = Solution()
    s = "lintcode"
    wordDict = ["de", "ding", "co", "code", "lint"]
    result = solu.wordBreak(s, wordDict)
    print("result is: ", result)

