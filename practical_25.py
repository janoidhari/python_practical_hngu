# 25. Write a Python program for search record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Servel and create "bca" database.
- Create users Table and add dummy data.

"""

import mysql.connector
print("")
mydb = mysql.connector.connect(
    host='localhost', database='growmore', user='root', password='')

mycursor = mydb.cursor()
sql = "SELECT * FROM students WHERE name ='hitesh'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
