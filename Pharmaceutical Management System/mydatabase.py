import sys
import mysql.connector

try:
    db = mysql.connector.connect(
        host="192.168.205.113",
        user="aurora",
        password="1234@Aurora",
        database="pharmacy"
    )
    mycursor = db.cursor()
except mysql.connector.Error as e:
    print(f"Error connecting to database: {e}")
    sys.exit()