##Simulation class, we use it to simulate the trip
##all methods other than start_trip are O(1)

import time
class Simulation:
    
    def __init__(self):
        self.depa = 0
        self.time = 0
        
        
    #here's our simulation method when we deploy our trucks
    #Time Complexity:  O(n^2)
    #Space Complexity: O(n^2) 
    def start_trip(self, truck, hashing, graph, depaTime, clock):
        y = 0
        miles = 0
        
        
        ##we won't get back to the hub until we delivered all of the packages in that trip
        print(truck.truck, " is deployed")
        while len(truck.get_truck_packages()) > 0:
        
           
            loc = graph.next_route(y)
            truck.set_location(loc.get_next())
            truck.give_delivery(hashing, loc.get_curr(), clock, loc.get_miles())
            clock = int(clock + ((loc.get_miles() / 18) * 60))
            
                
            miles = miles + loc.get_miles()
            
            
            ##Notification to upate the address of Package ID #9
            if clock >= 620 and hashing.get_package("9").get_delivery_address() != "410 S State St":
                print("WGUPS know the proper address for package #9")
                print("Would you like to change the address? Please type 'y'")
                vali = input()
                if vali.lower() == "y":
                    hashing.update_wrong_address("9")
                    print("Package #9 address has been corrected")
               
                    
                    
            y=y+1
            time.sleep(0.5)
           
                
                    
                     
                
        y=0
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("all packages delivered and returning to the hub")
        back = graph.cut_to_hub(truck.get_location())
        clock = clock + ((back / 18) * 60)
        miles += back
        truck.get_back_to_hub() 
        print("Departure Time for this Truck: ", hashing.transform_hour(depaTime))
        print("Time of arrival: ", hashing.transform_hour(clock))
        print("total miles: ", miles)
        depaTime = clock
        self.depa = depaTime
        self.time = clock
        print("----------------------------------------------------------------------------------------------------------------------------------")
       
        return miles
    
    
    
    def get_depa(self):
        return self.depa
    def get_time(self):
        return self.time