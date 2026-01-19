class box1:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


b1 = box1(50)
b2 = box1(30)
b3 = box1(10)
result = b1 + b3
print(result)



