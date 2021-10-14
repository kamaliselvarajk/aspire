import configparser

config = configparser.ConfigParser()

config['Card'] = {'number': '1111 1111 1111 1111',
                  'pin': '1234',
                  'cvv': '123',
                  'otp': '12345678'
                 }

config['NetBanking'] = {'username': 'sampleuser',
                        'password': '123'
                       }

config['GPay'] = {'UPI Id': 'kamali@abc',
                  'pin': '123'
                 }

config['Paytm'] = {'UPI Id': 'kamali@abc',
                   'pin': '123'
                  }

config['PhonePay'] = {'UPI Id': 'kamali@abc',
                   'pin': '123'
                  }


with open('config_ex.ini', 'w') as configfile:
    config.write(configfile)


