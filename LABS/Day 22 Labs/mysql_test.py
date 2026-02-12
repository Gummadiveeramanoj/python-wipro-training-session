import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="company_db"
    )
    print("MySQL Connected Successfully")
    conn.close()

except mysql.connector.Error as e:
    print("Error:", e)
