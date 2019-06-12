#coding=utf-8

from collections import deque

DIRECTION = [
             (1, 2),  (1, -2),
             (-1, 2), (-1, -2),
             (2, 1),  (2, -1),
             (-2, 1), (-2, -1)
            ]
"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
    """
    Hint: 用一个dict来记录访问过的点，以及这个点距离start的distance
    """
        distance = {(source.x, source.y):0}
        queue = deque([(source.x, source.y)])

        while queue:
            x, y = queue.popleft()

            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]

            for x_add, y_add in DIRECTION:
                x_new, y_new = x + x_add, y + y_add

                if not self.isValid(grid, x_new, y_new):
                    continue
                
                if (x_new, y_new) in distance:
                    continue
                
                distance[(x_new, y_new)] = distance[(x, y)] + 1
                queue.append((x_new, y_new))

        return -1
        
    def isValid(self, grid, x, y):
        m = len(grid[0])
        n = len(grid)

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return not grid[x][y]

if __name__ == '__main__':
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    src = Point(2, 0)
    dst = Point(2, 2)

    solu = Solution()
    result = solu.shortestPath(grid, src, dst)

    print("Result is: ", result)