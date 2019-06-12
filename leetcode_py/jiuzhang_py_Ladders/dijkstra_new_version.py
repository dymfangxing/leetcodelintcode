from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.nodes = set()  #nodes looks like: set([1,2,3,4,5,6, ...])
        self.edges = defaultdict(list)     #edges looks like: {1:[2,3,4], 2:[1,4,5], ...}
        self.distances = defaultdict() #distances looks like: {(1,2):5, (1,3): 4, etc}

    def add_nodes(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        #self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, from_node):
        #we maintain two list, one is node_n_weight, anthother is path
        nodes = set(self.nodes)
        visited_node_n_weight = {from_node: 0}
        path = {}

        while nodes: #this is the nodes list which not being removed from graph yet
        #then we have a minor node to always start from the current node with minor weight
            minor_weight_node = None
            for node in nodes:
                if node in visited_node_n_weight:
                    if minor_weight_node is None: #1st time, use from node
                        minor_weight_node = node
                    elif visited_node_n_weight[node] < visited_node_n_weight[minor_weight_node]:
                        minor_weight_node = node

            print "visited node is: ", visited_node_n_weight
            print "current processing min node is:", minor_weight_node

            if minor_weight_node is None:
                break
            
            print "node: ", nodes
            nodes.remove(minor_weight_node)
            current_weight = visited_node_n_weight[minor_weight_node]

            for edge in self.edges[minor_weight_node]:
                wt = self.distances[(minor_weight_node, edge)] + current_weight

                if edge not in visited_node_n_weight or wt < visited_node_n_weight[edge]:
                    visited_node_n_weight[edge] = wt
                    path[edge] = minor_weight_node

            print "visited is: ", visited_node_n_weight
            print "path is: ", path
            print "###############################"

        return visited_node_n_weight, path

    def shortest_path(self, initial_node, goal_node):
        distances, paths = self.dijkstra(initial_node)
        print "distances list is: ", distances
        print "path list is: ", paths

        route = [goal_node]

        while goal_node != initial_node:
            route.append(paths[goal_node])
            goal_node = paths[goal_node]

        route.reverse()
        return route

if __name__ == '__main__':
    g = Graph()
    g.nodes = set(range(1, 7))
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 6, 9)
    print "node is: ", g.nodes
    print "edges is: ", g.edges
    print "distances is: ", g.distances

    #assert g.shortest_path(1, 5) == [1, 3, 6, 5]
    print "shortest path is: ", g.shortest_path(1, 5)