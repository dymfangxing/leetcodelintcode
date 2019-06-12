#coding=utf-8

"""
Hint：快慢指针
left:慢指针
right：快指针

1）left初始为0，遍历right从0 - len(s)时的情况。
需要注意的是，一旦s[left:right+1] distinct num > k时，
right再++，也是更加>k，所以不用继续算后面的情况，直接left++，然后进入下一个right的情况

2）while的时候只要loop当k>len(counter)的情况，因为目前的counter[s[left]]之前已经被
加过了，所以只要永远确保len(count) <= k的时候的值能被算到

"""
from collections import defaultdict
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
            
        #counter = {}
        counter = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(s)):
            #counter[s[right]] = counter.get(s[right], 0) + 1
            counter[s[right]] += 1
            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest


    def lengthOfLongestSubstringKDistinct1(self, s, k):
        # write your code here
        if not s or k < 0:
            return -1
            
        slow, fast = 0, 0
        max_substr_len = 1
        distinct_size = 1
        distinct_hash = {}
        distinct_hash[s[slow]] = 1
        
        while fast < len(s):
            distinct_size = len(distinct_hash)

            if distinct_size == k:
                substr_len = fast - slow + 1
                if substr_len > max_substr_len:
                    max_substr_len = substr_len
            if distinct_size > k:
                if distinct_hash[s[slow]] > 1:
                    distinct_hash[s[slow]] -= 1
                else:
                    del distinct_hash[s[slow]]
                slow += 1
            else:
                fast += 1
                print("slow is:", slow)
                print("fast is: ", fast)
                if fast < len(s):
                    max_substr_len = fast - slow + 1
                    if s[fast] not in distinct_hash:
                        print("not exist")
                        distinct_hash[s[fast]] = 1
                    else:
                        distinct_hash[s[fast]] += 1

        return max_substr_len

if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    S = "eceba"
    k = 3
    print(solu.lengthOfLongestSubstringKDistinct(S, k))
