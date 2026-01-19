#Custom Iterator (1 to N)
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# using the iterator
obj = NumberIterator(5)
for num in obj:
    print(num)

#Generator – First N Fibonacci Numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# using the generator
for value in fibonacci(5):
    print(value)

#Difference Demonstration (For Loop)
print("Iterator Output:")
for i in NumberIterator(3):
    print(i)

print("Generator Output:")
for j in fibonacci(3):
    print(j)

#Descriptors
#Salary Descriptor with Validation
class Salary:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be positive")
        instance._salary = value


class Employee:
    salary = Salary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# testing descriptor
emp1 = Employee("Ravi", 30000)
emp2 = Employee("Anita", 45000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# emp3 = Employee("John", -5000)  # this will raise ValueError

#Decorators
#Execution Time Decorator
import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Function:", func.__name__)
        print("Execution Time:", end - start, "seconds")
    return wrapper


@execution_time
def sample_task():
    total = 0
    for i in range(1000000):
        total += i


sample_task()
