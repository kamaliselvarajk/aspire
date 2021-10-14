>>> import os
>>> os.getcwd()
'C:\\Users\\kamali.selvaraj'
>>> import glob
>>> glob.glob('*.py')
[]
>>> import sys
>>> print(sys.argv)
['']
>>> sys.stderr.write('Error occured!')
14
Error occured!
>>> import re
>>> re.findall(r'\bf[a-zA-Z]*', 'food fast and fest')
['food', 'fast', 'fest']
>>> re.findall(r'\bfo[a-zA-Z]*', 'food fast and fest')
['food']
>>> 'All is good'.replace('good', 'well')
'All is well'
>>> import math
>>> math.log(1024,2)
10.0
>>> math.log(165,2)
7.366322214245815
>>> math.cos(300)
-0.022096619278683942
>>> import random
>>> random.randrange(10)
8
>>> random.randrange(10)
3
>>> random.random()
0.7410243423763114
>>> random.random()
0.6491141325336172
>>> import statistics
>>> a = [23,12,45,23.4,67.2,76,91.5]
>>> statistics.mean(a)
48.3
>>> statistics.median(a)
45
>>> statistics.variance(a)
929.9033333333333
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2021, 7, 19)
>>> curr_yr = date.today().year
>>> curr_yr
2021
>>> curr_month = date.today().month
>>> curr_month
7
>>> date.today().day
19
>>> import zlib
>>> s = b'Python is a open source interpreted language'
>>> len(s)
44
>>> t = zlib.compress(s)
>>> len(t)
52
>>> zlib.decompress(t)
b'Python is a open source interpreted language'




