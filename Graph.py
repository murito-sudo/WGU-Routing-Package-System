import csv
from Vertex import Vertex
from Route import Route



##This is our graph class, here we create the best path the truck will take

class Graph:
    
    ##Our constructor for the graph class
    
    def __init__(self, size):
        
        ##Declaring the size of the distance array
        ##the distance array contains the dictionary of the adjacency matrix
        ##distanceOptimize is the nodes of the trip, each node connected to its nearest neighbour
        ##self.distances is O(n)
        self.size = size
        self.distances = [None for i in range(self.size)]
        self.distanceOptimize = []
          
        
        ##Opening the WGUPS Distance Table file
        file2 = open('WGUPS Distance Table.csv', "U")
        
        ##we create a list of the from the csv file above so we can iterate it without creating a new instance of file
        csvreader2 = list(csv.reader(file2))
        #We open the same file with another variable to populate the locations array
        file = open('WGUPS Distance Table.csv', "U")
        type (file)
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        ##creating locations array to save the addresses 
        self.locations = [None for i in range(len(header))]
        y = 0
        ##adding the address to the locations array and modify it so it matches the address from the HashTable packages
        #Time complexity: O(n^2)
        #Space Complexity: O(N)
        for x in range(2,len(header)):
            self.locations[y] = header[x]
            self.locations[y] = self.locations[y].replace("South", "S")
            self.locations[y] = self.locations[y].replace("North", "N")
            self.locations[y] = self.locations[y].replace("East", "E")
            self.locations[y] = self.locations[y].replace("West", "W")
            self.locations[y] = self.locations[y].replace(",", "")
        
            y=y+1
            
        
        
        t=2
        csvreader2 = csvreader2[1:]
        y=0
        
        
        ##Here we create our adjacency matrix, finding the relationship in the rows
        #Time complexity: O(n^3)
        #Space Complexity: O(n^2)
        for m in range(0,len(csvreader2)):
            self.distances[y] = Vertex(self.locations[y].split("\n")[1].strip())
            s= 0
            
            for q in csvreader2:
                
                if len(q[t].strip()) != 0:
                    self.distances[y].get_vertices()[self.locations[s].split("\n")[1].strip()] = float(q[t])
                else:
                    self.distances[y].get_vertices()[self.locations[s].split("\n")[1].strip()] = float(-1)
                    
                
                
                
                s=s+1
            t=t+1
            
            y=y+1
            
        
        y = 0
            
        ##Here we plug the column values to fill our whole adjacency matrix    
        #Time complexity: O(n^3)
        for m in csvreader2:
            t = 2
            s = 0
            
            for q in range(0,self.size-1):
                
                if self.distances[y].get_vertices()[self.locations[s].split("\n")[1].strip()] == -1:
                    self.distances[y].get_vertices()[self.locations[s].split("\n")[1].strip()] = float(m[t])
                    
                s=s+1
                t=t+1
                
            y=y+1
            
            
        
            
            
        
    ##Here we sort each row of our adjaency matrix, so we can have more flexibility
    ##Time Complexity: O(N^2LogN) 
    def sort_graph(self):
        for x in range(len(self.distances)):
            self.distances[x].sort_vertex()
            
       
    
    
    ##Here's our method to optimize the path and know which node is best
    ##for this algorithm i used a nearest neighbor algorithm approach and assign each node to the nearest non visited neighbour
    ##Time complexity: O(n^4)
    ##Space Complexity: O(n^3)
    def optimize_path(self):
        locale = "4001 S 700 E" 
        route = []
        route2 = []
       
        
        
        for i in range(0, len(self.distances)):
            
            for val in self.distances:
                if i == len(self.distances)-1:
                    self.distanceOptimize.append(Route(locale, "4001 S 700 E", self.distances[0].get_vertices()[locale]))
                    break
                
                
                
                if val.get_vertex_address() == locale:
                    for key, value in val.get_vertices().items():
                        if val.get_vertex_address() not in route and key not in route2 and key != "4001 S 700 E" and key != val.get_vertex_address():
                            self.distanceOptimize.append(Route(locale, key, value))
                            route.append(val.get_vertex_address())
                            route2.append(key)
                            locale = key
                            
                            break
        
        
        
        
        
        
    
            
    #method to get the next route 
    #Time Complexity: O(1)
    #Space Complexity: O(n)       
    def next_route(self, index):
        return self.distanceOptimize[index]
        
        
            
        
    #getting the distanceOptimize array
    def get_distance_optimizer(self):
        return self.distanceOptimize
    
    
    #Method we use to measure the total miles to get to the hub in each Node
    #Time Complexity: if the total miles to get to Node x to the hub is less than 6 the time complexity is O(1)
    #If it is greater than or equal to 6, the time complexity is O(n^2)
    def cut_to_hub(self, location):     
        min = self.distances[0].get_vertices()[location]
        if self.distances[0].get_vertices()[location] >= 8:
            for val in self.distances:
                if val.get_vertex_address() == location:
                    x=0
                    for key, value in val:
                        if x == 0:
                            x=x+1
                            continue
                        mina = val.get_vertices()[key]
                        mina += self.distances[0].get_vertices()[key]
                        if mina < min:
                            min = mina
                            
                    
                break
                    
        return min
    
 