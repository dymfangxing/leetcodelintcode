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

