class Animal:
    def speak(self):
        print("Animal makes sound")

class dog(Animal):
    def bark(self):
        print("Dog bark")

d=dog()
d.speak()
d.bark()