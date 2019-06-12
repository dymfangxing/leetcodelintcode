# -*- coding: utf-8 -*- 

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if not A and not B:
            return 0

        size = len(A) + len(B)

        if size % 2 == 1:
            return self.findNum(A, B, size//2 + 1) * 1.0
        else:
            return (self.findNum(A, B, size//2 + 1) + self.findNum(A, B, size//2))/2.0

#Hint: be careful for either A or B is empty
    def findNum(self, A, B, k):
        start, end = self.getRange(A, B)

        while start + 1 < end:
            mid = (start + end)//2

            if self.getNumSmallerOrEqual(A, B, mid) >= k:
                end = mid
            else:
                start = mid

        if self.getNumSmallerOrEqual(A, B, start) >= k:
            return start

        return end

    def getRange(self, A, B):
        if not A:
            return B[0], B[-1]

        if not B:
            return A[0], A[-1]

        return min(A[0], B[0]), max(A[-1], B[-1])

    def getNumSmallerOrEqual(self, A, B, val):
        return self.getNumSmallerOrEqualInArray(A, val) +\
               self.getNumSmallerOrEqualInArray(B, val)

    def getNumSmallerOrEqualInArray(self, arr, val):
        if not arr:
            return 0

        start, end = 0, len(arr) - 1

        while start + 1 < end:
            mid = (start + end)//2
            
            if arr[mid] > val:
                end = mid
            else:
                start = mid
    
        if arr[start] > val:
            return start

        if arr[end] > val:
            return end

        return end + 1



if __name__ == '__main__':
    solu = Solution()
    A = [1,2,3,4,5,6]
    B = [2,3,4,5]

    result = solu.findMedianSortedArrays(A, B)
    print("result is: ", result)
