class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if not A:
            return None
        
        temp = [0 for _ in range(len(A))]
        self.mergeSort(A, 0, len(A) - 1, temp)
        
    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return
        
        self.mergeSort(A, start, (start + end)//2, temp)
        self.mergeSort(A, (start + end)//2 + 1, end, temp)
        self.merge(A, start, end, temp)
        
    def merge(self, A, start, end, temp):
        middle = (start + end)//2
        leftIndex = start
        rightIndex = middle + 1
        tempIndex = start
        
        while leftIndex <= middle and rightIndex <= end:
            if A[leftIndex] < A[rightIndex]:
                temp[tempIndex] = A[leftIndex]
                tempIndex += 1
                leftIndex += 1
            else:
                temp[tempIndex] = A[rightIndex]
                tempIndex += 1
                rightIndex += 1
        
        while leftIndex <= middle:
            temp[tempIndex] = A[leftIndex]
            tempIndex += 1
            leftIndex += 1
            
        while rightIndex <= end:
            temp[tempIndex] = A[rightIndex]
            tempIndex += 1
            rightIndex += 1
            
        for i in range(start, end + 1):
            A[i] = temp[i]

if __name__ == '__main__':
    A = [3,2,1,4,5]
    print("Before sorting: ", A)
    Solution().sortIntegers(A)
    print("After sorting: ", A)