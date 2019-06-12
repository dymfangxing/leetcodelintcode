#coding=utf-8
"""
https://www.lintcode.com/problem/number-of-islands/description?_from=ladder&&fromId=1
"""

"""
思路：当碰到1的小岛，以此小岛建立queue，bfs之，把邻居和邻居的邻居是1的都加进queue，pop出来的小岛置0
当queue空了之后，numOfIslands++

直到遍历完所有小岛，返回numOfIslands

1）到碰到第一个小岛值是1的小岛,放入queue中

2）bfs：找到这个小岛的邻居，以及邻居的邻居，都放入queue，
       从queue中pop出来的原来是1的小岛，置为0

3）

3) 统计完全部小岛，返回total # of islands
"""
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        isIsland = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    isIsland += 1
        return isIsland

    def bfs(self, grid, i, j):
        '''
        deltaX = [1, 0, 0, -1]
        deltaY = [0, 1, -1, 0]
        '''
        print("i,j are: ", i, j)
        queue = deque([(i, j)])
        print("deque is: ", queue)
        grid[i][j] = False

        while queue:
            print("in while loop, queue is: ", queue)
            x, y = queue.popleft()
            print("in while loop, x, y are: ", x, y)
            for delta_x, delta_y in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                if not self.isValid(grid, x + delta_x, y + delta_y):
                    continue
                queue.append((x + delta_x, y + delta_y))
                grid[x + delta_x][y + delta_y] = False

    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]

#Solu2: my solu: put bfs and isvalid together
    def numIslands2(self, grid):
        if not grid or not grid[0]:
            return 0

        height = len(grid)
        width = len(grid[0])
        
        queue = deque(list())
        numOfIslands = 0
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    while queue:
                        (cur_y, cur_x) = queue.popleft()
                        for step_y, step_x in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                            x_axis = cur_x + step_x
                            y_axis = cur_y + step_y
                            if self.isValidIsland(grid, x_axis, y_axis):
                                queue.append((y_axis, x_axis))
                                grid[y_axis][x_axis] = 0
                    numOfIslands += 1

        return numOfIslands

    def isValidIsland(self, grid, j, i):
        return len(grid[0]) > j >= 0 and \
               len(grid) > i >= 0 and \
               grid[i][j]

if __name__ == '__main__':
    solu = Solution()
    nums = [[1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1],
            [1,0,0,0,0]]

    print(solu.numIslands(nums))
