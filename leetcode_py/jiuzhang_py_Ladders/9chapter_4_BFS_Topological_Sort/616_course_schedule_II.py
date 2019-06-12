#coding=utf-8

from collections import deque

'''
Hint:
1) get edges[] depends on preqeuisities
2) get in_degree[] depends on preqeuisities
3) do topological sorting
4) if there is no way to finish all courses, return 0
'''
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