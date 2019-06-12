#coding=utf-8
"""
Hint：使用left and right表示每次剩下的左右括号数目
1）当left == right == 0时，说明找到一个
2）当left > 0时，继续添加left
3）当right > 0且left < right时，说明right还可以添加，继续添加right

"""
class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        if not n or n < 0:
            return []

        results = []
        self.helper(n, n, '', results)

        return results

    def helper(self, left, right, substr, results):
        print('     '+substr+'   ')
        if left == 0 and right == 0:
            results.append(substr)

        if left > 0:
            #print('cur substr is: ', substr + '(')
            self.helper(left - 1, right, substr + '(', results)

        if right > 0 and left < right:
            #print('cur substr is: ', substr + ')')
            self.helper(left, right - 1, substr + ')', results)

if __name__ == '__main__':
    solu = Solution()
    n = 3
    result = solu.generateParenthesis(n)
    print("result is: ", result)