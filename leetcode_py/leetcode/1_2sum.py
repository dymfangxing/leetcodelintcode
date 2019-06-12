#solution: Gitbook
#https://shenjie1993.gitbooks.io/leetcode-python/001%20Two%20Sum.html
#
#notes: you may not use the same element twice.
#so we should check Two indices info


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        hash_nums = {}

        for i, element in enumerate(nums):
            hash_nums[element] = i

        for index_1, element in enumerate(nums):
        	if target - element in hash_nums:
        		index_2 = hash_nums[target - element]
        		if index_2 != index_1:
        			return [index_1, index_2]
        '''
        if not nums or target is None:
            return []

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[target - nums[i]] = i
            else:
                indice1 = hashMap[nums[i]]
                indice2 = i
                return [indice1, indice2]

        return []

if __name__ == "__main__":
    #None
    #Test case 1:
    nums = [2, 7, 11, 15]

    sol = Solution()
    print sol.twoSum(nums, 11)
