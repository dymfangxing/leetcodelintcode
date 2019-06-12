from collections import defaultdict

class Solution(object):
    def findSentence(self, string, word_list):
        if not string or not word_list:
            return ""

        self.hash_string = defaultdict(int)
        self.result_str = None

        for c in string:
            if c == " ":
               continue
            self.hash_string[c.lower()] += 1 

        memo = [None for _ in range(len(word_list))]
        self.helper([], word_list, memo)
        
        return self.result_str

    def helper(self, subset, word_list, memo):
        if self.isAnagrams(subset):
            word = ' '.join(subset)
            self.result_str = word
            return

        for i in range(len(word_list)):
            if self.result_str:
                break
            if memo[i] == True:
                continue

            if memo[i - 1] == False and word_list[i] == word_list[i - 1] and i > 0:
                continue
            
            memo[i] = True
            subset.append(word_list[i])

            self.helper(subset, word_list, memo)

            memo[i] = False
            subset.pop()

        return

    def isAnagrams(self, subset):
        hash_candidate = defaultdict(int)

        for word in subset:
            for c in word:
                hash_candidate[c.lower()] += 1

        return hash_candidate == self.hash_string

if __name__ == '__main__':
    solu = Solution()
    string = "older and wiser"
    word_list = ["learned", "I", "words"]
    #word_list = ["and", "older", "wiser"]
    result = solu.findSentence(string, word_list)
    print("result is: ", result)

