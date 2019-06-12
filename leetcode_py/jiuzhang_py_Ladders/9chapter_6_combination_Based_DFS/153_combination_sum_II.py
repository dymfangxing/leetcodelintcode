class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        #num = sorted(list(set(num)))
        num.sort()
        print("num is: ", num)
        subset = []
        results = []

        self.helper(num, 0, target, subset, results)

        return results

    def helper(self, num, startIndex, target, subset, results):
"""
Input:
num is:  [1, 1, 2, 5, 6, 7, 10]

Output
[[1,1,6],[1,2,5],[1,7],[1,2,5],[1,7],[2,6]]
Expected
[[1,1,6],[1,2,5],[1,7],[2,6]]

Hint: need to add avoid duplicates code to avoid situations like: [1,2] and [1', 2]
"""   
    	if target == 0:
    		results.append(list(subset))
            return

    	for i in range(startIndex, len(num)):
    	    if target < num[i]:
    	        return
            if i > startIndex and num[i - 1] == num[i]:
                continue

    	    subset.append(num[i])
            self.helper(num, i + 1, target - num[i], subset, results)
    	    subset.pop()

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    num =  [10,1,6,7,2,1,5]
    target = 8
    result = solu.combinationSum2(num, target)
    print("combination is: ", result)
