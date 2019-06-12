#coding=utf-8
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return []

        nums.sort()
        size = len(nums)

        dp = [1] * size
        parents = [-1] * size

        max_size, maxVal_index = 0, -1

        #subset里面任何2个数互相除，大的都要能整除小的

        #dp是一个index array，i是index，dp[i]表示这个index时候最大subset的size
        #parents:这个数是由之前哪个转移过来的，这个数能整除的上一个数在nums中的index
        #当parent数组中某数为-1时，表示这个数自己是一个集合

        #先用i遍历每个数字，然后用j从后向前寻找能被nums[i]整除的数字，
        #这样如果判断能整除的时候，再判断dp[i] < dp[j] + 1，
        #即对于以i索引结尾的最长的数组是否变长了。如果没变长，dp[j] + 1 = dp[i]
        #问题：相等的时候，dp[i]难道不需要更新吗？因为要把dp[i]作为新的maxsize啊？？？
        #为了保证求出的集合是最大的？但是相等的时候也是比j大的啊……
        #在变长的情况下，需要更新dp[i]，同时使用parent[i]更新i的前面能整除的数字。
        for i in range(size):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    #[1 3 9 18 20 54]
                    #Here's the explanation for 1 + dp[j] > dp[i] :
                    #you want the "largest" subset, so the count should be increasing
                    #比如[1 3 9 18, ...]
                    """
                    当num[i]是18时，dp[i] default是1；
                    先check num[j] = 9,因为num[9]肯定是>=1的；
                    那么若能整除时，dp[j] + 1肯定 > 1，就可以替换，dp[i] = dp[j] + 1;
                    后面的dp[j - 1], dp[j - 2]...如果之前也和dp[j]的值相同，那并没有更新dp[i]的必要；
                    只有当后面dp[j - 1], dp[j - 2]...的值 + 1 > dp[i]时候
                    （因为dp[j - 1], dp[j - 2]可能之前已经被更新过好几次）
                    才要再更新dp[i]
                    """
                    if dp[j] + 1 > dp[i]:
                        print("dp[j] + 1 > dp[i]")
                        dp[i] = dp[j] + 1
                        parents[i] = j

            if dp[i] >= max_size:
                max_size = dp[i]
                maxVal_index = i
            print("i is: ", nums[i])
            print("dp is: ", dp)
            print("parents: ", parents)
            print("#########################")


        result = []
        for i in range(max_size):
            result.append(nums[maxVal_index])
            maxVal_index = parents[maxVal_index]

        return result

if __name__ == '__main__':
    solu = Solution()
    #nums =  [1,2,3]
    nums = [1,2,4,8,9,11,13,72] 
    print("orgin nums is: ", nums)
    result = Solution().largestDivisibleSubset(nums)
    print("final result is: ", result)
    