import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="sampledb")

mycursor = conn.cursor()

sql = "INSERT INTO sampletable (name, email, age, sNo) VALUES (%s, %s, %d, %d)"
value = [("Keerthi", "keerthi@gmail.com", 21, 2),
         ("Dharshini", "dharshi@gmail.com", 20, 3),
         ("Shwetha", "shwetha@gmail.com", 35, 4),
         ("Kabi", "kabi@gmail.com", 21, 5),
         ("Bhakiya", "bhakiya@gmail.com", 21, 6),
         ("Sathya", "sathya@gmail.com", 28, 7),
         ("Johncy", "johncy@gmail.com", 30, 8),
         ("Kathir", "kathir@gmail.com", 33, 9),
         ("Saravanan", "saravanan@gmail.com", 37, 10)
         ]

mycursor.execute(sql, value)
conn.commit()

mycursor.close()
conn.close()
