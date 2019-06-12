#coding=utf-8

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome1(self, s):
        if s is None:
            return

        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    #print(strStr("a", "a"))
    sol = Solution()
    print(sol.isPalindrome("abcdefgbbcs"))
    print(sol.isPalindrome("aaaa"))
    #rint(sol.longestPalindrome("A"))
