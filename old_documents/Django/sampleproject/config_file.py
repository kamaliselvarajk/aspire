import configparser

config = configparser.ConfigParser()


config['Host'] = {  'url': 'http://127.0.0.1:8000/',
                    'username': 'kamali.selvaraj',
                    'password': '621317205022Sk#'
                }

config['Database'] = { 'NAME': 'django',
                       'USER': 'root',
                       'PASSWORD': '621317205022Sk#',
                       'HOST': 'localhost'

}


with open('config.ini', 'w') as configfile:
    config.write(configfile)