from product.product import *
from pprint import pprint
#from admin.sample_cls import *
from database import db
from customer.carts_payments import *
from customer.payment import *

#obj = ProductClass(a)
cartobj = Cart([])
paymentobj = Payment()
#obj.view_product()
db.init()
db.view_product()

def action():
    x = int(input('''Choose the below one:
            1)Admin
            2)Customer
            3)Go Back
            Enter your choise: 
'''))

    if x == 1:
        if(input('Enter the admin password: ') == 'admin'):
            admin()
        else:
            print('Invalid credentials!')
            action()
    if x == 2:
        customer()
    if x == 3:
        action()
def admin():
    y = int(input('''Choose your option
               1)Add product
               2)Delete product
               3)Go Back
               Enter your option: 
''')) 
    if (y == 1):
        print('1)Washing_machine\n 2)Mobile\n 3)TV')
        z = input('Choose the category: ')
        if(z == '1'):
            #pprint(obj.add_product('washing_machine'), width = 100)
            add_product()   
        if(z == '2'):
            #pprint(obj.add_product('mobile'), width = 100)
            add_product()   
        if(z == '3'):
            #pprint(obj.add_product('tv'), width = 100)
            add_product()
            
        admin()

            
    if(y == 2):
        print('List of products')
        #obj.view_product()
        view_product()
        m = input('Enter the id of the item that you want to delete: ')
        print('Updated List: ')
        delete_product()
        #pprint(obj.delete_product(m), width = 100)
        admin()
        
    if(y == 3):
        action()

def payment():
    option = int(input('''Enter the payment options:
1)Credit/Debit card\n 2)Netbanking\n 3)Wallets\n 4)COD\n 5)Go back
'''))
    if(option == 1):
        cd = Card()
        cd.initiate()
        cartobj.clear_cart()
        payment()
        
    if(option == 2):
        nb = NetBanking() 
        nb.initiate()
        cartobj.clear_cart()
        payment()
        
    if(option == 3):
        ip = int(input('''Choose wallet options
1)GPay\n 2)PhonePay\n 3)Paytm
'''))
        if(ip == 1):
            ip = 'GPay'
        if(ip == 2):
            ip = 'PhonePay'
        if(ip == 3):
            ip = 'Paytm'

        wt = Wallet(ip)
        wt.initiate()
        cartobj.clear_cart()
        customer()
        
    if(option == 4):
        cod = Cod()
        cod.initiate()
        cartobj.clear_cart()
        customer()
        
    if(option == 5):
        action()

def formatDisplay(filtered):
    for i in filtered:
        for x, y in (i.items()):
            if(type(y) == dict):
                for x, y in (y.items()):
                    print(f'{x.capitalize()}: {y.capitalize()}')
            else:
                if(x == 'id'):
                    continue
                print(f'{x.capitalize()}: {y.capitalize()}')

                
        
def view_items(item):
    cat = list(filter(lambda x: x['category'] == item, a))
    pprint(cat)

    def fun():
        option = int(input('''Choose your option:
     \t1)Add to cart\n\t 2)View cart\n\t 3)Delete from cart\n\t 4)Payment\n\t 5)Go back
'''))
        if(option == 1):
            name = input("Enter the name: ")
            for item in cat:
                if(name == item['name']):
                    cartobj.add(item)
                    print('Added successfully')
                    customer()
                
        if(option == 2):
            pprint(cartobj.view())
            fun()
        
        if(option == 3):
            pprint(cartobj.view())
            name = input("Enter the name of product that you want to delete: ")
            pprint(cartobj.delete(name))
            fun()
        
        if(option == 4):
            if(len(cartobj.view())>0):
                payment()
            else:
                print('Your cart is empty! Please add some products!!')
            fun()
        if(option == 5):
            customer()
    fun()

def customer():
    #obj.view_product()
    view_product()
    x = int(input('''Choose the product to buy:
            1)Washing Machine
            2)Mobile
            3)Tv
'''))
    if(x == 1):
        view_items('washing-machine')
    if(x == 2):
        view_items('mobile')
    if(x == 3):
        view_items('tv')

    
action()
