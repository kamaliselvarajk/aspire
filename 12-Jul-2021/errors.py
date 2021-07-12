>>> while true
  File "<stdin>", line 1
    while true
              ^
SyntaxError: invalid syntax
>>> while true:
... print('Hi')
  File "<stdin>", line 2
    print('Hi')
    ^
IndentationError: expected an indented block
>>> while true:
...     print('Hi')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
