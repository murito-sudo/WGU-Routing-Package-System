from Package import Package
import csv

##HashTable class used to create our own hashtable without using any additional libraries
class HashTable:
    #we first create a constructor with size parameter that will determine our hash initial length
    def __init__(self, size):
        
        self.size = size
        ##here we initialize an array with all value None in all of it's indexes
        self.arr = [None for i in range(self.size)]
        
        #Here we open the WGUPS Package File which contains all the packages and it's information read it and then iterate through each row
        ##Time Complexity:
        ##file = open('WGUPS Package File.csv'): O(1)
        ##csvreader reads all the lines line by line on the csv file: O(n) Source: (https://stackoverflow.com/questions/63098337/what-is-the-time-complexity-of-csv-reader-in-python)
        ##the for loop reads the lines from csv reader line by line and then add it to the hash: O(n)
        ##The add() method has a best time complexity of O(1) and worst time complexity of O(n)
        ##Final Time complexity: Best Case: O(1) + O(n) + O(n)*O(1) = 2 + 2n = n
        ##Final Time Complexity: Worst Case: O(1) + O(n) + O(n)*O(n) = 1 + n + n^2 = n^2
        file = open('WGUPS Package File.csv')
        type (file)
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        x=0
        for row in csvreader:
            if x >= 7:
              
                self.add(row[0], row[1], row[5].split(" ")[0], row[2], row[4], row[6], "at the hub")
                
            
            x=x+1
            
                  
                
    #Here we return the hashtable 
    #Final Time complexity O(1)
    def get_list_package(self):
        return self.arr 
    
    ##here we get the hash of some key
    ##We first create a hash variable and then we assign it to 0
    ##We iterate through the characters of the key and then we get the ASCII Value of each character of the key
    #every ASCII Value we get, let's sum that ASCII Value + the hash variable
    #after we complete our loop iteration we return the modulo of hash % self.size, that way we can point to a direction without going through the whole list
    #Final Time complexity: O(1)
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash+= ord(char)
        return hash % self.size
    
      
    ##package lookup with the PackageID as it's parameter
    ##We start by looking our hash, we get our hash and retrieve it in the hash variable
    ##We then check if the value is None if it is then we will return None, if not then we will iterate through the values of that cell
    ##We then check if the key is equal to the key of the hashtable iteration, if we find the match we return that package
    ##Final Time Complexity: Best Case: if we don't have collision in our hashtable then this algorithm will have a O(n) of O(1)
    ##Final Time Complexity: Worst Case: if we do have collision, we will have to loop through the values of that cell, if we only have one cell, then the Time complexity is O(n)
    #Final Time Complexity: Average Case: if we do have collision, but we store all of our values in multiple cells, we will only check some values of the hashtable, making the Time complexity O(logN)
    def get_package(self, key):
        hash = self.get_hash(key)
        if self.arr[hash] is not None:
            for val in self.arr[hash]:
                if key == val[0]:
                    return val[1]
        return None
    
    
    #Method to retrieve the information of all the packges at certain time
    #Time Complexity: O(nlogn)
    #Space Complexity: O(n^2)
    def get_all_packages(self, clockTracker, truck1, truck2, truck3):
        ref = []
        for val in self.arr:
            if val is not None:
                for t in val:
                    if t is not None:
                        ref.append(t[1])
        
        
        ref.sort(key=lambda x : int(x.get_packageID()))
        
        
       
        for res in ref:
            
            status = self.convert_status(res, clockTracker)
            if status == "delivered":
                print("Package ID:", res.get_packageID(), ",Package Address:", 
                res.get_delivery_address(), ",City:", res.get_delivery_city(), 
                ",Zip:", res.get_delivery_zip(), ",Weight:", res.get_package_weight(),
                ",Delivery Deadline:", res.get_delivery_deadline(), 
                ",Pickup Time:", self.transform_hour(res.get_pickup_time()),
                ",Delivery Status:", status, ",Delivered at:", self.transform_hour(res.get_delivery_time()))
            elif status == "en route":
                print("Package ID:", res.get_packageID(), ",Package Address:", 
                res.get_delivery_address(), ",City: ", res.get_delivery_city(), 
                ",Zip: ", res.get_delivery_zip(), ",Weight:", res.get_package_weight(),
                ",Delivery Deadline:", res.get_delivery_deadline(), ",Pickup Time:"
                , self.transform_hour(res.get_pickup_time()),
                ",Delivery Status:", status)
            elif status == "at the hub":
                print("Package ID:", res.get_packageID(), ",Package Address:", 
                res.get_delivery_address(), ",City: ", res.get_delivery_city(), 
                ",Zip:", res.get_delivery_zip(), ",Weight:", res.get_package_weight(),
                ",Delivery Deadline:", res.get_delivery_deadline(),",Delivery Status:", status)
                        
        print("-----------------------------------------------------------------------------------------------")
        print("Total mileage of: ", truck1.truck, ": ", truck1.get_mileage())
        print("Total mileage of: ", truck2.truck, ": ", truck2.get_mileage())
        print("Total mileage of: ", truck3.truck, ": ", truck3.get_mileage())
                    
                
                
    
    ##Here we made a lookup function by package address on the hash
    ##Time Complexity: O(nlogn)
    ##Space complexity: O(n^2)
    def get_package_by_address(self, address, clockTracker):
        print("                        -------------------------------------", address, "-------------------------------------")
        
        for val in self.arr:
            if val is not None:
                for res in val:
                    if res[1].get_delivery_address() == address:
                        status = self.convert_status(res[1], clockTracker)
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
                        
    ##Here we made a lookup function by package deadline on the hash
    ##Time Complexity: O(n)
    ##Space complexity: O(n)        
    def get_package_by_deadline(self, deadline, clockTracker):
        print("                        -------------------------------------", deadline, "-------------------------------------")
        
        for val in self.arr:
            if val is not None:
                for res in val:
                    if res[1].get_delivery_deadline() == deadline:
                        status = self.convert_status(res[1], clockTracker)
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
                        
                        
                        
    ##Here we made a lookup function by package city on the hash
    ##Time Complexity: O(n)
    ##Space complexity: O(n)        
    def get_package_by_city(self, city, clockTracker):
        print("                        -------------------------------------", city, "-------------------------------------")
        for val in self.arr:
            if val is not None:
                for res in val:
                    if res[1].get_delivery_city() == city:
                        status = self.convert_status(res[1], clockTracker)
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
                        
                        
    ##Here we made a lookup function by package zip on the hash
    ##Time Complexity: O(n)
    ##Space complexity: O(n)           
    def get_package_by_zip(self, zip, clockTracker):
        print("                        -------------------------------------", zip, "-------------------------------------")
        for val in self.arr:
            if val is not None:
                for res in val:
                    if res[1].get_delivery_zip() == zip:
                        status = self.convert_status(res[1], clockTracker)
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
           
           
    ##Here we made a lookup function by package weight on the hash
    ##Time Complexity: O(n)
    ##Space complexity: O(n)                  
    def get_package_by_weight(self, weight, clockTracker):
        print("                        -------------------------------------", weight, "-------------------------------------")
        for val in self.arr:
            if val is not None:
                for res in val:
                    if res[1].get_package_weight() == weight:
                        status = self.convert_status(res[1], clockTracker)
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
                        
                        
                        
    ##Here we made a lookup function by package status on the hash
    ##Time Complexity: O(n)
    ##Space complexity: O(n)
    def get_package_by_status(self, stat, clockTracker):
        print("                        -------------------------------------", stat, "-------------------------------------")
        for val in self.arr:
            if val is not None:
                for res in val:
                    status = self.convert_status(res[1], clockTracker)
                    if stat == status:
                    
                        print("-------------------------------------------------------------------")
                        print("Package ID: ", res[1].get_packageID())
                        print("Package Address: ", res[1].get_delivery_address())
                        print("Delivery Deadline: ", res[1].get_delivery_deadline())
                        print("City: ", res[1].get_delivery_city())
                        print("Zip: ", res[1].get_delivery_zip())
                        print("Weight: ", res[1].get_package_weight())
                        print("Status: ", status)
                        if status == "delivered":
                            print("Delivery Time: ", self.transform_hour(res[1].get_delivery_time()))
                        print("---------------------------------------------------------------------")
                        
                        
                        
    
    
    
    
    
    
    
    

            
    
    
    
    #Here we add the values of all the deliveries, our key is the DeliveryPackageID, since that
    #value must be unique and a key must be unique
    ##Time complexity: Best Case: O(1) + O(1) + O(1) + O(1) + O(n) = O(n)
    
    def add(self, key, deliveryAddress, deliveryDeadline, deliveryCity, deliveryZip,packageWeight,
            deliveryStatus):
        hash = self.get_hash(key)
        res = [key, Package(key, deliveryAddress, deliveryDeadline, deliveryCity, deliveryZip, packageWeight, "at the hub")]
       
                
        if self.arr[hash] == None:
            self.arr[hash] = list([res])
        else:
            for val in self.arr[hash]:
                if key == val[0]:
                    print("No duplicate keys")
                    return True
                
            self.arr[hash].append(res)
        
        self.update_route_address(key, self.arr[hash])
            
            
            
            
    ##Here we updata the address of each package so it maches with the addresses on the Distance Table
    ##We loop through the whole array and then we update the values
    ##Time Complexity: O(Logn) for the loop and O(n) for the replace method = O(Logn)*O(n) = O(NLogN)
    ##If we don't have collision then the time complexity will be O(n)
    ##Space Complexity: O(n)  
    def update_route_address(self, key, array):
        for val in array:
            if key == val[0]:
                val[1].set_delivery_address(val[1].get_delivery_address().replace("South", "S"))
                val[1].set_delivery_address(val[1].get_delivery_address().replace("North", "N"))
                val[1].set_delivery_address(val[1].get_delivery_address().replace("East", "E"))
                val[1].set_delivery_address(val[1].get_delivery_address().replace("West", "W"))
                val[1].set_delivery_address(val[1].get_delivery_address().replace("Station", "Sta"))
                break
            
    
    
    #In this function we change the wrong address of the package ID "9"
    #First we will get our hash
    #Second we will iterate through hash cell
    #Third if we find the packageID number 9 we will set the delivery address to the new address
    #Final Time Complexity: if we don't have any collision on that cell, the Time complexity of the Algorithm is O(1)
    #Final Time Complexity: Worst Case: if we do have collision, and we only have one cell, the Time complexity of the algorithm is O(n)
    #Final Time Complexity: Average Case: if we do have collision, but we have our values in multiple cells, the Time complexity of the algorithm is O(logN)
    def update_wrong_address(self, key):
        hash = self.get_hash(key)
        for val in self.arr[hash]:
            if val[1].get_packageID() == "9":
                val[1].set_delivery_address("410 S State St")
                break
                
            
            
    #here we update our package status when a package is being delivered
    #we have 2 parameters, first one is key which is the key of the package we want to update
    #second one is clock, it is the current hour, we use it to store when that package was delivered
    #First we find our hash with the get_hash() function, then we loop through all the values on that cell
    #if we find the key, we will modify the status of the package with the .set_delivery_status() method on the package class, then we add the time of the delivery on .set_delivery_time()
    #Final Time Complexity: if we don't have any collision on that cell, the Time complexity of the Algorithm is O(1)
    #Final Time Complexity: Worst Case: if we do have collision, and we only have one cell, the Time complexity of the algorithm is O(n)
    #Final Time Complexity: Average Case: if we do have collision, but we have our values in multiple cells, the Time complexity of the algorithm is O(logN)
    def update_package_status(self, key, clock):
        hash = self.get_hash(key)
        for val in self.arr[hash]:
            if val[0] == key:
                val[1].set_delivery_status("delivered")
                val[1].set_delivery_time(clock)
             
                
            
    
            
    ##here we transform our time(which is stored as an int) to a string to have the HH:MM format and then we return the final result
    ##Time complexity of the code is O(1)
    ##Space complexity is O(1) 
    def transform_hour(self, time):
        hour = time / 60
        minute = time - (int(hour)*60)
        res = 0
        if minute == 0:
            res = str(int(hour)) + ":" + str(int(minute)) + "0"
        elif minute <= 9:
            res= str(int(hour)) + ":" + "0" + str(int(minute))
        else:
            res= str(int(hour)) + ":" + str(int(minute))
            
    
            
        
        return res
    
    ##Here we do the opposite of transform_hour() we convert an hour in a HH:MM format to an int
    ##Time Complexity: O(n) + O(1) + O(1) + O(1) = n + 3 = n
    ##Space Complexity:O(n)
    def transform_hour_to_string(self, hour):
        try:
            ref = hour.split(":")
            num1 = int(ref[0])*60
            num2 = int(ref[1])
            
            if int(ref[1]) >= 60 or int(ref[0]) > 24 or int(ref[1]) < 0 or int(ref[0]) < 0:
                print("Invalid format")
                return -1
            
            return num1+num2
            
            
        except:
            print("invalid format")
            return -1
        
        
    
    ##here we compare an hour and a package deliverya and pickup time, based on the result we will know if the package was delivered, at the hub or en route at that moment
    ##Time Complexity: O(1)
    ##Space Complexity: O(1)
    def convert_status(self, package, hour):
            pickup = package.get_pickup_time()
            delivery = package.get_delivery_time()
       
            
            if pickup > hour:
                return "at the hub"
            else:
                if delivery > hour:
                    return "en route"
                else:
                    return "delivered"
            
            
   
    
    
        
