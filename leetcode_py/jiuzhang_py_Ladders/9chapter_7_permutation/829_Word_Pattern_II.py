#coding=utf-8
"""
二刷：思路：

1）用dict存pattern char和substring对应关系，用set存substring是否已出现
2）dfs for loop遍历每一种可能：

a）如果substing已存在，continue
b）将char和substring添加进dict和set
c）递归，如果返回值是True，return True
d）否则，说明是false，这种情况不符合，则将char和substring踢出dict和set，继续

在for loop 外面，check：
1）当len（pattern）是0时，若len(string)不为0，则return False，否则return True
2）检查当前这个pattern char所对应的word，是不是当前string的startstring：
string.startwith(word), 若是，则继续调用递归，算剩下的substring和pattern，否则返回False
"""
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())

    def is_match(self, pattern, string, mapping, used):
        if not pattern:
            return not string
            
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word):], mapping, used)
            
        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            
            del mapping[char]
            used.remove(word)
            
        return False

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        """
        1) mapping{} maps each char in pattern with a string in str
        2) set() records each used string that was used in mapping 
        """
        return self.isMatching(pattern, str, {}, set())

    def isMatching(self, pattern, string, mapping, used):
    	#if len(pattern) is 0 and len(str) is not 0, return False
    	#else if len(str) is also 0, return True
    	if not pattern:
    	    return not string

    	char = pattern[0]

    	if char in mapping:
    	#if pattern exists, check if mapping word matches the start of str
    	#if so, remove those pair from origin and keep going
    	#else return False
    	    word = mapping[char]
    	    if not string.startswith(word):
    	    	return False
    	    	
    	    return self.isMatching(pattern[1:], string[len(word):], mapping, used)

    	#loop each combination and put into pair. try if it could match	
    	for i in range(len(string)):
    	    word = string[:i + 1]
            #this if statement is used to gurantee one word can only be mapped once     
    	    if word in used:
    	        continue

            mapping[char] = word
            used.add(word)
            #if the rest of them matches, return True
            if self.isMatching(pattern[1:], string[len(word):], mapping, used):
                return True
            #after that, we have to remove those combination for next try
            del mapping[char]
            used.remove(word)
            #if goes to this line, which means it fails
        return False
            
if __name__ == '__main__':
    solu = Solution()
    pattern = "abab"
    string = "abab"
    result = solu.wordPatternMatch(pattern, string)
    print("result is: ", result)

    pattern1 = "abab"
    string1 = "redblueredblue"
    result = solu.wordPatternMatch(pattern1, string1)
    print("result is: ", result)

