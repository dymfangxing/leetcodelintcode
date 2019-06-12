#coding=utf-8

from collections import deque
from collections import defaultdict


"""
Hint: use a dict to store how many of each character
      use a queue to store each character's showing up time in order
"""
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        if not str:
            return

        dic = defaultdict(int)
        queue = deque([])

        for i in range(len(str)):
            dic[str[i]] += 1
            if str[i] not in queue:
                queue.append(str[i])

        while len(queue) > 0:
            char = queue.popleft()
            if dic[char] == 1:
                return char

if __name__ == '__main__':
    solu = Solution()
    string = "abaccdeff"
    result = solu.firstUniqChar(string)
    print("result is: ", result)