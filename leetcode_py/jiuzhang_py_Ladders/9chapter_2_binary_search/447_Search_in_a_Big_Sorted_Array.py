class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader or target is None:
            return -1
        
        #cover index = 0 case
        if reader.get(0) == target:
            return 0

        start, index = 1, 1

        """
        用二分，由于不能得到end的位置，只能不断尝试，找到包含target的（start，index）的区间，然后二分
        """
        while reader.get(index) < target:
            start = index
            index *= 2
        
        while start + 1 < index:
            mid = start + (index - start)//2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) >= target:
                 index = mid
        
        if reader.get(start) == target:
            return start

        if reader.get(index) == target:
            return index

        return -1

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    test_array = [1,2,2,4,5,5]
    target = 5
    print(solu.lastPosition(test_array, target))

