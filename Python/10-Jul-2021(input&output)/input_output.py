>>> name = 'Kamali'
>>> company = 'Aspire'
>>> F'{name} is working in {company}'
'Kamali is working in Aspire'
*****************************************************************
>>> name = 'Kamali'
>>> company = 'Aspire'
>>> print('{} is working in {}'.format(name, company))
Kamali is working in Aspire
*****************************************************************
>>> s = 'Hello World'
>>> str(s)
'Hello World'
>>> repr(s)
"'Hello World'"
*****************************************************************
>>> s = 22
>>> str(s)
'22'
>>> repr(s)
'22'
*****************************************************************
>>> hello = 'Hello World\n'
>>> print(hello)
Hello World

>>> hellon = repr(hello)
>>> print(hellon)
'Hello World\n'
*****************************************************************
>>> a = 10
>>> b = 20
>>> print(f'The sum is {a + b}')
The sum is 30
*****************************************************************
>>> a=20
>>> b=30
>>> repr((a, b, ('first', 'second')))
"(20, 30, ('first', 'second'))"
*****************************************************************
>>> import math
>>> print(f'The value of PI is {math.pi:.3f}.')
The value of PI is 3.142.
>>> import math
>>> print(f'The value of PI is {math.pi:.4f}.')
The value of PI is 3.1416.
*****************************************************************
>>> ages = {"A":25, 'B':33, 'C':30}
>>> for name, age in ages.items():
...     print(F'{name} => {age}')
...
A => 25
B => 33
C => 30
*****************************************************************
>>> name = 'Kamali'
>>> print(f'The name is {name}')
The name is Kamali
>>> print(f'The name is {name!r}')
The name is 'Kamali'
*****************************************************************
>>> print('{0} and {1}'.format('a' , 'b'))
a and b
>>> print('{1} and {0}'.format('a', 'b'))
b and a
*****************************************************************
>>> print('{first}, {1}, {optional}'.format(optional = 'c', 'b', first = 'a'))
  File "<stdin>", line 1
    print('{first}, {1}, {optional}'.format(optional = 'c', 'b', first = 'a'))
                                                                            ^
SyntaxError: positional argument follows keyword argument
*****************************************************************
>>> print('{0}, {1}, {optional}'.format('a', 'b', optional = 'c'))
a, b, c
*****************************************************************
>>> for i in range(1,150,50):
...     print(repr(i).rjust(5), end = '\n')
...
    1
   51
  101
*****************************************************************
>>> '65'.zfill(5)
'00065'
>>> 'ab'.zfill(5)
'000ab'
>>> '3.14'.zfill(7)
'0003.14'
>>> '3.14'.zfill(9)
'000003.14'
*****************************************************************
# Interpolation
>>> print('The value of PI is %2.3f' % math.pi)
The value of PI is 3.142
>>> print('The value of PI is %0.1f' % math.pi)
The value of PI is 3.1
>>> print('The value of PI is %5.4f' % math.pi)
The value of PI is 3.1416
*****************************************************************
