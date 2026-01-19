class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(B):
    def c(self):
        print("C")
obj=C();
obj.c()
obj.b()
obj.a()