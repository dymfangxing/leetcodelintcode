#coding=utf-8
class Solution:
"""
1.在原数组上操作
2.将去除重复之后的元素放在数组的开头
3.返回去除重复元素之后的元素个数
"""
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if nums is None:
            return -1

        dict_table, result = {}, 0

        for num in nums:
            if num not in dict_table:
                dict_table[num] = True
                nums[result] = num
                result += 1

        return result

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #test_array = [4, 5, 1, 2, 3]
    test_array = [1,3,1,4,4,2]

    print(solu.deduplication(test_array))