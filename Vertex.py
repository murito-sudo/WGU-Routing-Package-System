##Vertex class to Store the adjacency matrix in a dictionary
##All methods except from sort_vertex are O(1)

class Vertex:
    def __init__(self, address):
        self.address = address
        self.vertices = {}
        
        
    def get_vertex_address(self):
        return self.address
    def get_vertices(self):
        return self.vertices
    
    def set_vertex_address(self, address):
        self.address = address
        
        
    ##Sorting each adjacency node in order to have more flexibility
    ##Time Complexity O(NlogN)
    def sort_vertex(self):
        self.vertices =  dict(sorted(self.vertices.items(), key=lambda item: item[1], reverse=False))