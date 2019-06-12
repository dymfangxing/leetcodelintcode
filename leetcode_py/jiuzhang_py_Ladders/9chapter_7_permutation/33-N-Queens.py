#coding=utf-8
"""
solu 5-24-2019 by myself:

1) cols既存col又存row，cols[i]是col，i就是row
2) 判断点是否valid的3种情况：建议画个3x3的棋盘，比划一下就清楚了
    a）在同一列上 c == col
    b）在左斜线上 r+c== col+row
    c) 在右斜线上 r-c == row-col
"""

    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []
        
        results = []
        cols = []
        
        self.helper(n, results, cols)
        
        return results
        
    def helper(self, n, results, cols):
        row = len(cols)
        
        if row == n:
            results.append(self.drawBoard(cols, n))
        
        for col in range(n):
            if not self.isValid(col, row, cols):
                continue
            cols.append(col)
            self.helper(n, results, cols)
            cols.pop()
            
            
            
    def drawBoard(self, cols, n):
        """
        return array
        """
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []
        
        for r,c in enumerate(cols):
            board[r][c] = 'Q'
            result.append("".join(board[r]))
            
        return result
    
    def isValid(self, col, row, cols):
        """
        return Boolean
        """
        for r, c in enumerate(cols):
            """
            row == r is not needed since one row only has one point
            """
            if col == c:
                return False
            if col + row == r + c or r - row == c - col:
                return False
                
        return True

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
#hint: think it like add n numbers into a list:
#[1,2,3,4], [2,1,3,4] ...
#the index of nums in this list represents the row 
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []

        cols = []
        results = []
        self.dfs(n, cols, results)

        return results

    def dfs(self, n, cols, results):
    """
    cols既存col又存row，cols[i]是col，i就是row
    """
    	row = len(cols)

    	if row == n:
            #we can first test it by check if this list is correct
            #then we use a draw function to draw it out
    	    #results.append(list(cols))
            results.append(self.drawBoard(cols))
    	    return

        for col in range(n):
            if not self.isValid(col, row, cols):
                continue
          
            cols.append(col)
            self.dfs(n, cols, results)
            cols.pop()

    def drawBoard(self, cols):
        board = []
        n = len(cols)

        for i in range(n):
            row = ["Q" if j == cols[i] else "." for j in range(n)]
            board.append(''.join(row))

        return board

    """
    3 situations to check if it is valid:
        1) if this number has existed in cols
        2) row + col == r + c
        3) row - col == r - c
    (These two are for: slash, and back-slash)
    """
    def isValid(self, col, row, cols):
    	for r, c in enumerate(cols):
    	    if c == col:
    	        return False
    	    if c + r == col + row or r - c == row - col:
    	        return False

        return True

if __name__ == '__main__':
    solu = Solution()
    n = 4
    result = solu.solveNQueens(n)
    print("result is: ", result)


        
