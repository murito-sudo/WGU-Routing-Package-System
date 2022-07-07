#Here's our truck class, where we assignn packages to the truck and manage package delivery
class Truck:
    #Truck default location: Western Governors University 4001 South 700 East, Salt Lake City, UT 84107
    def __init__(self, driver, truck):
        ##Here we set the variables of the Truck class, the default location of our truck is the Hub
        self.totalDelivered = 40
        self.driver = driver
        self.packages = []
        self.location = "4001 S 700 E"
        self.totalMileage = 0
        self.truck = truck
        
        
        
    
        
        
    ##Method to add packages to the truck
    ##We can't add more than 16 packages to the truck
    ##We need to be on the hub to add the packages
    ##we check the status of the packages, if they are delivered or en route, we cannot add that package to the truck
    ##if  the package and the truck is on the hub and the truck has less than 16 packages, we will add that package to the truck and update the package status to en route and pick up time to the time the package was added to the truck
    ##Time complexity: O(1) if no collision, O(Log N) if we have collision and multiple cells, O(n) if we have collisions and just one cell
    ##Space Complexity: O(1)
    def add(self, package, time):
        
        if len(self.packages) >= 16:
            print("Truck has 16 packages already")
            return True
       
        if self.location == "4001 S 700 E":
            if package.get_delivery_status() == "delivered":
                print("package has been delivered already")
            elif package.get_delivery_status() == "en route":
                print("package is en route")
            elif package.get_delivery_status() == "at the hub":
                print("package ID: ", package.get_packageID(), " added to the truck ", self.truck)
                self.packages.append(package)
                package.set_delivery_status("en route")
                package.set_pickup_time(time)
                
        else:
            print(self.truck, " is not on the hub")
            
        
                
        
    
    #method to deliver the packages, it has 3 parameters, the HashMap which is where we store the packages, clock to track the time and miles to add miles to add the miles it takes to get to point a to b to totalMileage
    ##Time Complexity: O(n) + O(1) + O(n) + O(n)*O(1) + O(n)*O(1) + O(logN) = n + 1 + n + n + logn = 3n + 1 + logn = n
    def give_delivery(self,HashMap, location, clock, miles):
        
        ref = [x for x in self.packages if x.get_delivery_address() == location]
        self.totalMileage += miles
        
        
        for val in self.packages:
            if val is not None:
                if val.get_delivery_address() == location:
                    print("Package ID: ", val.get_packageID(), " has been delivered to ", val.get_delivery_address(), " by truck ", self.truck, " and driver ", self.driver, " and recieved at ", HashMap.transform_hour(clock), " Deliveryb Deadline: ", val.get_delivery_deadline())
                    
        
        
        for val in ref:
            HashMap.update_package_status(val.get_packageID(), clock)
        
        
        self.packages[:] = [x for x in self.packages if x.get_delivery_address() != location]
        
        
        
    ##set the truck's location to the hub's location
    #Time complexity: O(1)
    #Space Complexity: O(1) 
    def get_back_to_hub(self):
        self.location = "4001 S 700 E"
    
    #Get Truck's location
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def get_location(self):
        return self.location
    
    
    
    #Get Truck's Packages
    #Time complexity: O(1)
    #Space Complexity: O(1)
    def get_truck_packages(self):
        return self.packages
    
    #Get Truck's mileage
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def get_mileage(self):
        return self.totalMileage
                
    #Set Truck's location
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def set_location(self, location):
        self.location = location
        
    
        
    
         