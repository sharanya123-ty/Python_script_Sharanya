class Car:
    brand = "suzuki"  

    def __init__(self, carname, carprice):
        self.carname = carname  
        self.carprice = carprice 

    def breakingSys(self):
        print("Break Applied.. :)")

Car1=Car("swift", "8lakhrs")
print(Car1.carname) 
print(Car1.carprice)
print(Car1.brand)  
Car1.breakingSys()
