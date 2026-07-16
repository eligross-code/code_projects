### This is the graph class.

class Graph():
    # the graph class takes in a set of weighted edges and vertices
    def __init__(self, edges, vertices, directed = False):
        self.directed = directed
        # these are sets
        self.edges = edges
        self.vertices = vertices

        # this is our dict we will construct
        self.adjacency_dict = {}

        # make sure we don't recreate adjacnency dict if it already exists

        self.dict_made = False

    def create_adjacency_dict(self):
        

        ### there are some edge cases to consider, and therefore errors to return.
        if self.dict_made:
            raise Exception("Adjacency dict already exists.")
        if (self.edges is None) or (self.vertices is None):
            raise Exception("Edges and vertices must be defined before creating adjacency dict.")

        if (len(self.edges) == 0) or (len(self.vertices) == 0):
            raise Exception("Edges and vertices must be non-empty before creating adjacency dict.")
        
        if (not isinstance(self.edges, set)) or (not isinstance(self.vertices, set)):
            raise Exception("Edges and vertices must be sets before creating adjacency dict.")


        # create the adjacency dict

        for vertex in self.vertices:
            self.adjacency_dict[vertex] = set()

        for edge in self.edges:
            if len(edge) != 3:
                raise Exception("Edges must be tuples of length 2 with a weight.")
            
            if edge[0] not in self.vertices or edge[1] not in self.vertices:
                raise Exception("Edges must be between vertices in the graph.")
            
            if edge[0] == edge[1]:
                raise Exception("Edges must be between different vertices.")
            
            if edge[2] < 0:
                raise Exception("Edges must have non-negative weights.")
            

            self.adjacency_dict[edge[0]].add((edge[1],edge[2]))
            self.adjacency_dict[edge[1]].add((edge[0],edge[2]))

            

        self.dict_made = True

    def solve(self, start_node, end_node):

        # given a starting and finish node, find the shortest path between them using dijkstra's algorithm

        # start with neighbors of start
        weighted_neighbors = self.adjacency_dict[start_node]

        # now...the hard part is setting up the piority queue and the visited set. The priority queue will be a list to start (deque in prod).
        priority_queue = []

        # visited set.
        visited_set = set()
        visited_set.add(start_node)

        # shortest path dict. This will have nodes and the shortest path so far...if a shorter path is found, update.
        shortest_path_dict = {}


        # now we have to explore ... we assume that the graph is connected and can only expand one node at a time.
        # now this becomes recursive. We need to check to see if it has been explored, if yes, see if new shortest path, if yes, update, if no, keep, if not, add to visited set and move on.
        # when this becomes recusive, I am not sure if the dicts and stuff stay in scope 
        for neighbor, distance in weighted_neighbors:


            visited_set.add(neighbor)







        