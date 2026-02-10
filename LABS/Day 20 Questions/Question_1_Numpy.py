students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]
import pandas as pd
import numpy as np

df_students = pd.DataFrame(students)
print(df_students)

scores = df_students["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_score)

df_students["above_average"] = df_students["score"] > mean_score

print(df_students)
