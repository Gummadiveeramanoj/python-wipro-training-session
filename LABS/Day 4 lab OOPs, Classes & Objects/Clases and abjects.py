#Class → Blueprint
#Object → Instance of class
#Method → Function inside class
#Constructor → Initializes object data

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("----------------")

student1 = Student("Manu", 9)
student2 = Student("Harshu", 10)

student1.display_details()
student2.display_details()

