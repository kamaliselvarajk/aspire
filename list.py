>>> a=['c', 'python', 'java', 'html', 'css', 'php']
>>> print(a)
['c', 'python', 'java', 'html', 'css', 'php']
>>> print(a, end = '\n')
['c', 'python', 'java', 'html', 'css', 'php']
>>> x = 'mysql'
>>> a.append(x)
>>> print(a)
['c', 'python', 'java', 'html', 'css', 'php', 'mysql']
>>> a.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count(python)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> a.count('python)
  File "<stdin>", line 1
    a.count('python)
                    ^
SyntaxError: EOL while scanning string literal
>>> a.count('python')
1
>>> len(a)
7
>>> for x in a:
...     print(x, a[x])
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: list indices must be integers or slices, not str
>>> a.insert(0,c++)
  File "<stdin>", line 1
    a.insert(0,c++)
                  ^
SyntaxError: invalid syntax
>>> a.insert(0,js)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'js' is not defined
>>> a.insert(0,'js')
>>> print(a)
['js', 'c', 'python', 'java', 'html', 'css', 'php', 'mysql']
>>> x = 'c++'
>>> a.insert(4,x)
>>> print(a)
['js', 'c', 'python', 'java', 'c++', 'html', 'css', 'php', 'mysql']
>>> a.remove('c++')
>>> print(a)
['js', 'c', 'python', 'java', 'html', 'css', 'php', 'mysql']
>>> a.remove('c++')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> a.append('python')
>>> print(a)
['js', 'c', 'python', 'java', 'html', 'css', 'php', 'mysql', 'python']
>>> a.index('python')
2
>>> a.index('python',2)
2
>>> a.index('python', 3)
8
>>> a.index('java', 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'java' is not in list
>>> print(a)
['js', 'c', 'python', 'java', 'html', 'css', 'php', 'mysql', 'python']
>>> a.reverse()
>>> a
['python', 'mysql', 'php', 'css', 'html', 'java', 'python', 'c', 'js']
>>> a.sort()
>>> print(a)
['c', 'css', 'html', 'java', 'js', 'mysql', 'php', 'python', 'python']
>>> a.pop('js')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(4)
'js'
>>> print(a)
['c', 'css', 'html', 'java', 'mysql', 'php', 'python', 'python']
>>> x = a.copy()
>>> print(x)
['c', 'css', 'html', 'java', 'mysql', 'php', 'python', 'python']
>>> a.clear()
>>> a
[]
>>> print(a[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(x[3])
java
>>> print(a[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(x[-3])
php
>>> x.extend()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.extend() takes exactly one argument (0 given)
>>> x.extend(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> x.extend(iterable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'iterable' is not defined
>>> x.extend('js')
>>> print(x)
['c', 'css', 'html', 'java', 'mysql', 'php', 'python', 'python', 'j', 's']
>>> x.extend('abc')
>>> x
['c', 'css', 'html', 'java', 'mysql', 'php', 'python', 'python', 'j', 's', 'a', 'b', 'c']
>>> x.pop()
'c'
>>> x.extend(ds)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ds' is not defined
>>> x.pop
<built-in method pop of list object at 0x000001C946AF39C0>
>>> x.pop()
'b'
>>> x
['c', 'css', 'html', 'java', 'mysql', 'php', 'python', 'python', 'j', 's', 'a']
>>> x.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'popleft'
>>> from collections import deque
>>> x.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'popleft'
>>> new = ['python', 'css', 'html', 'java', 'c', 'php', 'css', 'python']
>>> new.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'popleft'
>>> new = deque(['python', 'html', 'css'])
>>> new.append('php')
>>> new
deque(['python', 'html', 'css', 'php'])
>>> new.append('python')
>>> new
deque(['python', 'html', 'css', 'php', 'python'])
>>> new.popleft()
'python'
>>> print(new)
deque(['html', 'css', 'php', 'python'])
>>> cubes = []
>>> for i in range(10):
...     cubes.append(i**3)
...
>>> print(cubes)
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> cubes = [i**3 for i in range(1,10)]
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 512, 729]
