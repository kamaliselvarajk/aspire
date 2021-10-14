import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")

mycursor = conn.cursor()

sql = "INSERT INTO sampletable (name, email, age, sNo) VALUES ('Kamali', 'kamalishwetha@gmail.com', 21, 1)"
#value = ("Kamali S", "kamalishwetha@gmail.com", "21")

mycursor.execute(sql)
conn.commit()

mycursor.close()
conn.close()
