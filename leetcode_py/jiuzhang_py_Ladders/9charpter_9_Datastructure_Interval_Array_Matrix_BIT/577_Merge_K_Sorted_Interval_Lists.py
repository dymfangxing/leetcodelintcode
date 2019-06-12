#coding=utf-8

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Hint:

Use heap to store every interval list's first element's start,
use itertools to keep add ID in heap (in order to avoid same interval
    cannot be compared issue.)

不用itertools,用一个全局counter也是可以的
"""


import heapq
import itertools

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        results = []
        heap = []
        counter = itertools.count()

        #i is used to avoid same interval cannot be compared
        #for i, interval_list in enumerate(intervals):
        for interval_list in intervals:
            if len(interval_list) == 0:
                continue
            heapq.heappush(heap, (interval_list[0].start, next(counter), \
                                  interval_list, 0))

        while len(heap) > 0:
            _, _, interval_list, index = heapq.heappop(heap)
            self.mergeInterval(interval_list[index], results)
            if index + 1 < len(interval_list):
                heapq.heappush(heap, (interval_list[index + 1].start, \
                                      next(counter), \
                                      interval_list, index + 1))

        return results

    def mergeInterval(self, interval, results):
        if len(results) == 0:
            results.append(interval)

        if results[-1].end < interval.start:
            results.append(interval)

        results[-1].end = max(results[-1].end, interval.end)

