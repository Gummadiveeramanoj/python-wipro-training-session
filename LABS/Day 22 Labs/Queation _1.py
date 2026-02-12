# ================== IMPORTS ==================

import mysql.connector
from pymongo import MongoClient


# ================== MYSQL OPERATIONS ==================

def mysql_operations():
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",          # 🔴 CHANGE THIS
            password="root123",   # 🔴 CHANGE THIS
            database="company_db"
        )

        cursor = conn.cursor()
        print("\n--- MySQL Operations ---")

        # 1. Fetch employees with salary > 50000
        print("\nEmployees with salary > 50000:")
        cursor.execute("SELECT * FROM employees WHERE salary > %s", (50000,))
        for row in cursor.fetchall():
            print(row)

        # 2. Insert a new employee
        cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
            ("Rahul", "IT", 60000)
        )
        conn.commit()
        print("\nInserted new employee into MySQL")

        # 3. Update salary by 10% for employee with id = 1
        cursor.execute(
            "UPDATE employees SET salary = salary * 1.10 WHERE id = %s",
            (1,)
        )
        conn.commit()
        print("Updated salary by 10%")

    except mysql.connector.Error as err:
        print("MySQL Error:", err)

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed")


# ================== MONGODB OPERATIONS ==================

def mongodb_operations():
    client = None

    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["company_db"]
        collection = db["employees"]

        print("\n--- MongoDB Operations ---")

        # 1. Insert new employee document
        employee = {
            "name": "Anita",
            "department": "IT",
            "salary": 70000
        }
        collection.insert_one(employee)
        print("\nInserted new employee into MongoDB")

        # 2. Find all IT department employees
        print("\nEmployees in IT Department:")
        for emp in collection.find({"department": "IT"}):
            print(emp)

        # 3. Update salary of employee by name
        collection.update_one(
            {"name": "Anita"},
            {"$set": {"salary": 75000}}
        )
        print("\nUpdated salary for Anita")

    except Exception as e:
        print("MongoDB Error:", e)

    finally:
        if client:
            client.close()
            print("MongoDB connection closed")


# ================== MAIN ==================

if __name__ == "__main__":
    mysql_operations()
    mongodb_operations()
