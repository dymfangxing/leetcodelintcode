class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def isPalindrome(self, substring):
    	start = 0
    	end = len(substring) - 1
        flag = True

        while start < end:
        	if substring[start] == substring[end]:
        		flag = False
        	else:
        		flag = True

        return flag

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return None

        longestPalindromeString = ''

        for i in range(len(s)):
        	for j in range(len(s) - i):
                substring = s[:i] + s[j:] 
            #print "substring is: ", substring
            is_Palidrome = True

	    for j in range(len(substring)/2):
                #print "j is: ", j
	        #print "start ", substring[j]
                #print "end", substring[len(substring) - j - 1]
	        if substring[j] != substring[len(substring) - j - 1]:
                    is_Palidrome = False
	            break

            #print "current flag is: ", is_Palidrome
            if is_Palidrome == True and len(substring) > len(longestPalindromeString):
                longestPalindromeString = substring

        return longestPalindromeString


if __name__ == '__main__':
    #print(strStr("a", "a"))
    sol = Solution()
    print(sol.longestPalindrome("abcdfeghijk"))
    print(sol.longestPalindrome("baaaa"))
    print(sol.longestPalindrome("cccdd"))
