#coding=utf-8

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
"""
https://www.lintcode.com/problem/course-schedule/description?_from=ladder&&fromId=1
"""
from collections import deque

 class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges = {n:[] for n in range(numCourses)}
        indegree = {n: 0 for n in range(numCourses)}

        for i, j in prerequisites:
            edges[j].append(i)
            indegree[i] += 1

        start = deque(list())

        for index in range(numCourses):
            if indegree[index] == 0:
                start.append(index)
        
        cnt = 0
        result = []

        while start:
            course = start.popleft()
            for edge in edges[course]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    start.append(edge)
            cnt += 1
            result.append(course)

        if cnt == numCourses:
            return result
        else:
            return []

if __name__ == '__main__':
    #elems = [3,9,20,"#","#",15,7]
    #elems = [3,9,20,8,2,15,7]
    '''
    creating graph
    '''
    '''
    prerequisites = [[1,0],
                     [2,0],
                     [0,1]]
    n = 3
    '''
    prerequisites = [[1,0]]
    n = 2
    '''
    end
    '''
    solu = Solution()

    result = solu.canFinish(n, prerequisites)
    print("final result is: ", result)
