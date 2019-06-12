class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        A = sorted(A)
        B = sorted(B)
        
        print(A)
        print(B)

        return A == B
   
"""     
        flag = False
        
        if len(A) == len(B):
            for i in range(len(A)):
                if A[i] == B[i]:
                    continue
                else:
                    break
            flag = True
        
        return flag
"""
if __name__ == '__main__':
    solu = Solution()
    
    A = "abcd"
    B = "bcad"
    result = solu.Permutation(A, B)
    print("result is: ", result)