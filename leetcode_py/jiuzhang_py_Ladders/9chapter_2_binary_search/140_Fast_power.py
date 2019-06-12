#coding=utf-8
"""
 (n/2)
(a     %b)**2%b
"""

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1%b
            
        if n == 1:
            return a%b

        if n%2 == 1:
            return (a%b * (self.fastPower(a, b, n//2)%b)**2)%b
        else:
            return ((self.fastPower(a, b, n//2)%b)**2)%b


#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    a = 3
    b = 1
    n = 0
    print(solu.fastPower(a, b, n))

