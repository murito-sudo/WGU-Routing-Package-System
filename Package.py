##Here's our package class, we store packages as objects here, we have a constructor,getters and setters that we use to update, retrieve and create new objects
##Time complexity: all of it's methods are O(1)
class Package:
    def __init__(self, packageID, deliveryAddress, deliveryDeadline, deliveryCity, deliveryZip,packageWeight,
            deliveryStatus):
        self.packageID = packageID
        self.deliveryAddress = deliveryAddress
        self.deliveryDeadline= deliveryDeadline
        self.deliveryCity = deliveryCity
        self.deliveryZip = deliveryZip
        self.packageWeight = packageWeight
        self.deliveryStatus = deliveryStatus
        self.deliveryTime = None
        self.pickupTime = None
        
      
    def get_packageID(self):
        return self.packageID
    def get_delivery_address(self):
        return self.deliveryAddress
    def get_delivery_deadline(self):
        return self.deliveryDeadline
    def get_delivery_city(self):
        return self.deliveryCity
    def get_delivery_zip(self):
        return self.deliveryZip
    def get_package_weight(self):
        return self.packageWeight
    def get_delivery_status(self):
        return self.deliveryStatus
    def get_state(self):
        return self.state
    def get_delivery_time(self):
        return self.deliveryTime
    def get_pickup_time(self):
        return self.pickupTime
    
    
    def set_delivery_status(self, status):
        self.deliveryStatus = status
    def set_delivery_time(self, time):
        self.deliveryTime = time
    def set_delivery_address(self, address):
        self.deliveryAddress = address
    def set_pickup_time(self, time):
        self.pickupTime = time
    