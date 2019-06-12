#use double pointer.
#we could use Hash Map too.
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums or target is None:
            return []

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[target - nums[i]] = i
            else:
                indice1 = hashMap[nums[i]]
                indice2 = i
                return [indice1 + 1, indice2 + 1]

        return []

    def twoSum1(self, nums, target):
        # write your code here
        if not nums or target is None:
            return -1
            
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                return [start + 1, end + 1]
                
        if nums[start] + nums[end] == target:
            return [start + 1, end + 1]
        else:
            return -1

#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    nums = [2, 7, 11, 15]
    target = 9
    print(solu.twoSum(nums, target))

