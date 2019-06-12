"""
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        #return self.isPalindrome(s)
        subset = []
        result = []

        self.helper(s, subset, result)
        return result

    #s: the rest of string to be cut
    #subset: substring(s) which is palidrome and has been cut
    #result: final subsets
    def helper(self, s, subset, result):
        if len(s) == 0:
            result.append(list(subset))
            return
        #at least cut 1 character
        #at most cut to the end of this string
        for i in range(1,len(s) + 1):
            prefix = s[:i]
            if self.isPalindrome(prefix):
                subset.append(prefix)
                #pass the rest of string for deeper processing
                self.helper(s[i:], subset, result)
                subset.pop()

    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    s = "aab"
    result = solu.partition(s)
    print("result is: ", result)
