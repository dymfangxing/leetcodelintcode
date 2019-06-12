from collections import defaultdict

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        #letter_dict = defaultdict()
        if not s:
        	return 0
        letter_dict = {}
        length = 0

        for c in s:
            if c not in letter_dict:
            	letter_dict[c] = 1
            else:
                letter_dict[c] = letter_dict[c] + 1

        print letter_dict

        for key in letter_dict:
            if letter_dict[key] == 1:
        		continue
            elif letter_dict[key]%2 == 1:
            	length += letter_dict[key] - 1
            else:
            	length += letter_dict[key]
        
        if len(letter_dict) == 1:
            cur_val = letter_dict.values()
            return cur_val[0]

        return length + 1

if __name__ == '__main__':
    #print(strStr("a", "a"))
    sol = Solution()
    print(sol.longestPalindrome("abcdefgbbcs"))
    print(sol.longestPalindrome("aaaa"))
    print(sol.longestPalindrome("A"))


