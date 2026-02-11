import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("plot1")
plt.subplot(1, 2, 2)
plt.bar(["a", "b", "c"], [3, 5, 7])
plt.title("plot2")
plt.show()
plt.savefig("report.png")
