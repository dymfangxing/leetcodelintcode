#coding=utf-8
"""
1) 大于左右：找到
2）大于左边小于右边->上坡->peak在右边->start=mid
3) 小于左边大于右边->下坡->peak在左边->end=mid
4）小于左右->往左右均可->start = mid or end = mid
"""
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start)//2

            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                start = mid
            elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid

        return -1


if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
