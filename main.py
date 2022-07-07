#Name: Luis
#Last Name: Pichardo
#Student ID: 010039420
from HashTable import HashTable
from Truck import Truck
from Graph import Graph
from Simulation import Simulation




#Here we created an instance for our own implemented Hashmap, with an initial size of 40
HashMap = HashTable(40)


## Here we create the instances and call the methods of the graph class
Adjacency = Graph(27)
Adjacency.sort_graph()
Adjacency.optimize_path()



#Variable for the results Menu   
clockTracker = 0     
        
#Variables we use to store the time of the trucks trip
clockTruck1 = 545
clockTruck2 = 480
clockTruck3 = 480

#variables we use to store the departure time of the trucks
depaT1 = clockTruck1
depaT2 = clockTruck2
depaT3 = clockTruck3



#total miles of all trucks milesTruck1 + milesTruck2 + milesTruck3
totalMiles = 0


            
#Instances of the Truck class      
Truck1 = Truck("Pajita Tox", "Truck 1")
Truck2 = Truck("Punti Jordan", "Truck 2")
Truck3 = Truck("", "Truck 3")


##Instance for our truck simulation
S = Simulation()


    


     
print("Welcome to WGUPS, What would you like to do?")
print("Press 1 to begin delivery simulation")
print("Press 2 to quit the program")
x = input()
if x == "1":
   
        
    #Loading packages to Truck 1
    Truck1.add(HashMap.get_package("4"), clockTruck1)
    Truck1.add(HashMap.get_package("6"), clockTruck1)
    Truck1.add(HashMap.get_package("12"), clockTruck1)
    Truck1.add(HashMap.get_package("21"), clockTruck1)
    Truck1.add(HashMap.get_package("22"), clockTruck1)
    Truck1.add(HashMap.get_package("31"), clockTruck1)
    Truck1.add(HashMap.get_package("40"), clockTruck1)
    Truck1.add(HashMap.get_package("32"), clockTruck1)
    Truck1.add(HashMap.get_package("24"), clockTruck1)
    Truck1.add(HashMap.get_package("25"), clockTruck1)
    Truck1.add(HashMap.get_package("34"), clockTruck1)
    Truck1.add(HashMap.get_package("26"), clockTruck1)
    Truck1.add(HashMap.get_package("17"), clockTruck1)
  
    print("------------------------------------------")
              
    #Loading packages to truck 2         
    Truck2.add(HashMap.get_package("13"), clockTruck2)
    Truck2.add(HashMap.get_package("39"), clockTruck2)
    Truck2.add(HashMap.get_package("3"), clockTruck2)
    Truck2.add(HashMap.get_package("5"), clockTruck2)
    Truck2.add(HashMap.get_package("37"), clockTruck2)
    Truck2.add(HashMap.get_package("38"), clockTruck2)
    Truck2.add(HashMap.get_package("14"), clockTruck2)
    Truck2.add(HashMap.get_package("15"), clockTruck2)
    Truck2.add(HashMap.get_package("16"), clockTruck2)
    Truck2.add(HashMap.get_package("19"), clockTruck2)
    Truck2.add(HashMap.get_package("20"), clockTruck2)
    Truck2.add(HashMap.get_package("10"), clockTruck2)
    Truck2.add(HashMap.get_package("29"), clockTruck2)
    Truck2.add(HashMap.get_package("30"), clockTruck2)
    Truck2.add(HashMap.get_package("33"), clockTruck2)
    Truck2.add(HashMap.get_package("1"), clockTruck2)
    
    print("----------------------------------------------")
    
    print("--------------Beginning Truck Simulation--------------")
    ## here we call the method start_trip which returns the total round trip miles from the hub and sum the return value to totalMiles
    totalMiles += S.start_trip(Truck2, HashMap, Adjacency, depaT2, clockTruck2)
    ##Here we call a method  in Simulation to get the saved departure time on the class and assign it to the proper variable
    depaT2 = S.get_depa()
    ##Here we call a method in Simulation to get the saved hour and assign it to the proper variable
    clockTruck2 = S.get_time()
       
       
    #Loading Packages to Truck 2
    Truck2.add(HashMap.get_package("2"), clockTruck2)
    Truck2.add(HashMap.get_package("7"), clockTruck2)
    Truck2.add(HashMap.get_package("36"), clockTruck2)
    Truck2.add(HashMap.get_package("8"), clockTruck2)
    Truck2.add(HashMap.get_package("35"), clockTruck2)
    Truck2.add(HashMap.get_package("27"), clockTruck2)
    Truck2.add(HashMap.get_package("18"), clockTruck2)
    Truck2.add(HashMap.get_package("23"), clockTruck2)
    Truck2.add(HashMap.get_package("11"), clockTruck2)
    Truck2.add(HashMap.get_package("9"), clockTruck2)
    Truck2.add(HashMap.get_package("28"), clockTruck2)
    
    totalMiles += S.start_trip(Truck1, HashMap, Adjacency, depaT1, clockTruck1)
    depaT21 = S.get_depa()
    clockTruck1 = S.get_time()
    
    totalMiles += S.start_trip(Truck2, HashMap, Adjacency, depaT2, clockTruck2)
    depaT2 = S.get_depa()
    clockTruck2 = S.get_time()
    
    print("------------------------------------------------")    
    print("------------------------------------------------")



    print("                                   ------Total Miles For All Trucks------                             ")
    print("                                           ", totalMiles)    
    
    print()
 
  
    
    print("-------------------------------Ending of the Truck simulator-------------------------------")
    
    print()
    print()
    print("--------------------------------------------------------------Results Menu--------------------------------------------------------------")
    print("Would you like to track packages at certain time? if yes type the desired hour of format HH:MM, if not type 'n'")
    
    x = input()
    if x != 'n':
        
        clockTracker = HashMap.transform_hour_to_string(x)
        print("Packages status at: ", HashMap.transform_hour(clockTracker))
        HashMap.get_all_packages(clockTracker, Truck1, Truck2, Truck3)
        input("Press Enter to continue...")
        if clockTracker == -1:
            quit()
            
        print("current hour", HashMap.transform_hour(clockTracker))
        print("        1.Look Packages by ID")
        print("        2.Look Packages by address")
        print("        3.Look Packages by deadline")
        print("        4.Look Packages by city")
        print("        5.Look Packages by zip code")
        print("        6.Look Packages by weight")
        print("        7.Look Packages by status")
        print("        8.Retrieve total mileage")
        print("        9.Exit application")
        while x != "9":
            print("What would you like to do?")
           
            x = input()
            
            if x == "1":
                print("Type the desire ID ")
                z = input()
                res = HashMap.get_package(z)
                if res is not None:
                    status = HashMap.convert_status(res, clockTracker)
                    print("---------------------------------------------------------------------")
                    print("Package ID: ", res.get_packageID())
                    print("Package Address: ", res.get_delivery_address())
                    print("Delivery Deadline: ", res.get_delivery_deadline())
                    print("City: ", res.get_delivery_city())
                    print("Zip: ", res.get_delivery_zip())
                    print("Weight: ", res.get_package_weight())
                    print("Status: ", status)
                    if status == "delivered":
                        print("Delivery Time: ", HashMap.transform_hour(res.get_delivery_time()))
                    print("---------------------------------------------------------------------")
                    
                else:
                    print("     Invalid ID")
                
            elif x == "2":
                print("Type Desired Address")
                z = input()
                HashMap.get_package_by_address(z, clockTracker)
                
            elif x == "3":
                print("Type Desired Deadline")
                z = input()
                HashMap.get_package_by_deadline(z, clockTracker)
            
            elif x == "4":
                print("Type Desired City")
                z = input()
                HashMap.get_package_by_city(z, clockTracker)
            
            elif x == "5":
                print("Type Desired Zip Code")
                z = input()
                HashMap.get_package_by_zip(z, clockTracker)
                
            elif x == "6":
                print("Type Desired Weight")
                z = input()
                HashMap.get_package_by_weight(z, clockTracker)
                
            elif x == "7":
                print("Type Desired Status: (delivered,en route, at the hub)")
                z = input()
                HashMap.get_package_by_status(z, clockTracker)
                
            elif x == "8":
                print("-------------------Total Mileage---------------------")
                print("                   ", totalMiles)
                
            elif x == "9":
                print("See you Later! ")
                break
            else:
                print("choose the correct numbers from (1-8)")
        
    else:
        print("Good Bye!!")
    
        
            
elif x == "2":
    print("Application terminated successfully!")
    print("Good bye!!!!")

 