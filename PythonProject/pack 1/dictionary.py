student={

    "name": "Praveen",
    "age": 30,
    "Course": "Python"

}
print(student)
print(student["name"])
print(student.get("age"))

student["Marks"]=100
student["age"]=30
print(student)
print(student["name"])
print(student.get("age"))
student.pop("age")
print(student)
student.popitem()
print(student)

print(student.keys())
print(student.values())


for key in student:
    print(key,student[key])

if "name" in student:
    print("key exists")

employees={

    101:{"name":"Divya","salary":95000},
102:{"name":"Divya","salary":95000},

}

print(employees[101]["name"])