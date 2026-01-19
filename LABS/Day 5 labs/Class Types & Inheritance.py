#Create a base class Vehicle with a method start()
class Vehicle:
    # Class variable
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")

#Create a derived class Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self):
        super().__init__()   # Call parent constructor

    def drive(self):
        print("Car is being driven")

#Add a class variable to track the number of vehicles created
class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def charge(self):
        print("Electric car is charging")

#Demonstrate single inheritance and multilevel inheritance with appropriate classes
# Creating objects
v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Calling methods
v1.start()        # From Vehicle
c1.start()        # Inherited from Vehicle
c1.drive()        # From Car
e1.start()        # From Vehicle
e1.drive()        # From Car
e1.charge()       # From ElectricCar

# Display total vehicles created
print("Total vehicles created:", Vehicle.vehicle_count)

