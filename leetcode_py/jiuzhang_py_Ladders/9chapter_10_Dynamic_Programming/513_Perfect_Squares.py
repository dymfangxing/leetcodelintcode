#coding=utf-8
import sys,math
"""
1）用dp[]表示这n个数分别对应的完全平方数的个数
2) 如果n = i * i,则dp[n] = 1。我们先把比n小的数里面只能能被完全平方的数找出来
3）对0 - n中剩下的数i，dp[i] = min(dp[i], dp[i - j*j] + 1)

一句话总结：dp[i] = min(dp[i], dp[i - j*j] + 1) #因为dp[j*j] = 1
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        if not n:
            return

        dp = [sys.maxsize for _ in range(n + 1)]

        for i in range(int(math.ceil((math.sqrt(n + 1))))):
            if i*i <= n:
                dp[i*i] = 1

        for i in range(n + 1):
            for j in range(int(math.ceil((math.sqrt(i))))):
                dp[i] = min(dp[i], dp[i - j*j] + 1)

        return dp[n]

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    num = 12
    result = Solution().numSquares(num)
    print("final result is: ", result)