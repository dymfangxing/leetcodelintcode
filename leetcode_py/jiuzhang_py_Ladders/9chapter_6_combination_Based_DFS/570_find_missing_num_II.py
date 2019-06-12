#coding=utf-8

"""
edge condition：
1) prefix_str 不能以0开始
2）prefix_str不能 > n
3) prefix_str不能已经在subset里出现过
4) 使用set(list())作为subset的type，这样在3）时，time complexity = O(1)
"""
class Solution:
    def findMissing2(self, n, string):
        # write your code here
        if n < 0 or n > 30:
            return -1
        
        if not string:
            return -1
            
        #prefix_length = len(str(n))
        self.missing = 0
        self.found = False
        self.missings = None
        subset = set(list())

        self.dfs(string, n, subset)

        print("missings arr is: ", self.missings)

        if self.found:
            return self.missing
        else:
            return -1
            
        
    def dfs(self, s, n, subset):
        """
        当整个s遍历完，且len(subset) == n-1，说明找到了
        """
        if len(s) == 0 and len(subset) == n - 1:
                self.found = True
                sum_n, sum_subset = 0, 0
                for num in range(1, n + 1):
                    sum_n += num 
                for c in subset:
                    sum_subset += int(c) 
                self.missing = sum_n - sum_subset
                self.missings = list(subset)

        for i in range(1, len(s) + 1):
            if not self.found:
                prefix_str = s[:i]

                if len(prefix_str) > len(str(n)):
                    continue
                if prefix_str[0] == '0':
                    continue
                if prefix_str in subset:
                    continue
                if int(prefix_str) > n:
                    continue
                    
                subset.add(prefix_str)
                self.dfs(s[i:], n, subset)
                subset.remove(prefix_str)

if __name__ == '__main__':
    solu = Solution()
    n = 10
    string = "5641278910"
    result = solu.findMissing2(n, string)
    print("result is: ", result)
    
    n = 20
    string = "19201234567891011121314151618"
    result = solu.findMissing2(n, string)
    print("result is: ", result)

    n = 28
    string = "111098654327128213127262524232120191817161514"
    result = solu.findMissing2(n, string)
    print("result is: ", result)


