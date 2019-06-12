#coding=utf-8
#1）array中每个元素表示在这一步最大能跳多少步，而非一定要这么多步
#2）可以超过最后那个数
#3) reach means it reachs the last index
"""
reach是为了记录每个点最远能到达的位置，取当前值与i+A[i]的较大值，
这样，即使reach不再变大，但i+A[i]依然能帮助走完整个array 
"""

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False

        length, reach = len(A), 0

        for i in range(length):
            if i > reach or reach >= length -1:
                break

            reach = max(reach, i + A[i])

        return reach >= length - 1

    def canJump_mythought(self, A):
        if not A:
            return False

        length, start = len(A), 0

        while start < length:
            start += A[start]
            if start >= length:
                return True

        return False
        

if __name__ == '__main__':
    solu = Solution()
    nums = [2,3,1,1,4]
    result = Solution().canJump(nums)
    print("final result is: ", result)