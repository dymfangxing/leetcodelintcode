#coding=utf-8
"""
solu 1:最好的解法是dp：bottom->top
"""
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
"""
solu 2: divide_conquer + memolization:

memo存从这个点到底部的min_path
"""

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})
        
    # 函数返回从 x, y 出发，走到最底层的最短路径值
    # memo 中 key 为二元组 (x, y)
    # memo 中 value 为从 x, y 走到最底层的最短路径值
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
            
        # 如果找过了，就不要再找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        # 在 return 之前先把这次找到的最短路径值记录下来
        # 避免之后重复搜索
        memo[x][y] = min(left, right) + triangle[x][y]
        return memo[x][y]



"""
dfs做也可以，不过由于许多重复计算，会TLE，所以要记忆化搜索
"""
import sys
class Solution_1:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
            
        self.minTotal = sys.maxsize
        subset = [triangle[0][0]]
        level, index = 0, 0
        self.dfs(triangle, subset, level, index)
        
        return self.minTotal
        
    def dfs(self, tri, subset, level, index):
        if len(tri) - 1 == level:
            self.minTotal = min(self.minTotal, sum(subset))
            return
        
        for i in range(index, len(tri[level])):
            subset.append(tri[level+1][index])
            self.dfs(tri, subset, level + 1, index)
            subset.pop()
            
            subset.append(tri[level+1][index + 1])
            self.dfs(tri, subset, level + 1, index+1)
            subset.pop()

if __name__ == '__main__':
    solu = Solution()

    arr = [[-1],[2,3],[1,-1,-3]]
    result = solu.minimumTotal(arr)
    print("result is: ", result)


"""
    arr = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
"""
