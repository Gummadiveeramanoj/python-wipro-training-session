import csv
import os

def load_users():
    users = []
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "data", "users.csv")

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)

    return users
