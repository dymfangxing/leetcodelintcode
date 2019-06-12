#coding=utf-8
"""
题目要求是找交集
"""
"""
solu1: use set
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection1(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
            
        a = set(nums1)
        b = set(nums2)
        results = []
        
        for n in a:
            if n in b:
                results.append(n)
                
        return results

    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
            
        a = set(nums1)
        results = set()
        
        for n in a:
            if n in nums2:
                results.add(n)
                
        return list(results)
 
"""
solu 2: brute force
"""       
class Solution1:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 and not nums2:
            return

        results = []
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                results.append(nums1[i])
                i += 1
                j += 1
                
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    j += 1

        return results

        
if __name__ == '__main__':
    solu = Solution()
    nums1 = [1, 2, 2, 1,3,4]
    nums2 = [2, 2,3]
    result = solu.intersection(nums1, nums2)
    print("result is: ", result)