#coding=utf-8

#Hint: 状态转移方程： dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if not m or not n:
            return 0

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


if __name__ == '__main__':
    solu = Solution()
    m = 1
    n = 3
    
    assert Solution().uniquePaths(m, n)==1

"""
    m = 3
    n = 3
    
    assert Solution().uniquePaths(m, n)==6
"""