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
