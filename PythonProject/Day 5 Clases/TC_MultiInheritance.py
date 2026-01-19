class B:
    def showB(self):
        print("B")

    def showA(self):
        print("A from class B ")

class C(B,A):
    pass

c=C();
c.showA()
c.showB()