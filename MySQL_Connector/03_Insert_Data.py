import mysql.connector as c

conn = c.connect(host='localhost', user='root', passwd='', db='test')

if conn.is_connected():
    print("Connected")

crsr = conn.cursor()

sql = "insert into student (id, Name, City) values('Vision', 'Idar', 'India') "
crsr.execute(sql)
conn.commit()
print(crsr.rowcount, "record inserted.")
