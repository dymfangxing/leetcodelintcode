#coding=utf-8

"""
别忘了n < 0时的情况
"""
class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if x is None or n is None:
            return -1

        if n < 0:
            n *= -1
            return self.myPow(1/float(x), n)

        if n == 0:
            return 1

        if n == 1:
            return x

        if n%2 == 1:
            return x*(self.myPow(x, n//2)**2)
        else:
            return self.myPow(x, n//2)**2



#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    a = 2
    n = -2
    print(solu.myPow(a, n))

