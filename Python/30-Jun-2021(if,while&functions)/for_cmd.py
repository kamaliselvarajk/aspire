>>> a=[[1,2,3], ['Kamali', 'Dharshu', 'Papu']]
>>> for i in a:
...     print(i, len(i))
...
[1, 2, 3] 3
['Kamali', 'Dharshu', 'Papu'] 3
>>> a=[[1,2,3], ['Kamali', 'Dharshu', 'Papu'], 'Aspire']
>>> for i in a:
...     print(i, len(i))
...
[1, 2, 3] 3
['Kamali', 'Dharshu', 'Papu'] 3
Aspire 6
>>> for i in 'Kamali S':
...     print(i)
...
K
a
m
a
l
i

S
>>> sum=0
>>> for i in range(11):
...     sum=sum + i
... print('Total sum is: ',sum)
  File "<stdin>", line 3
    print('Total sum is: ',sum)
    ^
SyntaxError: invalid syntax
>>> sum=0
>>> for i in 'Kamali S':
...     print(i, len(i))
...
K 1
a 1
m 1
a 1
l 1
i 1
  1
S 1
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(1,11,2))
[1, 3, 5, 7, 9]
>>> list(range(3,31,3))
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> list(range(3,31,-2))
[]
>>> list(range(3,31,-1))
[]
>>> list(range(3,31,-10))
[]
>>> list(range(-3,-31,-1))
[-3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30]
>>> list(range(-5,-100,-10))
[-5, -15, -25, -35, -45, -55, -65, -75, -85, -95]
>>> sum(range(1,6))
15
>>> sum(range(1,7,2))
9
