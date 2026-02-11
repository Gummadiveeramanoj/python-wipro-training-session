import matplotlib.pyplot as plt

#data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.figure(figsize=(8, 5))
sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Distribution")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()
