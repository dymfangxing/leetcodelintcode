# -*- coding: utf-8 -*- 

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        """
        #hint: from bottom to top，转化为求从最下层，到triangle上每个点的最短距离

        minPath[k][i] = min(minPath[k+1][i], minPath[k+1][i+1]) + triangle[k][i]
        用dp[]这个一维数组，每个loop只存当前loop这一层元素的最短路径，即：
        使用dp[i]表示到当前这一层第i个元素时的最小路径。

        则可知：

        第k层的i: dp[i] = 

        第k+1层的: min(dp[i], dp[i+1]) + triangle[k][i](当前层的i)

        所以最后到top层后，只要返回dp[0]即可

        """
        if not triangle:
            return 0

        dp = triangle[-1]
        height = len(triangle)

        for layer in range(height - 2, -1, -1):#dp初始化是最下一层，从倒数第二层往第0层递减逐层遍历
            for index in range(len(triangle[layer])):
                dp[index] = min(dp[index], dp[index + 1]) + triangle[layer][index]

        return dp[0]

if __name__ == '__main__':
    solu = Solution()

    arr = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    result = solu.minimumTotal(arr)
    print("result is: ", result)


    """
if __name__ == "__main__":
    assert Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11
    """