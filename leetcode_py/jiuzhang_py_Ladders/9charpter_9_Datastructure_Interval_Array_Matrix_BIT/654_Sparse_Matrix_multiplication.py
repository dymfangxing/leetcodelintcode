#coding=utf-8

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        if not A or not B:
            return

        rowA = len(A)
        colA = len(A[0])
        colB = len(B[0])

        result = [[0 for j in range(colB)] for i in range (rowA)]
        
        for i in range(rowA):
            for j in range(colA):
                if A[i][j] != 0:
                    for k in range(colB):
                        result[i][k] += A[i][j] * B[j][k]

        return result

if __name__ == '__main__':
    solu = Solution()
    #arr = [-3,1,2,-3,4]
    A = [
          [ 1, 0, 0],
          [-1, 0, 3]
        ]

    B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]
        ]

    result = solu.multiply(A, B)

    print("result is: ", result)