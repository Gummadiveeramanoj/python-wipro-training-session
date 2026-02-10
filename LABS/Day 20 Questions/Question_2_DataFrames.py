import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)
print(df)


it_employees = df[df["Department"] == "IT"]
print(it_employees)

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

df["Salary_Adjusted"] = df["Salary"] * 1.10
print(df)

