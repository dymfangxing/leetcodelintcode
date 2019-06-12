#coding=utf-8

"""
Hint:
1) Get every substring of this string
2) Verify if it is Palindrome
3) Keep the maxLex one
""" 
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return
        
        maxLen = 0
        result = None
        i,j = 0, 0
        length = len(s)

        for i in range(length):
            for j in range(i, length):
                if self.isPalindrome(s[i:j+1]):
                    if len(s[i:j+1]) > maxLen:
                        result = s[i:j+1]
                        maxLen = len(s[i:j+1])

        print("maxLen is: ", maxLen)

        return result

    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    string = "abcdzdcab"
    print("orgin sting is: ", string)
    result = Solution().longestPalindrome(string)
    print("final result is: ", result)
    