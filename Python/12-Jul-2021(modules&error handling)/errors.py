>>> while true
  File "<stdin>", line 1
    while true
              ^
SyntaxError: invalid syntax
*******************************************************************
>>> while true:
... print('Hi')
  File "<stdin>", line 2
    print('Hi')
    ^
IndentationError: expected an indented block
*******************************************************************
>>> while true:
...     print('Hi')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
*******************************************************************
>>> a = 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
*******************************************************************
>>> a = 2 + 'Kamali'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
*******************************************************************
