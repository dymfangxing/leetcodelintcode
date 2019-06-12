#coding=utf-8

from collections import deque

#https://www.lintcode.com/problem/sequence-reconstruction
#http://www.shengjie.me/2018/07/23/leetcode-444/
#https://www.jiuzhang.com/solution/sequence-reconstruction/#tag-highlight-lang-python
"""
如果将每个数字作为一个节点，其前后关系作为一条边，则这道题的seqs参数可以转为一个图数据结构
以例子4为例， [5,2,6,3] -> [5,2],[2,6],[6,3], [4,1,5,2] -> [4,1],[1,5],[5,2]
基于以上的edge list可以构造一个图数据结构，而参数org则是满足有向图的遍历路径。

当且仅当org是唯一合法的拓扑遍历路径时，返回true: 判断这个是否是唯一的路径的方法是看queue
里面是否永远只有1个element
"""
'''
Hint:
topological sorting
1) build edges[] and indegree[] based on seqs
2) compare it with org to see if they match
'''
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        results = self.topoSort(graph)

        return results == org

    def build_graph(self, seqs):
        graph = {}

        for seq in seqs:
            for num in seq:
                if num not in graph:
                    graph[num] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def topoSort(self, graph):
        indegrees = self.getIndegree(graph)

        start = []
        results = []

        for node in graph:
            if indegrees[node] == 0:
                start.append(node)

        while start:
            if len(start) > 1:
                return
            node = start.pop(0)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    start.append(neighbor)
            results.append(node)

        return results

    def getIndegree(self, graph):
        indegrees = {node:0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees
    
if __name__ == '__main__':
    org = [4,1,5,2,6,3]
    seqs = [[5,2,6,3],[4,1,5,2]]

    solu = Solution()
    result = solu.sequenceReconstruction(org, seqs)

    print("Result is: ", result)