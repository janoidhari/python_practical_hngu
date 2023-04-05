# 23. Write a Python program for connection with my Sql and display all record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Server and create "bca" database.
- Create users Table and add dummy data.
"""
import mysql.connector
print("")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = '',
    database = "growmore"
)
mycursor = mydb.cursor()

# sql = "SELECT * FROM students"

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
