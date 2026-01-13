numbers=[10,20,30,40,50]
names=["mam","manoj","jashu"]
mixed=[1,"python",3.5,True]

print(numbers)
print(names)
print(mixed)

numbers=[10,20,30,40,50]
names=["mam","manoj","jashu"]
mixed=[1,"python",3.5,True]

numbers[1]=100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)

if 10 in numbers:
    print("Found")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

names.reverse()
print(names)
names.append("dolly")
print(names)

names.extend(["dolly","chitti"])
print(names)

names.remove("mam")
print(names)

names.insert(0,"manoj")
print(names)