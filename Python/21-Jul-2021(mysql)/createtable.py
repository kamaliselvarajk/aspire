import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")

mycursor = conn.cursor()

sql = "CREATE TABLE sampletable (name VARCHAR(100), email VARCHAR(100), age INT(3))"

mycursor.execute(sql)

mycursor.close()
conn.close()
