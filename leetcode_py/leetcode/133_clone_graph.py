# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        # Use a Hashmap to map to each node
        #in this graph for:
        # 1) Remember the visited node
        # 2) Always be able to access to it by its label(value)
        if not node:
            return node

        cloned_node = UndirectedGraphNode(node.label)
        visited = {}
        visited[cloned_node.label] = cloned_node
        stack = [node]

        while stack:
            cur_node = stack.pop()
            for neighbor in cur_node.neighbors:
                if neighbor.label not in visited:
                    stack.append(neighbor)
                    visited[neighbor.label] = UndirectedGraphNode(neighbor.label)
                visited[cur_node.label].neighbors.append(visited[neighbor.label])
                #this is the new cloned object. do not put "neighbor" here!
                #that will point to the orig object

        return cloned_node
 
def printGraph(node):
    q ,vis = [],set([node])
    q.append(node)
    while q:
        cur = q.pop(0)
        print '  ',cur.label
        for i in cur.neighbors:
            print i.label
            if i not in vis:
                q.append(i)
                vis.add(i)
 
 
 
if __name__ ==  '__main__':
    s=Solution()
    one = UndirectedGraphNode(1)
    two = UndirectedGraphNode(2)
    three =UndirectedGraphNode(3)
    one.neighbors.append(one)
    one.neighbors.append(two)
    two.neighbors.append(three)
    #printGraph(one)
    printGraph( s.cloneGraph(one))
