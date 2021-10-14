>>> import reprlib
>>> reprlib.repr(set('kamali'))
"{'a', 'i', 'k', 'l', 'm'}"
>>> import pprint
>>> t = [[12,23,34], [54,32], [55,11,65,87], [90,76,22]]
>>> pprint.pprint(t, width=30)
[[12, 23, 34],
 [54, 32],
 [55, 11, 65, 87],
 [90, 76, 22]]
>>> pprint.pprint(t,width=10)
[[12,
  23,
  34],
 [54, 32],
 [55,
  11,
  65,
  87],
 [90,
  76,
  22]]
>>> import textwrap
>>> txt = 'Python is a open source interpreted language and it is compiled line by line, it is developed by Gudio Van Rossum in 1985 and he named it as python because he is a fan of Monty python flying circus'
>>> print(textwrap.fill(txt, width=40))
Python is a open source interpreted
language and it is compiled line by
line, it is developed by Gudio Van
Rossum in 1985 and he named it as python
because he is a fan of Monty python
flying circus
>>> print(textwrap.fill(txt, width=70))
Python is a open source interpreted language and it is compiled line
by line, it is developed by Gudio Van Rossum in 1985 and he named it
as python because he is a fan of Monty python flying circus
>>> from string import Template
>>> s = Template('${Name} is working in {company} for last $$4 months')
>>> s.substitute(Name='Kamali')
'Kamali is working in {company} for last $4 months'
>>> import logging
>>> logging.warning('Warning:There is a chance for occurrence of error')
WARNING:root:Warning:There is a chance for occurrence of error
>>> logging.error('Error occurred!')
ERROR:root:Error occurred!
>>> from array import array
>>> a = array([12,23,34,45,56])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array() argument 1 must be a unicode character, not list
>>> a = array('K', [12,23,34,45,56])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
>>> a = array('B', [12,23,34,45,56])
>>> sum(a)
170
>>> a[:4]
array('B', [12, 23, 34, 45])
>>> import bisect
>>> a = [100, 200, 400, 500]
>>> bisect.insort(a,(300))
>>> a
[100, 200, 300, 400, 500]
>>> bisect.insort(a,265)
>>> a
[100, 200, 265, 300, 400, 500]
>>> from heapq import heapify, heappop, heappush
>>> a = [3,1,5,2,7,6,9,0,7,8]
>>> heapify(a)
>>> a
[0, 1, 5, 2, 7, 6, 9, 3, 7, 8]
>>> heappush(a, -6)
>>> a
[-6, 0, 5, 2, 1, 6, 9, 3, 7, 8, 7]
>>> [heappop(a) for i in range(4)]
[-6, 0, 1, 2]
