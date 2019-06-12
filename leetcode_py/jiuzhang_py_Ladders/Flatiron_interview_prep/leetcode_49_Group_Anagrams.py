
#coding=utf-8
"""
https://instant.1point3acres.com/thread/386690

今天面的是一个非面经，亏我准备了所有出现过的题。。anyway
给一个list：“steak”, "the", "hello", "word", "teaks", "tseak"
target word: "steak"
output: ["steak","teaks", "tseak"] 
这个很好做，bug free秒了
followup把我击倒了
We are now given a sentence of several words, and would like to find a sentence 
with words from D, which is an anagram of the original. 

Example “older and wiser” -> “I learned words”. 
Individual words don’t have to be anagrams of each other, 
and it doesn’t even need to be the same number of words.
"""
"""
solu 0: 每个单词sort()后作为key，相同key的加到数组里来，最后一波流输出
"""
from collections import defaultdict

class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        
        hash_dict = defaultdict(list)
        
        for word in sorted(strs):
            key_word = "".join(sorted(word))
            hash_dict[key_word].append(word)
            
        return [ v  for k,v in hash_dict.iteritems()]

"""
solu:

0. word -> frequency map
1. “older and wiser” -> frequency map.
2. backtracking all possible words?
"""

from collections import defaultdict

class Solution(object):
    def findSentence(self, string, word_list):
        if not string or not word_list:
            return ""

        self.hash_string = defaultdict(int)
        for c in string:
           if c == " ":
               continue
            self.hash_string[c] += 1 

        memo = [None for _ in range(len(word_list))]
        result_str = self.helper([], word_list, memo)
        
        return result_str

    def helper(self, subset, word_list, memo):
        if self.isAnagrams(subset, string):
            return ' '.join(subset)

        for i in range(len(word_list)):
            if memo[i] == True:
                continue

            if memo[i - 1] == False and word_list[i] == word_list[i - 1] and i > 0:
                continue
            
            memo[i] = True
            subset.append(word_list[i])

            self.helper(subset, word_list, string, memo)

            memo[i] = False
            subset.pop()

        return

    def isAnagrams(self, subset):
        hash_candidate = defaultdict(int)

        for word in subset:
            for c in word:
                self.hash_candidate[c] += 1

        return hash_candidate == self.hash_string


class Solution222(object):
    def findSentence(self, string, word_list):
        if not string or not word_list:
            return ""
        
        char_frequency_map = defaultdict(int)
        self.char_frequency_size = 0

        for c in string:
            if c == ' ':
                continue
            char_frequency_map[c] += 1
            self.char_frequency_size += 1

        word_frequency_map = defaultdict(int)
        self.word_frequncy_size = 0

        for word in word_list:
            word_frequency_map[word] += 1
            self.word_frequncy_size += 1

        subset = []

        memo = [None for _ in range(word_list)]
        word_list = sorted(word_list)

        self.helper(word_list, 0, word_frequency_map, char_frequency_map, subset, memo)

        return " ".join(subset)

    def helper(word_list, start, subset, memo):
        if 

        for i in range(len(word_list)):
            if memo[i] == True:
                continue

            if memo[i - 1] == False and word_list[i] == word_list[i - 1]:
                continue

            memo[i] = True    
            subset.append(word_list[i])

            self.helper(word_list, i + 1, subset, memo)

            subset.pop()
            memo[i] = False




if __name__ == '__main__':
    solu = Solution()
    strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = solu.groupAnagrams(strs)

    print("result is: ", result)

    string = "older and wiser"
    word_list = ["learned", "I", "words"]
    result2 = solu.findSentence(strs)



"""
solu 1: passed on lintcode but TLE on leetcode?
"""
from collections import defaultdict

class Solution0(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        
        self.results = []

        for word in strs:
            self.add(word)

        return self.results

    def add(self, word):
        if len(self.results) == 0:
            self.results.append([word])
            return

        for word_list in self.results:
            first_word = word_list[0]
            if self.isMatching(first_word, word):
                word_list.append(word)
                return

        self.results.append([word])
        return

    def isMatching(self, first_word, word):
        if len(first_word) != len(word):
            return False
        
        hash_A = defaultdict(int)
        hash_B = defaultdict(int)

        for c in first_word:
            hash_A[c] += 1

        for c in word:
            hash_B[c] += 1

        return hash_A == hash_B





