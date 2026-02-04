# 1 Custom Iterator Class (1 to N)
class MyIterator:
    def __init__(self, n):
        self.n = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.n:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


# using custom iterator
print("Using Iterator:")
for i in MyIterator(5):
    print(i)

#iterators
data = [1,2,3]
it = iter(data)
print(next(it))
print(next(it))
print(next(it))

for x in [10,20,30]:
    print(x)

class count:
    def __init__(self,limit):
        self.limit=limit
        self.count=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<=self.limit:
            val=self.count
            self.count+=1
            return val
        else:
            raise StopIteration
obj = count(10)
for num in obj:
    print(num)


# 2 ️ Generator Function (First N Fibonacci Numbers)
def fibonacci_gen(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# using generator
print("Using Generator:")
for f in fibonacci_gen(5):
    print(f)

#generators
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))

print(next(gen))

def count_up(n):
    for i in range(1,n+1):
        yield i
for val in count_up(5):
    print(val)

# 3️ Difference Demonstration (For Loop)
print("Iterator gives sequential numbers:")
for x in MyIterator(3):
    print(x)

print("Generator gives Fibonacci numbers:")
for y in fibonacci_gen(3):
    print(y)


