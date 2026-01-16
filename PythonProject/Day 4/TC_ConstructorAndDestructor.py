class employee:
    def __init__(self,name):
        self.name = name
        print("constructor is called")
    def __del__(self):
        print("destructor is called")
e=employee("James")