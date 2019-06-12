#coding=utf-8

#hint: dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return

        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        print("result is: ", dp[-1][-1])
        return dp[-1][-1]

if __name__ == '__main__':
    solu = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert Solution().minPathSum(grid)==7
    