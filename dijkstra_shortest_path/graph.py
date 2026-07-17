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


        # later we will need the priority queue and visited set.
        self.priority_queue = []
        self.visited_set = set()


        # shortest path dict. This will have nodes and the shortest path so far...if a shorter path is found, update.
        self.shortest_path_dict = {}

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
