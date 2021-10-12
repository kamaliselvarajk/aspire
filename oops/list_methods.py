a = [5, 6.5, 7, 5, 10, 5, 18, 5]
print('Reverse a list')
print(a[ ::-1])
print('--------------------')

print('Maximum occurrence element ')
print(max(a, key = a.count))
print('--------------------')

print('Minimum occurrence element ')
print(min(a, key = a.count))
print('--------------------')

print('2nd smallest element')
a.sort()
print(a[1])
print('--------------------')

print('append and maximum element')
a.append(65)
print(a)
print(max(a))
print('--------------------')

print('Copy and remove all element from list')
b = a.copy()
print(b)
b.clear()
print(b)
print('--------------------')

print('Append and extend')
x = (60,80,90)
a.append(x)
print(a)
a.extend(x)
print(a)
print('--------------------')

print('Index')
print(a.index(60))
print('--------------------')

print('Insert')
a.insert(1,4.5)
print(a)
print('--------------------')

print('Pop')
a.pop()
print(a)
a.pop(6)
print(a)
print('--------------------')

print('Remove')
a.remove(5)
print(a)
print('--------------------')

print('Reverse')
a.reverse()
print(a)
print('--------------------')

print('Ascending and descending order')
b = [23,55,6,1,90,12]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
print('--------------------')

print('Count')
print(a.count(5)) 
