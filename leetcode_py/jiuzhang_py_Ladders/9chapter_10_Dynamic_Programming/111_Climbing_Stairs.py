#coding=utf-8

#hint: if obstacleGrid[i][j] == 1, dp[i][j] = 0
#if i = 0，当dp[i][j] == 1时，obstacleGrid[i][j] = 1, 否则dp[i][j] = dp[i][j - 1]，即1就是1，0就是0
#if j = 0, 以此类推

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if i == 0:
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print("dp is: ", dp[n - 1][m - 1])
        return dp[n - 1][m - 1]

if __name__ == '__main__':
    solu = Solution()
    arr = [[0,0],[0,0],[0,0],[1,0],[0,0]]
    assert Solution().uniquePathsWithObstacles(arr)==3

    """
    arr = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().uniquePathsWithObstacles(arr)==2
    """
    """
    arr = [[0]]
    assert Solution().uniquePathsWithObstacles(arr)==1
    """
    