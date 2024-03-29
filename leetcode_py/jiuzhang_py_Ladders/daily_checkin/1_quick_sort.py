class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if not A:
            return A
            
        self.quickSort(A, 0, len(A) - 1)
        
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[(start + end)//2]
            
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A [right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

if __name__ == '__main__':
    test_data = [3,2,1,4,5]
    solu = Solution()
    solu.sortIntegers(test_data)
    print("combination is: ", test_data)
