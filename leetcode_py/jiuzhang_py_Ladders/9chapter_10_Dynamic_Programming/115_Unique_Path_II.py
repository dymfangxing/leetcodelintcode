#coding=utf-8

#hint: dp[n] = dp[n - 1] + dp[n - 2]
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if not n:
            return 0

        if n == 1 or n == 2:
            return n

        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            val = dp[i - 1] + dp[i - 2]
            dp[i] = val

        print("result is: ", dp[-1])
        
        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    n = 3
    assert Solution().climbStairs(n)==3
