import sys
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pharmacy"
    )
    mycursor = db.cursor()
except mysql.connector.Error as e:
    print(f"Error connecting to database: {e}")
    sys.exit()