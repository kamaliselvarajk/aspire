import mysql.connector
from tabulate import tabulate
conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'aspire')

#mycursor = conn.cursor()

#sql = 'create database aspire'
#sql = 'create table Products(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), cost INT(10), currency VARCHAR(10), category VARCHAR(20), colour VARCHAR(20))'
#sql = 'INSERT INTO Products (name, cost, currency, category, colour) VALUES (%s, %s, %s, %s, %s)'
'''value = [("Iphone 11", 50000, "INR", "mobile", "black"),
         ("Samsung Galaxy", 45000, "INR", "mobile", "grey"),
         ("Washing Machine", 25000, "INR", "washing-machine", "blue"),
         ("Samsung TV", 40000, "INR", "tv", "black")
        ]'''
'''input_field = {
        'washing_machine': ['machine_capacity', 'machine_rpm', 'type'],
        'mobile':['ram', 'processor', 'screen_size'],
        'tv': ['issmart', 'resolution', 'screen_size'],
        'common_input' : ['id', 'name', 'cost', 'currency', 'category', 'color']
        }

def get_input(self, ip):
        comm_input = {}
        diff_input = {}
        print(ip)
        for common in self.input_field['common_input']: #miniimize
            comm_input[common] = input('Enter the {}'.format(common))

        for differ in self.input_field[ip]:
            diff_input[differ] = input('Enter the {}'.format(differ))

        comm_input.update({'product_details':diff_input})
        return comm_input'''

def add_product(input):
        name = input('Enter name: ')
        cost = input('Enter cost')
        currency = input('Enter currency')
        category = input('Enter category')
        colour = input('Enter colour')
        mycursor = conn.cursor()
        sql = 'insert into Products(name, cost, currency, category, colour) values (%s, %s, %s, %s, %s)'
        value = (name, cost, currency, category, colour)
        mycursor.execute(sql, value)
        conn.commit()

def view_product():
        mycursor = conn.cursor()
        sql = 'select * from Products'
        mycursor.execute(sql)
        res = mycursor.fetchall()
        #print(res)
        print(tabulate(res, headers=['name', 'cost', 'currency', 'category', 'colour']))

def delete_product():
        id = input('Enter id of item that you want to delete')
        mycursor = conn.cursor()
        sql = 'delete from Products where id=%s'
        value = id
        mycursor.execute(sql, value)
        conn.commit()


#mycursor.executemany(sql, value)
#conn.commit()

mycursor.close()
conn.close()
