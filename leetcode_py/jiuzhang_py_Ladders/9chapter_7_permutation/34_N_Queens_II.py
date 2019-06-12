class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
#hint: think it like add n numbers into a list:
#[1,2,3,4], [2,1,3,4] ...
#the index of nums in this list represents the row 
    def totalNQueens(self, n):
        # write your code here
        if not n:
            return []

        cols = []
        results = []
        self.dfs(n, cols, results)

        return len(results)

    def dfs(self, n, cols, results):
    	row = len(cols)

    	if row == n:
    	    results.append(list(cols))
    	    return

        for col in range(n):
            if not self.isValid(col, row, cols):
                continue
          
            cols.append(col)
            self.dfs(n, cols, results)
            cols.pop()

    """
    def drawBoard(self, cols):
        board = []
        n = len(cols)

        for i in range(n):
            row = ["Q" if j == cols[i] else "." for j in range(n)]
            board.append(''.join(row))

        return board
    """
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
    result = solu.totalNQueens(n)
    print("result is: ", result)
