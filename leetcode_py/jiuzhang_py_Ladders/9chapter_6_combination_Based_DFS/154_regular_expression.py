class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.helper(0, s, 0, p, {})

    def helper(self, i, src, j, pattern, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(src):
            return self.isEmpty(pattern[j:])

        if j == len(pattern):
            return False

        if j + 1 < len(pattern) and pattern[j + 1] == "*":
            #two situation: in order to use at least once of *,
            #you have to : match s&p's first char AND 
            #check src's 2nd char with origin pattern(to see if * can 
            #match more than 1 char apart from the first one)

            #OR use 0 times *'s char
            matched = self.charMatch(src[i], pattern[j]) and \
                      self.helper(i + 1, src, j, pattern, memo) or\
                      self.helper(i, src, j + 2, pattern, memo)
        else:
            matched = self.charMatch(src[i], pattern[j]) and \
                      self.helper(i + 1, src, j + 1, pattern, memo)

        memo[(i, j)] = matched

        return matched

    def charMatch(self, s, p):
        return s == p or p == "."

    def isEmpty(self, pattern):
        if len(pattern) % 2 == 1:
            return False

        for index in range(0, len(pattern)//2):
            if pattern[index * 2 + 1] != "*":
                return False

        return True

if __name__ == '__main__':
    #test_data = [1,2,3,None,5]
    solu = Solution()
    #nums = []
    s = "aab"
    p = "a*b"
    result = solu.isMatch(s,p)
    print("result is: ", result)
