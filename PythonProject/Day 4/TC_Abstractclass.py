from abc import ABC,abstractmethod

class shape(ABC):
    def display(self):
        print("normal method")
    @abstractmethod
    def area(self):
        pass


class reactangle(shape):
    def area(self):
        print("area method implemented")


r=reactangle()
r.area()
r.display()
