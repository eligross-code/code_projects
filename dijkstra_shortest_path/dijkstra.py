### this will be the dijkstra class

class Dijkstra:
    # we pass in a graph object, which has the adjacency dict, edges, and vertices.
    def __init__(self, graph):
        self.graph = graph
        self.shortest_path_dict = {}
        self.visited_set = set()
        self.priority_queue = []
        self.previous_node = {}

    def one_expansion(self, node, end_node):
        # recusive function that expands the graph one node at a time, and returns the shortest path and length if the end node is reached.

        if node == end_node:
            return [node], 0
        
        # so ... we begin at the first node.
        self.visited_set.add(node)

        # then, we look at all neighbors of that node and add them to the priority queue based on distance
        neighbors = self.graph.adjacency_dict[node]

        # neighbors is a list of tuples...we want to sort based on the weight of the edge, which is the second element of the tuple.

        for neighbor, weight in neighbors:
            self.add_to_sorted_list((neighbor, weight))

        # decide the next node to visit.
        next_node, next_weight = self.priority_queue[0]

        if next_node == end_node:
            return [node, next_node], self.shortest_path_dict[node] + next_weight

        # now, if the next node has been visited and the aggregate weight is greater than the current distnace + this weight, then we have to update.
        # however, we need to keep track of the shortest path to each node, otherwise, it will just reset to the path from the neighbor, not from the start node.
        # so we need to keep track of the shortest path to each node, and somehow see if a shorter path exists.
        if next_node in self.visited_set:
            if next_weight < self.shortest_path_dict[next_node]:
                self.shortest_path_dict[next_node] = next_weight
    
        
        else:
            # if not, we can add the weight to the shortest path dict and continue.
            self.shortest_path_dict[next_node] = next_weight
            self.visited_set.add(next_node)





        return path, length

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