import mysql.connector

conn = myql.connector.connect(host="localhost", user="root", password="")

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE sampledb")

cursor.close()
conn.close()
