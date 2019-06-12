class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    """
    注意：如果是[1, 0, 0, 3, 1, 2, 5]
    最开始left和right都指第0个，
    那left和right互换，还是保持不动，
    然后再都往前。
    总之left永远指0，right永远指1
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return nums
        #left always points to 0
        #right always points to non-0
        left, right = 0, 0

        while right < len(nums):
            #right stops at first 0
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
     
        return nums

#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    test_arrary = [0, 1, 0, 3, 12]
    print(solu.moveZeroes(test_arrary))
    test_arrary1= [5,4,3,2,1]
    print(solu.moveZeroes(test_arrary1))
