#coding=utf-8
"""
这道题考的是最长回文子序列，注意是序列而不是子串，序列的意思是组成回文的字符可以是不连续的，
而回文子串则需要连续的，比如例子中的bbbab，最长回文序列是bbbb，最长回文子串是bbb或是bab。


一个字符串有许多子序列，比如字符串cabbeaf，它的子序列有c、abb、e、a、f，
可以通过删除某些字符而变成回文字符串，
字符串“cabbeaf”，删掉‘c’、'e'、‘f’后剩下的子串“abba”就是回文字符串，也是其中最长的回文子序列。

DP：
对于任意字符串，如果头尾字符相同，
那么字符串的最长子序列等于去掉首尾的字符串的最长子序列加上首尾；
如果首尾字符不同，则最长子序列等于:
去掉头的字符串的最长子序列和去掉尾的字符串的最长子序列的较大者。

dp[i][j] 表示从第i到第j个字符间的最大回文序列长度，
dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j]
dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])   if s[i] != s[j]

Refer to: https://www.jiuzhang.com/solution/longest-palindromic-subsequence/#tag-highlight-lang-python

注意：
每次loop时都从dp[i][i]开始，i需要从array最后一个element开始，j从i+1开始
"""
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        print("before inside loop: ")
        #print([i for i in dp])
        print('\n'.join([str(i) for i in dp]))

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            print("1st inside loop: ")
            print('\n'.join([str(_) for _ in dp]))
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            print("2nd inside loop: ")
            print('\n'.join([str(__) for __ in dp]))
            print("#######################")

        return dp[0][len(s) - 1]

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    string = "bbbab"
    print("orgin sting is: ", string)
    result = Solution().longestPalindromeSubseq(string)
    print("final result is: ", result)
    