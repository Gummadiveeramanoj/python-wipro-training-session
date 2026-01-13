# question 1
for i in range(1,21):
    print(i)

# question 2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# question 3
squared_numbers = list(map(lambda x: x * x, even_numbers))
print(squared_numbers)

# question 4
data = [1,2,3,4,5,6,7,8,9,10]

squares = [x * x for x in data]
print(squares)

# question 5
even_set = {x for x in data if x % 2 == 0}
print(even_set)

# question 6
cube_dict = {x: x ** 3 for x in data}
print(cube_dict)