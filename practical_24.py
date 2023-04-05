# 24. Write a Python program for modified record, display record and delete record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Servel and create "bca" database.
- Create users Table and add dummy data.

"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', database='growmore', user='root', password='')

mycursor = mydb.cursor()

sql = "UPDATE students SET city = 'idar' WHERE city = 'hmt'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
sql="DELETE FROM students WHERE  id=0"
mycursor.execute(sql)

mydb.commit()

print("Rows Deleted = ",mycursor.rowcount)
mydb.close()