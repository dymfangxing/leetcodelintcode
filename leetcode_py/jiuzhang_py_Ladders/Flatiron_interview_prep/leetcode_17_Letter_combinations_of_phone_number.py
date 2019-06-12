
#coding=utf-8

"""
https://www.1point3acres.com/bbs/thread-475072-1-1.html
Given phone idalboard and a string of numbers, find all the valid English words.
这时候就要你假设你有一个可以让你查找english word的数据结构，我当时第一选择是set

followup 1: set is too expensive, 
do you have other data sturcture for u to store the English dictionary?

followup 2: what if we want to return all the valid English words sorted by frequency?
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
