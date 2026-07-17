### this will be the dijkstra class

class Dijkstra:
    # we pass in a graph object, which has the adjacency dict, edges, and vertices.
    def __init__(self, graph):
        self.graph = graph
        self.shortest_path_dict = {}
        self.visited_set = set()
        self.priority_queue = []
        self.previous_node = {}
        
        # in the code, I found it useful to create a prespective set, these are all the nodes that need to be sorted in the priority queue, but have not been visited yet.
        self.perspective_nodes = set()
    def one_expansion(self, node, end_node):
        # recusive function that expands the graph one node at a time, and returns the shortest path and length if the end node is reached.

        if not True:
            raise Exception("Node must be in the graph.")
        
        else:
            
            # check end condition
            if node == end_node:
                
                # for end node to be expanded into, it must already have been added to the piority queue
                return self.shortest_path_dict[node]
            
            else:

                # if not the end node, then we must look at the neighbors of this node, then sort them into the priority queue, then select the next node to explore.

                # this returns a list of tuples
                neighbors = self.graph[node]

                # we need to update the shortest path dict for each neighbor
                # I am not sure if this has the shortest path for this node...if we start the dict with shortest_path[start_node] = 0, then we can update like this.

                for neighbor, weight in neighbors:
                    self.perspective_nodes.add(neighbor)
                    
                    
                    # remove the node we just searched
                    if node in self.perspective_nodes:
                        self.perspective_nodes.remove(node)

                    if neighbor in self.visited_set:
                        # if the neighbor is already in the dict, compare and then chose to update
                        if neighbor in self.shortest_path_dict:
                            # if the new path is shorter, update the shortest path dict and previous node dict
                            if self.shortest_path_dict[node] + weight < self.shortest_path_dict[neighbor]:
                                self.shortest_path_dict[neighbor] = self.shortest_path_dict[node] + weight
                                self.previous_node[neighbor] = node
                    else:
                        # put the shortest paths in the dict ... node will always have one when this is code with node ...
                        self.shortest_path_dict[neighbor] = self.shortest_path_dict[node] + weight
                        self.previous_node[neighbor] = node

                    
 
                # resort the priority queue based on the shortest path to each neighbor
                # note, cannot just sort the priority queue based on visited node, these are all prospective nodes. We could also make a set for this.
                self.priority_queue = sorted(list(self.perspective_nodes), key=lambda x: self.shortest_path_dict[x])


                # final recusive call
                return self.one_expansion(self.priority_queue[0], end_node)

    def sort_list(self, list, final=[]):
        ### sort the list of integer
        
        # if the len is 0, return the final list
        if len(list) == 0:
            return final
        
        # else recusively call, finding the minuim element and sorting the rest
        else:
            # set the first element to the min to start
            min = list[0]

            # find min
            for ele in list:
                if ele < min:
                    min = ele
            # add lowest
            final.append(min)
            # remove
            remove = set(list).remove(min)
            # convert back to list
            new_list = list(remove)

            # rec call.
            self.sort_list(new_list, final)


    def add_to_sorted_list(self, tuple):
        # our assumed invariant is that the list is sorted, and we want to add a new tuple to the list while maintaining the sorted order based on the second element of the tuple (the weight).

        if self.priority_queue == []:
            self.priority_queue.append(tuple)
            return
        
        vertex, weight = tuple

        for ele in self.priority_queue:
            if weight < ele[1]:
                index = self.priority_queue.index(ele)
                self.priority_queue.insert(index, tuple)
                return
            
    
    def get_node_chain(self, node):
          if node is None:
            return []
          
          else:
                return self.get_node_chain(self.previous_node[node]) + [node]

    def solve(self, start_node, end_node):
        
        self.shortest_path_dict[start_node] = 0
        self.previous_node[start_node] = None

        # start the recusive function
        return self.one_expansion(start_node, end_node)
    
