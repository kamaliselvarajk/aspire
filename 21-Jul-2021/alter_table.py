import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")

mycursor = conn.cursor()

sql = "ALTER TABLE sampletable ADD COLUMN sNo INT AUTO_INCREMENT"

mycursor.execute(sql)

mycursor.close()
conn.close()
