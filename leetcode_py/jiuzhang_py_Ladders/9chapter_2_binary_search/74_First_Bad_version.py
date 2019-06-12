class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start, end = 1, n

        while start + 1 < end:
            mid = (start + end)//2

            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start

        if SVNRepo.isBadVersion(end):
            return end

        return -1

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    test_array = [1,2,2,4,5,5]
    target = 5
    print(solu.lastPosition(test_array, target))

