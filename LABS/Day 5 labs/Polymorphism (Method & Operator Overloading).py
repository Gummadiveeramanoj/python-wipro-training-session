#1. Create a class Calculator that demonstrates method overriding
class vehicle:
    count=0
    def __init__(self):
        vehicle.count+=1
    def start(self):
        print("vehicle started")
class car(vehicle):
    def drive(self):
        print("car is driving")

class ecar(car):
    def stop(self):
        print("car stopped")

c=car()
c.start()
e=ecar()
e.start()
e.stop()
print(vehicle.count)

#2. Create another class AdvancedCalculator that overrides a method from Calculator
class calculator:
    def add(self,a,b):
        print("basic add:",a+b)
class advanced_calculator(calculator):
    def add(self,a,b):
        print("advanced add:",(a+b)*2)
c1=calculator()
c2=advanced_calculator()
c1.add(23,45)
c2.add(23,45)

#3. Implement operator overloading by overloading the + operator to add two objects of a custom class
class box:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return box(self.value+ other.value)
b1=box(23)
b2=box(34)
print((b1+b2))

#4. Demonstrate polymorphism using the same method name with different behaviors
class calculator:
    def add(self, a, b):
        print("basic add:", a + b)


class advanced_calculator(calculator):
    def add(self, a, b):
        print("advanced add:", (a + b) * 2)


c1 = calculator()
c2 = advanced_calculator()
c1.add(23, 45)
c2.add(23, 45)


def operator(obj):
    print(obj.__class__.__name__)
    obj.add(23, 45)


operator(c1)
operator(c2)