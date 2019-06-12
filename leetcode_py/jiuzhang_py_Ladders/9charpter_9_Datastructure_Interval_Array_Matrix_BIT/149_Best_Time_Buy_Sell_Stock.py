
#coding=utf-8

"""
思路：

记录：
1）最低的股票价格
2）最多赚了多少钱

因为只买卖一次，所以只要不断更新这2个值，最后返回2）即可
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
            
        total = 0
        low = sys.maxsize
        
        for price in prices:
            if price < low:
                low = price
            if price - low > total:
                total = price - low
                
        return total
            
        
