#coding=utf-8
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if not dict:
            return 0
        
        dict.add(end)
        queue = deque([(start, 1)])

        while queue:
            word, count = queue.popleft()
            if word == end:
                return count
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in dict:
                        dict.remove(new_word)
                        queue.append((new_word, count + 1))

        return 0

if __name__ == '__main__':
    elems = set(["hot","dot","dog","lot","log"])
    #elems = ["hot",dot","dog","lot","log"]
    solu = Solution()
    print(solu.ladderLength('hit', 'cog', elems))