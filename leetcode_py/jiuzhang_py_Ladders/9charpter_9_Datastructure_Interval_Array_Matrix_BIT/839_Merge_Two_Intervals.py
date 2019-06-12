# -*- coding: utf-8 -*- 
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        intervals = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i].start <= list2[j].start:
                self.push(list1[i], intervals)
                i += 1
            else:
                self.push(list2[j], intervals)
                j += 1

        while i < len(list1):
            self.push(list1[i], intervals)
            i += 1

        while j < len(list2):
            self.push(list2[j], intervals)
            j += 1

        return intervals

    def push(self, interval, intervals):
        #if result is empty, directly add into it
        if not intervals:
            intervals.append(interval)
            return

        #start from here, always take last element from intervals to process
        last_interval = intervals[-1]

        #if last interval and new interval are not overlapped, directly append
        if last_interval.end < interval.start:
            intervals.append(interval)
            return
        #pick either last interval or new interval's end as the end
        intervals[-1].end = max(intervals[-1].end, interval.end)

"""
if __name__ == "__main__":
    A = []
    A.append(Interval(1, 7))
    A.append(Interval(5, 6))
    A.append(Interval(3, 4))
    print("Before sort:")
    for i in A:
        print("({},{})".format(i.left, i.right))

    # 由于定义了__lt__，方法，此处可以直接调用sort方法进行升序排序
    A.sort()

    print("After sort:")
    for i in A:
        print("({},{})".format(i.left, i.right))
"""

if __name__ == '__main__':
    solu = Solution()
    list1 = [(1,2),(3,4)]
    list2 = [(4,5),(6,7)]

    result = solu.mergeTwoInterval(arr)
    print("result is: ", result)
