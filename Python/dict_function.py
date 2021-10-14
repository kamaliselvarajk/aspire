d = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
print(d)
d1 = dict.copy(d)
print(d1)
key = dict.keys(d)
print(key)
value = dict.values(d)
print(value)
item = dict.items(d)
print(item)
str = 'Kamali'
ch = 'Character'
new = dict.fromkeys(str, ch)
print(new)
num = [10,20,30,40,50]
ip = 'Number'
new1 = dict.fromkeys(num, ip)
print(new1)
print(d.get(2))
print(d.pop(3))
print(d)
print(d.popitem())
print(d.setdefault(6))
print(d)
print(d.setdefault(7, 'Kamali'))
print(d)
t = {10:'Hi', 11:'Hello'}
d.update(t)
print(d)