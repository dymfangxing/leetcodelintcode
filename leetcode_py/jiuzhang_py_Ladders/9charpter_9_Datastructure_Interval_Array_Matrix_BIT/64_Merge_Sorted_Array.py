#coding=utf-8
"""
Hint：从尾巴朝向头补
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        index = m + n - 1
        i = m - 1
        j = n - 1
        
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                index -= 1
                i -= 1
            else:
                A[index] = B[j]
                index -= 1
                j -= 1
                
        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1


        #do not need to think abt i since if B is running out, the element left in A are the smallest and are inorder
        """
        while i >= 0:
            A[index] = A[i]
            index -= 1
            i -= 1
        """
