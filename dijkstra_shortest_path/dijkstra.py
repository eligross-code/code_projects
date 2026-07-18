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

        # base case
        if node == end_node:
            return (self.get_node_chain(node), self.shortest_path_dict[node])
        

        # recursive case
        else:
            # no need to check if the node is in visited, as shortest legth is guaranteed to be rewritten, and therefore, the invariant holds.

            #check neighbors

            for neighbor, weight in self.graph[node]:
                # add to fronteir / possible nodes to visit only if it has not been visited yet. Not needed, we can do thsi through the shortest path dict and visited set. 
                """if neighbor not in self.visited_set:
                    self.perspective_nodes.add(neighbor)"""

                # WAIT....can't blindly update this, since it might have a lower value if anythig.
                # maybe just check, if so, then update. Using visited here would not make sense, since we want to update shortest path regardless of visited status.
                if neighbor not in self.shortest_path_dict:
                    # THIS DISTANCE IS FINAL
                    self.shortest_path_dict[neighbor] = self.shortest_path_dict[node] + weight

                    # how the final distance was created
                    self.previous_node[neighbor] = node

                # if neighbor exists and there is a shorter path. COULD HAPPEN AS LONG AS IT HAS NOT BEEN POPPED.
                elif neighbor not in self.visited_set and self.shortest_path_dict[node] + weight < self.shortest_path_dict[neighbor]:
                    self.shortest_path_dict[neighbor] = self.shortest_path_dict[node] + weight
                    self.previous_node[neighbor] = node

            # now remove the node from the perspective set, since it has been visited.
            # CAREFUL, start node might not be in teh set, so only remove if it is in the set.
            """if node in self.perspective_nodes:
                self.perspective_nodes.remove(node)
                """
            # sort based on the shortest path so far
            # FILTER, otherwise previous distances could be in the priority queue
            self.priority_queue = self.sort_list([(node, weight) for (node, weight) in self.shortest_path_dict.items() 
                                                      if (node not in self.visited_set)], final=[])

            # select the next node
            next_node = self.priority_queue[0][0]

            # ONCE POPPED, distance is set, and it has been visited.
            self.visited_set.add(next_node)

            #finally, make the rec call
            return self.one_expansion(next_node, end_node)

                
    def sort_list(self, list_of_tuples, final=[]):
        ### sort the list of tuples based on the second element of the tuple (the weight) using recursion. This is a helper function for the priority queue.
        
        # if the len is 0, return the final list
        if len(list_of_tuples) == 0:
            return final
        
        # else recusively call, finding the minuim element and sorting the rest
        else:
            # set the first element to the min to start
            min = list_of_tuples[0][1]
            low = list_of_tuples[0]
            # find min
            for node, weight in list_of_tuples:
                if weight < min:
                    min = weight
                    low = (node, weight)
            # add lowest
            final.append(low)
            # remove
            temp = set(list_of_tuples)
            
            temp.remove(low)
            # convert back to list
            new_list = list(temp)

            # rec call.
            return self.sort_list(new_list, final)


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
        self.visited_set.add(start_node)


        # we do not need the perspective set, since we already have the shortest path dict and can filter based on visited.
        # start the recusive function
        return self.one_expansion(start_node, end_node)
    
