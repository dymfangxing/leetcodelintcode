#coding=utf-8
"""
题目：找一个字符串里各种排列组合是不是存在一个palindrome。

思路：统计每个字符出现次数，如果存在2个字符出现是奇数次，则False
"""

from collections import defaultdict
class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        if s is None:
            return False
            
        if len(s) == 0:
            return True
        
        c_dict = defaultdict(int)
        num_of_odd = 0
        
        for i in range(len(s)):
            c_dict[s[i]] += 1
            
        for key in c_dict:
            if c_dict[key] % 2 == 0:
                continue
            else:
                num_of_odd += 1
                
        return num_of_odd < 2