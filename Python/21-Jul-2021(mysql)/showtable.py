import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")

mycursor = conn.cursor()

sql = "SHOW TABLES"

mycursor.execute(sql)

for i in mycursor:
    print(i)
    
mycursor.close()
conn.close()
