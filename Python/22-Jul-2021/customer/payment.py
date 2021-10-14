import configparser
import datetime
import re

config = configparser.ConfigParser()
config.read('config_ex.ini')

class Payment:
    types = {
            'Card': ['number', 'pin', 'cvv', 'expiry date', 'otp'],
            'NetBanking': ['username', 'password'],
            'Wallet' : ['upi id', 'pin'],
            'Cod': ['pwd'],
            'Type':['str', 1]
            }

    def type_validate(self, temp):
        test = dict(temp)
        flag = True
        index = 0
        for i in test.values():
            if(type(i) != type(self.types['Type'][index])):
                flag = False
                index +=1

        if(flag):
            return True
        else:
             print('Enter the credentials in correct format!')
             return False
            
    def get_input(self, Class):
        temp = dict()

        for i in self.types[Class]:
            temp[i] = input('Enter the {}: '.format(i))

        return temp

    def validate(self, temp, Class):
        flag = True

        for i in temp.keys():
            if(temp[i] != config[Class][i]):
                flag = False

        if(flag):
            print('Order placed successfully')
        else:
            print('Error occurred')
            #raise Exception('Authentication failed')

#Inheritance
class Card(Payment): #Uppercase
    credential = ''

    def __init__(self):
        self.credential = self.get_input('Card')

    def reg_check(self, credential):
        enterDate = credential['date']
        d, m, y = enterDate.split('/')
        enterDate = datetime.datetime(int(y), int(m), int(d))
        if(not (enterDate > datetime.datetime.today())):
            print('Your card expired')
            return False
        else:
            if(len(credential['number']) != 19):
                print('Invalid card number')
                return False
            if(len(credential['cvv']) != 3):
                print('Invalid CVV')
                return False
        return True

    def initiate(self):
        if(self.reg_check(self.credential)):
            self.validate(self.credential, 'Card')

class NetBanking(Payment):
    credential = ''
    def initiate(self):
        ip = input('Do you want to redirect?\n Yes/No: ')
        if(ip.lower() == 'yes'):
            self.credential = self.get_input('NetBanking')
            if(self.type_validate(self.credential)):
                self.validate(self.credential, 'NetBanking')
            else:
                self.initiate()

class Wallet(Payment):
    credential = ''
    index = 0
    Wallet = {'GPay': 'abc',
              'PhonePay': 'abc',
              'Paytm': 'abc'
             }

    def __init__(self, index): #keep it in initiate()
        self.index = index
        self.credential = self.get_input('Wallet')
        self.type_validate(self.credential)
        
    def reg_validate(self):
        if(re.search('@+{0}'.format(self.Wallet[self.index]), self.credential['upi id'])):
            return True
        else:
            return False

    def initiate(self):
        if(self.reg_validate):
            self.validate(self.credential, self.index)

class Cod(Payment):
    def initiate(self):
        if(input('Do you want to place the order?\n Yes/No: ')):
            self.validate(self.get_input('Cod'), 'Cod')






            
