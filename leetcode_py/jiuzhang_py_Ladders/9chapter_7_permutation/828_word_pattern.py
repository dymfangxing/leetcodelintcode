#coding=utf-8

"""
思路：用两个dict，互相备份

遍历两个string，如果：
1）word和pattern都不在各自dict里，互相加一下

2）word和pattern都在各自dict里，看看互相能否对上

3）其中只有一个在，肯定是false了（对不上了）
"""
class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        if not pattern or not teststr:
            return False
        
        wordDict = {}
        patternDict = {}
        
        words = teststr.split(' ')

        i, j = 0, 0

        while i < len(words) and j < len(pattern):
            if words[i] not in wordDict and pattern[j] not in patternDict:
                wordDict[words[i]] = pattern[j]
                patternDict[pattern[j]] = words[i]
            elif words[i] in wordDict and pattern[j] in patternDict:
                if wordDict[words[i]] != pattern[j]:
                    return False
            else:
                return False
            i += 1
            j += 1
        
        return True