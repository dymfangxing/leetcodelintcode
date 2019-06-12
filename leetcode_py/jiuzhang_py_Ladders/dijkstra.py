from collections import defaultdict

class Graph(object):
	def __init__(self):
	    self.nodes = set()
	    self.edges = defaultdict(list)
	    self.distances = defaultdict()

	def add_node(self, node):
		self.nodes.add(node)

	def add_edge(self, from_node, to_node, distance):
		self._add_edge(from_node, to_node, distance)
		self._add_edge(to_node, from_node, distance)

	def _add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance

def dijkstra(graph, init_node):
    nodes = set(graph.nodes)
    visited_nodes_w_weight = {init_node:0}
    path = {}

    while nodes:
    	minor_weight_node = None
    	#now we have to find minor weight node
    	for node in nodes:
            if node in visited_nodes_w_weight:
    	        if minor_weight_node is None:
    		    minor_weight_node = node
    		elif visited_nodes_w_weight[node] < visited_nodes_w_weight[minor_weight_node]:
    		    minor_weight_node = node

        print minor_weight_node

    	if minor_weight_node is None:
    	    break
        #remove this current processing node
        #from nodes.
        #so it won't be visited again
    	nodes.remove(minor_weight_node)
    	cur_wt = visited_nodes_w_weight[minor_weight_node]
  
        #find edges from this current processing nodes
    	for node in graph.edges[minor_weight_node]:
    	#weight of init node to current	processing node + current node to this edge
    	    weight_from_initnode = cur_wt + graph.distances[(minor_weight_node, node)]
    	    if node not in visited_nodes_w_weight or weight_from_initnode < visited_nodes_w_weight[node]:
    	        visited_nodes_w_weight[node] = weight_from_initnode
    	        path[node] = minor_weight_node

    return visited_nodes_w_weight, path

def shortest_path(graph, init_node, target_node):
    visited_nodes_w_weight, path = dijkstra(graph, init_node)
    print visited_nodes_w_weight
    print path
    
    weight = 0
    route = []
    cur_node = target_node

    while cur_node != init_node:
    	weight += visited_nodes_w_weight[cur_node]
    	route.append(cur_node)
    	cur_node = path[cur_node]
    
    route.append(init_node)
    route.reverse()
    return route, weight

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
    '''
    print "node is: ", g.nodes
    print "edges is: ", g.edges
    print "distances is: ", g.distances
    '''
    path, weight = shortest_path(g, 1, 5)
    print "shortes path is:", path, ", weight is: ", weight
