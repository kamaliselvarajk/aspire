import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")

mycursor = conn.cursor()

sql = "SHOW DATABASES"

mycursor.execute(sql)

for i in mycursor:
    print(i)

mycursor.close()
conn.close()
