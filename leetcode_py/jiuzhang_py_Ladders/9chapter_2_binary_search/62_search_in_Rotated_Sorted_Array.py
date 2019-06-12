#coding=utf-8

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or target is None:
            return -1
        
        left, right = 0, len(A) - 1

        while left + 1 < right:
            print "left is: ", left
            print "right is: ", right

            mid = (left + right)//2

            print "mid is: ", mid
            print "###########################"

            if A[mid] == target:
                return mid
        """
        注意不要 == mid了，因为上面已经算过了
        """
            #middle is at left part
            if A[mid] > A[right]:
                if target >= A[left] and target < A[mid]:
                    right = mid
                else:
                    left = mid 
            else: #middle is at right part
                if target > A[mid] and target <= A[right]:
                    left = mid
                else:
                    right = mid


        if A[left] == target:
            return left

        if A[right] == target:
            return right

        return -1 

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #test_array = [4, 5, 1, 2, 3]
    test_array = [6,8,9,1,3,5]
    #test_array = [5]

    print(solu.search(test_array, 5))