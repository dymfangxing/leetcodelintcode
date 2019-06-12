#coding=utf-8

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        results = []
        memo = [None for _ in range(len(nums))]
        self.dfs(nums, [], results, memo)
        
        return results

    def dfs(self, nums, subset, results, memo):
        if len(subset) == len(nums):
            results.append(list(subset))
            return

        for i in range(0, len(nums)):

            """
            1，2，2’‘，2’‘’
            2 为首字母的情况
            """
            if memo[i] == True:
                continue
            #not memo[i - 1] means its previous same value num needs to be picked 
            #beforehand
            #in another word, only if its previous same value is picked
            #then you can pick the current one: for example: 1, 2, 2, 2, 2,...
            #in this way we gurantee every element is picked.
            #比如1，2'，2''，2'''，2''''吧，
            #如果某个2是false，其实表示还没选呢，应该去选；true表示已经选了。
            #那你要先选没选过的，就是之前那个2；
            #等之前那个2选过了，再选后面那个2

            """
            比如1，2'，2''，2'''，2''''吧

            之前都没问题，直到：

            2'开头时，虽然2''是false，但nums[i] != nums[i-1],所以没问题

            但2''开头时，nums[i] == nums[i-1](2'' and 2'),且2'是false,
            说明还没呢（其实是和2'时的情况重复了），所以要去掉。
            """
            """
            2''或者2‘’‘为首字母的情况

            补充：这一步和subsetII里面i > start是一个意思，目的是去掉重复里的第一个元素
            """

            if nums[i] == nums[i - 1] and memo[i - 1] is False:
                continue

            subset.append(nums[i])
            memo[i] = True
            self.dfs(nums, subset, results, memo)
            memo[i] = False
            subset.pop()


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,2]
    result = solu.permuteUnique(nums)
    print("result is: ", result)
