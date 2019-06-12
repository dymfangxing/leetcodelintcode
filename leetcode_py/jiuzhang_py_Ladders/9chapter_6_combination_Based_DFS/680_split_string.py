#coding=utf-8


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        subset = []
        result = []

        self.helper(s, subset, result)
        return result

    #s: the rest of string to be cut
    #subset: substring(s) which is palidrome and has been cut
    #result: final subsets
    def helper(self, s, subset, result):
        if len(s) == 0:
            result.append(list(subset))
        #at least cut 1 character
        #at most cut to the end of this string
        """
        i是隔板位置，所以从1开始（至少选1个），到len(s)为止（最后一个元素的后面）

        len(prefix) > 2, 说明每次割掉的prefix string最多length=2，再多就不割了

        比如1，2，3，4，5，6

        那么prefix_string最多就是”1“和”1，2“

        传到后面去的s就是”2，3，4，5，6“或者”3，4，5，6“，不会再有更多的下去了
        """
        for i in range(1,len(s) + 1):
            prefix = s[:i]
            #so only prefix with length 1 or 2 will be processed
            #and the rest will be put into helper for next level processing
            if len(prefix) > 2:
            	continue
            subset.append(prefix)
            #pass the rest of string for deeper processing
            self.helper(s[i:], subset, result)
            subset.pop()

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    s = "aabcd"
    result = solu.splitString(s)
    print("result is: ", result)