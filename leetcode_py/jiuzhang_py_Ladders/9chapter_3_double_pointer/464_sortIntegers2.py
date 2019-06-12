class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return

        self.quickSort(A, 0, len(A) - 1)

        print("A is sorted as:", A)

    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[(start + end)//2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    test_arrary = [0, 1, 0, 3, 12]
    print(solu.sortIntegers2(test_arrary))
    test_arrary1= [5,4,3,2,1]
    print(solu.sortIntegers2(test_arrary1))
