##Route class to store the nodes from each address and determine which should be the next route based on distance
##Time complexity of all methods and constructor is O(1)
class Route:
    def __init__(self, currLoc, nextLoc, miles):
        self.currLoc = currLoc
        self.nextLoc = nextLoc
        self.miles = miles
        
        
    def get_curr(self):
        return self.currLoc
    
    
    def get_next(self):
        return self.nextLoc
    
    
    def get_miles(self):
        return self.miles
