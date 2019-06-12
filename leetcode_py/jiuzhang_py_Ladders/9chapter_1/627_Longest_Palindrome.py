#coding=utf-8
#这一题不同于667，667是字符串要连着的，这题只要抽里面的char即可
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0

        letter_dict = {}
        maxLen = 0

        #count each character using a dict
        for c in s:
            if c not in letter_dict:
                letter_dict[c] = 1
            else:
                letter_dict[c] += 1

        """
        1) character only appears 1 time: Continue. because we only need 1 of this situation
        2) character cnt is even: add all into maxLen, remove this key-value
        3) character cnt is odd: add letter_dict[c] - 1 to maxLen
        """
        for key in letter_dict:
            if letter_dict[key] == 1:
                continue
            elif letter_dict[key] % 2 == 0:
                maxLen += letter_dict[key]
                letter_dict[key] = 0
            elif letter_dict[key] % 2 == 1:
                maxLen += letter_dict[key] - 1
                letter_dict[key] = 1

        for key in letter_dict:
            if letter_dict[key] == 1:
                maxLen += 1
                break

        return maxLen

    """
    Hint: find the one which has to be removed
    1) find if all char appears in pair, put the total cnt of not pair into var "remove"
    2) if remove > 0, remove -- becuase we will keep one
    3) use total len - remove

    Very smart!
    """

     def longestPalindrome2(self, s):
        # Write your code here
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -= 1
    
        return len(s) - remove

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    string = "abccccdd"
    print("orgin sting is: ", string)
    result = Solution().longestPalindrome(string)
    print("final result is: ", result)
    