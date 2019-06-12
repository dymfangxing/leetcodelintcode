#coding=utf-8
"""
Hint: 二分:https://www.cnblogs.com/grandyang/p/5933787.html

因为是非负整数，所以：

low：m最大等于len(nums) - 1,即每个数都是一个子集，low=max(nums)
high: m=1,即所有数都在一个子集里，high = sum(nums)

对其他m的值来说，max subarray sum肯定在low，high之间

用二分，然后将(low+high)//2 传入valid function，

valid function的作用是验证这个值(mid)能否用m个subarray达到，
如果达到了，说明这个值还能更小，所以hi = mid

否则说明这个值用m个array是达不到的，要提高mid，lo = mid + 1
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValid(mid):
            cnt = 0
            cur = 0
"""
如果目前和超过mid了，从目前这个数开始一个新的subarray(cur = num)
cnt += 1

然后check cnt是否大于m，是的话直接返回False，否则返回True，说明mid还能更小
"""
            for num in nums:
                cur += num
                if cur > mid:
                    cnt += 1
                    cur = num
                if cnt >= m:
                    return False
                    
            return True

        lo = max(nums)
        hi = sum(nums)

        while lo < hi:
            mid = lo + (hi - lo)//2

            if isValid(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo