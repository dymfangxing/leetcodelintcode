#coding=utf-8

#DFS？
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #先把beginWord放入curr_level，然后从word_list里找只变了一个char
        #的word，找到了就放入next_level，并从word_list里remove
        #再将next_level变成cur_level,继续word_list里找
        #不断循环直到找到endWord
        #本来不加这句是过不了AC的，加set后就可以了，因为这样速度就快了search files from list was O(n),
        #but now it is O(1)！
        #set will return a new object here. not directly operate on wordList
        wordList = set(wordList)
        #so if we just 
        #wordList = list(wordList)
        #it will also allow the next call workable instead of cleaning up list
        #end
        cur_level = [beginWord]
        next_level = []
        depth = 1
        wordLen = len(beginWord)

        while cur_level:
            for element in cur_level:
            	if element == endWord:
            		return depth
            	else:
            		for i in range(wordLen):
            			for c in "abcdefghijklmnopqrstuvwxyz":
            				temp_word = element[:i] + c + element[i+1:]
            				if temp_word in wordList:
            				    next_level.append(temp_word)
            				    wordList.remove(temp_word) 
            depth += 1
            cur_level = next_level
            next_level = []

        return 0

    def ladderLength_1(self, beginWord, endWord, wordList):
    	#wordList是set型的话，检查一个单词在不在其中(word in dict)为O(1)时间
    	#设单词长度为L, dict里有N个单词, 每次扫一遍dict判断每个单词是否与当前单词
    	#只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母, 看变换出的
    	#词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。

    	#这个只是为了让当找到match时，word能被remove掉：wordList.remove(word). 否则数组里删不掉的
        #lintcode上直接传进来就是set，所以就不用这句了
        wordList = set(wordList)
        #print("ladderLength_1, wordlist is: ", wordList)
        queue = collections.deque([[beginWord, 1]]) #for 1st element, length is 1
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1]) #同层的word，其depth都相同
        return 0

if __name__ == '__main__':
    """主函数"""
    elems = ["hot","dot","dog","lot","log","cog"]
    #elems = ["hot",dot","dog","lot","log"]
    slu = Solution()
    print(slu.ladderLength('hit', 'cog', elems))
    #elems = ["hot","dot","dog","lot","log","cog"]
    print(slu.ladderLength_1('hit', 'cog', elems))

