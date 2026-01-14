#1️ Decorator to Measure Execution Time
#execution_time → decorator function
#wrapper → runs before and after the actual function
#time.time() → records start and end time
#func.__name__ → prints function name
import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()

        print("Function Name:", func.__name__)
        print("Execution Time:", end - start, "seconds")

        return result
    return wrapper

#2️ Recursive Factorial Function
@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#3️ Function Call
num = 5
print("Factorial:", factorial(num))
