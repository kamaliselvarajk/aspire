 n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> n=1
>>> a=5,b=2
  File "<stdin>", line 1
    a=5,b=2
      ^
SyntaxError: cannot assign to literal
>>> n=1
>>> a=5
>>> b=2
>>> print(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> width=10
>>> height=2*3
>>> print(width*height)
60
>>> width+_
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_' is not defined
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> a+b
30
>>> a+ _
40
>>> a+_
50
>>> print('doesn\'t')
doesn't
>>> print('doesn't')
  File "<stdin>", line 1
    print('doesn't')
                 ^
SyntaxError: invalid syntax
>>> print("doesn't")
doesn't
>>> print('Hi Kamali \nWelcome to Aspire')
Hi Kamali
Welcome to Aspire
>>> s='Hi Kamali \nWelcome to Aspire'
>>> s
'Hi Kamali \nWelcome to Aspire'
>>>print(s)
Hi Kamali
Welcome to Aspire
>>> print('Hi \nname please')
Hi
name please
>>> print(r'Hi \nname please')
Hi \nname please
>>> print(r'Hi \name please')
Hi \name please
>>> print('Hi \name please')
Hi
ame please
