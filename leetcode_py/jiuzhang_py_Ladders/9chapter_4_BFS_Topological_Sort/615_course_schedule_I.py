#coding=utf-8

from collections import deque

'''
Hint:
1) get edges[] depends on preqeuisities
2) get in_degree[] depends on preqeuisities
3) do topological sorting
'''
"""
(1,0)表示1依赖于0，则在graph中表示为 0->1，对1来说，入度是1，
对0 来说，neighbor=[1]
所以先构建edge表，再构建indegree表，再topological sorting

只有所有course都被放到queue里去过，才说明无环，可以选。
只要有环，就不行。可以自己画一下，就清楚了。
"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        edges = {n:[] for n in range(numCourses)}
        indegree = {n: 0 for n in range(numCourses)}

        for i,j in prerequisites:
            edges[j].append(i)
            indegree[i] += 1

        start = deque(list())

        for index in range(numCourses):
            if indegree[index] == 0:
                start.append(index)

        cnt = 0
        while start:
            course = start.popleft()
            for neighbor in edges[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    start.append(neighbor)
            cnt += 1

        return cnt == numCourses
    
if __name__ == '__main__':
    #elems = [3,9,20,"#","#",15,7]
    #elems = [3,9,20,8,2,15,7]
    '''
    creating graph
    '''
    
    prerequisites = [[1,0],
                     [2,0],
                     [0,1]]
    n = 3
    
    #prerequisites = [[1,0]]
    #n = 2
    '''
    end
    '''
    solu = Solution()

    result = solu.canFinish(n, prerequisites)
    print("final result is: ", result)