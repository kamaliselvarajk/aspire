>>> print('''
... User details
...     Name                    Kamali          User
...     Surname                 Selvaraj        Father
...     Mail id                 kamalishwetha   Personal
...                             Kamali.selvaraj Aspire
... ''')

User details
        Name                    Kamali          User
        Surname                 Selvaraj        Father
        Mail id                 kamalishwetha   Personal
                                Kamali.selvaraj Aspire

>>> print('''\
...     Name                    Kamali                  User
...     Surname                 Selvaraj                Father
...     Mail id                 kamalishwetha           Personal
...                             Kamali.selvaraj         Aspire
... ''')
        Name                    Kamali                  User
        Surname                 Selvaraj                Father
        Mail id                 kamalishwetha           Personal
                                Kamali.selvaraj         Aspire

>>> 'Kamali' + ' Selvaraj'
'Kamali Selvaraj'
>>> 'ba' + 2 * 'na'
'banana'
>>> 'ba' + 'na' * 2
'banana'
>>> 'ba' * 2 * 'na'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> 'ba' * 2 + 'na'
'babana'
>>> 'ba'  'na'  'na'
'banana'
>>> s='ba' + 2 * 'na'
>>> print s
  File "<stdin>", line 1
    print s
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> Yes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Yes' is not defined
>>> print(s)
banana
>>> text=('Kamali is a daughter of Selvaraj'
...       'Selvaraj is a father of Kamali')
>>> print(text)
Kamali is a daughter of SelvarajSelvaraj is a father of Kamali
>>> a='Kamali'
>>> b='Selvaraj'
>>> c = a + b
>>> print(c)
KamaliSelvaraj
>>> c = a + 'Shwetha'
>>> print(c)
KamaliShwetha
>>> a 'Shwetha'
  File "<stdin>", line 1
    a 'Shwetha'
      ^
SyntaxError: invalid syntax
>>> a + 'Shwetha'
'KamaliShwetha'
>>> a='KamaliSelvaraj'
>>> a[0]
'K'
>>> a[-10]
'l'
>>> a[-14]
'K'
>>> a[13]
'j'
>>> a[16]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> a[-0]
'K'
>>> a[1:7]
'amaliS'
>>> a[0:6]
'Kamali'
>>> a[0:-5]
'KamaliSel'
>>> a[5:-12]
''
>>> a[10:-13]
''
>>> a[0::6]
'KSa'
>>> a[0::3]
'KaSva'
>>> a[:6]
'Kamali'
>>> a[6:13]
'Selvara'
>>> a[6:]
'Selvaraj'
>>> a[:]
'KamaliSelvaraj'
>>> a[::2]
'KmlSlaa'
>>> a[::-2]
'jrveiaa'
>>> s='Kamali Selvaraj'
>>> s[4:16]
'li Selvaraj'
>>> s[4:32]
'li Selvaraj'
>>> s[6]='S'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> len(s)
15
>>> len(a)
14