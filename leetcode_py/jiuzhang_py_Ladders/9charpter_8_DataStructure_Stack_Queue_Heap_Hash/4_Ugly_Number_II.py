#coding=utf-8

import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    #Hint:  Use a set() to remove duplicates()ex: 2 * 3 = 6; 3 * 2 = 6 too;
    #       Use heapq to store each qualified integer.

    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([1])

        for i in range(n):
            val = heapq.heappop(heap)

            for num in [2, 3, 5]:
                element = val * num
                if element not in visited:
                    visited.add(element)
                    heapq.heappush(heap, element)

        return val
