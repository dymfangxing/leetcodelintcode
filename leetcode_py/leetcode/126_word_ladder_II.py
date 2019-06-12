import collections
import string

'''
class Solution:
    #exceed time!
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordLength = len(beginWord)
        queue = collections.dequeue([beginWord, 1])

        while queue:
            #for word in cur_level:
            word, length = queue.popleft()
            if word == endWord:
    		return length
            else:
    	        for i in range(wordLength):
                    for c in "abcdefghijklmnopqrstuvwxyz":
    		        temp_word = word[:i] + c + word[i+1:]
    		        if temp_word in wordList:
    	                    queue.append([temp_word, length + 1])
    			    wordSet.remove(temp_word)
        return 0
'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        #level = {start}
        dic.add(end)
        level = set([start])
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                #for char in string.ascii_lowercase:
                for char in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
 
        while res and res[0][0] != start:            
            test = []
            for r in res:
                for p in parents[r[0]]:
                    test += [[p] + r] 
            res = test
        return res

if __name__ == '__main__':
    elems = ["hot","dot","dog","lot","log"]
    #elems = ["hot",dot","dog","lot","log"]
    sol = Solution()
    print(sol.findLadders('hit', 'cog', elems))
