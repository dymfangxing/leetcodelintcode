# -*- coding: utf-8 -*- 
import sys

#hint:
#https://blog.csdn.net/qq508618087/article/details/51392072

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return
        
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[sys.maxsize for i in range(n)] for _ in range(m)]
        #从底部开始：
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                #情况1：到终点时需要的血量
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1,1 - dungeon[i][j])
                #情况2：最右边时需要的血量
                elif j == n - 1:
                    val = dp[i + 1][j] - dungeon[i][j]
                    dp[i][j] = max(1, val)
                #情况3：最下层时需要的血量
                elif i == m - 1:
                    val = dp[i][j + 1] - dungeon[i][j]
                    dp[i][j] = max(1, val)
                #情况4：普通情况时，当前位置需要的血量为其右边或者下方时需要的血量，减去其位置现有值
                #状态转移方程是：
                #dp[i][j]= max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
                #因为至少得是1
                else:
                    val = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
                    dp[i][j] = max(1, val)

        #print("dp is: ", dp)
        return dp[0][0]

if __name__ == "__main__":

    assert Solution().calculateMinimumHP([
            [-2, -3,   3],
            [-5, -10,  1],
            [10,  30, -5]
        ])==7
