#coding=utf-8

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
 
#hint: similar to 480:binary tree path 
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
    	if s in memo:
    		return memo[s]
    	#means no any solutions
        if len(s) == 0:
            return []

        partitions = []

        for index in range(1, len(s)):
            prefix = s[:index] #cut a prefix (at lease one char)
            #if it's not in wordDict, try to cut more
            if prefix not in wordDict:
            	continue
            
            #else if prefix is in wordDict
            #find all sub-partitions with this prefix
            sub_partitions = self.dfs(s[index:], wordDict, memo)
            #after find all partitions,
            #need to combine prefix, with " ", to form a result
            #for example:
            #lint, code(co, de) => (lint, co, de)
            for partition in sub_partitions:
            	partitions.append(prefix + " " + partition)
        
        #this happens when a whole string is a matching word
        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        return partitions

if __name__ == '__main__':
    solu = Solution()
    s = "lintcode"
    wordDict = ["de", "ding", "co", "code", "lint"]
    result = solu.wordBreak(s, wordDict)
    print("result is: ", result)
