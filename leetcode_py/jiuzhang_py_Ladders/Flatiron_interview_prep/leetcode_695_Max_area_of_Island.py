#coding=utf-8

"""
Use bfs: not sure if i should also use DFS:
https://leetcode.com/problems/max-area-of-island/

我先写了一个修改input array + 全局变量存当前size的
followup1 不修改array：再用一个visited array
followup2 不用全局变量：递归返回值作为新的size

问了一个2D矩阵DFS找最大连通分量的问题，
我写完之后问如果这个2D矩阵不能fit mainmemory那么应该怎么做
"""

from collections import deque

delta = [(1,0), (-1, 0), (0, 1), (0, -1)]

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        self.maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
        
        return self.maxArea
    
    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        cur_area = 1
        grid[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in delta:
                if not self.isValid(grid, x + delta_x, y + delta_y):
                    continue
                queue.append((x + delta_x, y + delta_y))
                grid[x + delta_x][y + delta_y] = 0
                cur_area += 1
                
                
        if cur_area > self.maxArea:
            self.maxArea = cur_area
            
    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]
