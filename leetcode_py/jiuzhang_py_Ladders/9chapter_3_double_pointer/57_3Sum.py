#coding=utf-8

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return -1

        numbers.sort()
        results = []
        for index, n in enumerate(numbers):
            result = self.findPair(numbers, n, index)
            """
            这里也可以用set()去重
            """
            if len(result):
                for re in result:
                    if re not in results:
                        results.append(re)
        
        return results
        
    def findPair(self, numbers, n, index):
        start, end = 0, len(numbers) - 1
        result = []
        
        while start + 1 < end:
            if start == index:
                start += 1
            if end == index:
                end -= 1

            if numbers[start] + numbers[end] > -n and start + 1 < end:
                end -= 1
            elif numbers[start] + numbers[end] < -n and start + 1 < end:
                start += 1
            elif numbers[start] + numbers[end] == -n and start + 1 < end:
                result.append(sorted([numbers[start], numbers[end], numbers[index]]))
                end -= 1
                start += 1

        return result

"""
solu2： 用nums[i] == nums[i - 1]: continue 保证去重
"""
    def threeSum2(self, nums):
        nums.sort()
        results = []
        length = len(nums)
        """
        这里最后处理的数是nums[len(nums) - 3]，
        是因为3sum最少也要3个数，当nums[len(nums) - 3]时，
        left = len(nums) - 2, right =  len(nums) - 1
        就到头了
        """
        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1;
            target = -nums[i]

            self.find_two_sum(nums, left, right, target, results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                """
                发现相同后，直接跳到下一个
                """
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    nums = [-1, 0, 1, 2, -1, -4]
    print("solu 1 is: ", solu.threeSum(nums))
    nums1 = [2,7,11,15]
    print("solu 2 is: ", solu.threeSum(nums1))


