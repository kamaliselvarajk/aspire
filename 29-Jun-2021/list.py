>>> name = ['Kamali', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> name
['Kamali', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> print(name)
['Kamali', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> print name
  File "<stdin>", line 1
    print name
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name)?
>>> name[2]
'Vasantha'
>>> name[-2]
'Vasantha'
>>> name[1]
'Dharshini'
>>> name[-1]
'Selvaraj'
>>> name[0:3]
['Kamali', 'Dharshini', 'Vasantha']
>>> name[0:8]
['Kamali', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> name[-1:4]
['Selvaraj']
>>> name[-2:4]
['Vasantha', 'Selvaraj']
>>> name[4:-2]
[]
>>> name[:]
['Kamali', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> name[0]='Keerthi'
>>> print(name)
['Keerthi', 'Dharshini', 'Vasantha', 'Selvaraj']
>>> name + ['Papu']
['Keerthi', 'Dharshini', 'Vasantha', 'Selvaraj', 'Papu']
>>> len(name)
4
>>> new = name + ['Papu']
>>> len(new)
5
>>> print(new)
['Keerthi', 'Dharshini', 'Vasantha', 'Selvaraj', 'Papu']
>>> new.append('Kamali')
>>> print(new)
['Keerthi', 'Dharshini', 'Vasantha', 'Selvaraj', 'Papu', 'Kamali']
>>> len(new)
6
>>> new.pop()
'Kamali'
>>> print(new)
['Keerthi', 'Dharshini', 'Vasantha', 'Selvaraj', 'Papu']
>>> new.pop(2)
'Vasantha'
>>> print(new)
['Keerthi', 'Dharshini', 'Selvaraj', 'Papu']
>>> len(new)
4
>>> new.append('Vasantha')
>>> print(new)
['Keerthi', 'Dharshini', 'Selvaraj', 'Papu', 'Vasantha']
>>> len(new)
5
>>> new.pop(-3)
'Selvaraj'
>>> print(new)
['Keerthi', 'Dharshini', 'Papu', 'Vasantha']
>>> new(-3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> new[-3]
'Dharshini'
>>> new[0:-4]
[]
>>> new[0:-3]
['Keerthi']
>>> new[0::2]
['Keerthi', 'Papu']
>>> new[1:3] = []
>>> print(new)
['Keerthi', 'Vasantha']
>>> len(new)
2
>>> list = ['Aspire', [1,2,3,4,5], ['Kamali', 'Shwetha', 'Dharshu']]
>>> len(list)
3
>>> len(list[0])
6
>>> len(list[1])
5
>>> len(list[2])
3
>>> list[2][1]
'Shwetha'
>>> list[2][0] + list[0]
'KamaliAspire'
