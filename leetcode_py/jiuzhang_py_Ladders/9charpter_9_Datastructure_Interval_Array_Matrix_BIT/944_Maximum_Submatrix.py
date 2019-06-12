# -*- coding: utf-8 -*- 

"""
6-3 update solu： 没用prefix sum，更容易理解
solu 1: 我们会做max sub array， 所以只要把matrix降维成1D Array，然后再call max sub array即可

降维的方法是：
比如最开始是这个矩阵：
    matrix = [
            [1,3,-1,5],
            [2,3,-2,2],
            [-1,-2,-3,-1],
            [5,4,-2,1]
          ]

那我们开始的时候先算从第0列到第len(matrix) - 1列的结果：
是从第0列开始叠加：

第0列 [1,3,-1,5] 的max sub array
sum_arr= [1,3,-1,5]， 算这个sum_arr的max sub array；

接下来算第0列+第1列的max sub array:
 [1,3,-1,5],
 [2,3,-2,2]

即同列相加，生成一个sum_arr= [3,6,-3,7],
算这个sum_arr的max sub array；更新到result里去

。。。

依次类推


这个loop完了之后，我们再算从第1列到第len(matrix) - 1列的结果，是从第1列开始按列叠加

再后面，再算从第二列开始的结果。。。

最后算最后一列的结果
"""

class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        result = 0
        for i in range(len(matrix)):
            """
            循环这个矩阵的行数
            """
            """
            每次循环开始时，sum_val按列数置0
            """
            sum_val = [0 for m in range(len(matrix[0]))]
            print("sum is: ", sum_val)
            for j in range(i, len(matrix)):
                for k in range(0, len(matrix[0])):
                    sum_val[k] += matrix[j][k]
                temp = self.maxSubarray(sum_val)
                result = max(result, temp)
        return result
        
    def maxSubarray(self, nums):
        dp = [None for _ in range(len(nums))]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
            
        return max(dp)

"""
solu 2
"""
import sys

"""
Hint:

1) 按行取每行的prefix sum
2）循环取行不同i，j之间的和，放在一个arr里，比较arr的subarr max val
"""

class Solution2:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        self.row = len(matrix)
        self.col = len(matrix[0])

        #prefix sum btw row and row
        prefix_sum = self.getPrefixSum(matrix)
        maxSum = -sys.maxsize

        for up in range(self.row):
            for down in range(up, self.row):
                arr = self.compression(matrix, up, down, prefix_sum)
                #print("arr is: ", arr)
                #find the max sum in this array. same as 41_max subarray
                maxSum = max(maxSum, self.maxSubArray(arr))

        return maxSum

    def getPrefixSum(self, matrix):
        """
        Original Matrix:
        [
            [1,3,-1],
            [2,3,-2],
            [-1,-2,-3]
        ]
        Initialize by converting to prefix sum matrix (with row + 1)
        [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        """
        prefix_sum = [[0 for i in range(self.col)] for j in range(self.row + 1)]

        for i in range(self.row):
            for j in range(self.col):
                prefix_sum[i + 1][j] = prefix_sum[i][j] + matrix[i][j]
        #print(prefix_sum)
        return prefix_sum

    def compression(self, matrix, up, down, prefix_sum):
        #This array stores the sum btw different row i to j
        arr = [0 for i in range(self.col)]
        for i in range(self.col):
            arr[i] = prefix_sum[down + 1][i] - prefix_sum[up][i]

        return arr

    def maxSubArray(self, nums):
        # write your code here
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum

if __name__ == '__main__':
    solu = Solution()
    #arr = [-3,1,2,-3,4]
    matrix = [
            [1,3,-1,5],
            [2,3,-2,2],
            [-1,-2,-3,-1],
            [5,4,-2,1]
          ]
    result = solu.maxSubmatrix(matrix)
    print("result is: ", result)

