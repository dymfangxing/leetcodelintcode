#coding=utf-8

import heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

#Hint: use heapq to store the distance of each point

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        self.queue = []

        for point in points:
            dist = self.distance(point, origin)
            #Hint: Return these points sorted by distance, 
            #if they are same in distance, sorted by the x-axis, 
            #and if they are same in the x-axis, sorted by y-axis.
            #so smaller dist/x/y will always in front of others
            heapq.heappush(self.queue, (-dist, -point.x, -point.y))

            #heaqp pop up the smallest element 
            if len(self.queue) > k:
                heapq.heappop(self.queue)

        ret = []

        while len(self.queue) > 0:
            _, x, y = heapq.heappop(self.queue)
            ret.append(Point(-x, -y))

        ret.reverse()

        return ret
        

    def distance(self, target, origin):
        return (target.x - origin.x)**2 + (target.y - origin.y)**2
