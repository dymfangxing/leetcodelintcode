#coding=utf-8
"""
Hint:

wordladder I:只要找一条最短的就行了，所以bfs从start->end,取一个word就从dict删一个

wordladder II: 从尾巴开始是为了防止大量的重复，比如：

                 A
               /   \ 
              C     D
             / \   / \
            一堆   E  F 
             \ /   \ /
              E     B

从start A开始的话，还要去过左边的一堆，就浪费时间了：
直接从end：B 开始往回走到A为止，就不用管左边那一堆了
"""
from collections import deque

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    """
    BFS + DFS:
    1) use BFS to remember each word's distance from end
    2) use DFS to find each path which the distance btw neighbor words is 1
    """
    def findLadders(self, start, end, dic):
    	dic.add(start)
    	dic.add(end)
    	distance = {}
    	results = []

    	self.bfs(end, dic, distance)
        print("distance is: ", distance)
    	self.dfs(start, end, distance, dic, [start], results)

    	return results

    def dfs(self, cur, target, distance, dic, subset, results):
    	if cur == target:
    	    results.append(list(subset))
    	    return
        
        for word in self.getNextWords(cur, dic):
            if distance[word] != distance[cur] - 1:
                continue
    	    subset.append(word)
    	    self.dfs(word, target, distance, dic, subset, results)
    	    subset.pop()

    def bfs(self, start, dic, distance):
        distance[start] = 0
        queue = deque([start])

        while queue:
            word = queue.popleft()
            for next_word in self.getNextWords(word, dic):
                """
                这一句很重要！如果一个word两次被找到，只取第一次的。因为
                第一次肯定是最小的
                """
            	if next_word not in distance:
        	        distance[next_word] = distance[word] + 1
        	        queue.append(next_word)


    def getNextWords(self, word, dic):
    	words = []
    	for index in range(len(word)):
    	    for char in "abcdefghijklmnopqrstuvwxyz":
    	        next_word = word[:index] + char + word[index + 1:]
    	        if next_word in dic and next_word != word:
    	            words.append(next_word)

    	return words

if __name__ == '__main__':
    elems = {"hot","dot","dog","lot","log"}
    #elems = ["hot",dot","dog","lot","log"]
    sol = Solution()
    print(sol.findLadders('hit', 'cog', elems))
