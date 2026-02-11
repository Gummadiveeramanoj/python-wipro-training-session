import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o', linestyle='--')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Chart")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o', linestyle='--')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Chart")
plt.grid(True)
plt.show()
names = ["A", "B", "C"]
scores = [80, 90, 100]
plt.bar(names, scores)
plt.title("Student Scores")
plt.show()
plt.barh(names, scores)
plt.show()
plt.scatter(x, y)
plt.show()
marks = [50, 60, 80, 70, 77, 86]
plt.hist(marks, bins=5)
plt.title("Marks")
plt.show()

labels = ["Chrome", "Firfox", "Edge"]
sizes = [60, 25, 15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Browser usage")
plt.show()



