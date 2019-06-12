class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        results = []
        memo = [None for _ in range(len(str))]
        #sort string by convert it to list, then convert it back to str
        str_list = list(str)
        str_list.sort()
        str = "".join(str_list)

        self.dfs(str, [], results, memo)
        return results

    def dfs(self, str, subset, results, memo):
    	#'->'.join(path)
    	if len(subset) == len(str):
    	    results.append("".join(subset))
    	    return

    	for i in range(len(str)):
            if memo[i] == True:
            	continue
            
            if i > 0 and str[i] == str[i - 1] and not memo[i - 1]:
                continue
    	    subset.append(str[i])
    	    memo[i] = True
    	    self.dfs(str, subset, results, memo)
    	    memo[i] = False
    	    subset.pop()
        


if __name__ == '__main__':
    solu = Solution()
    string = "aab"
    result = solu.stringPermutation2(string)
    print("result is: ", result)
