a = [1,3,5,7]
b = [2,4,6,8]

#o/p -- [1,2,3,4,5,6,7,8]
print('Input\na', a,'\nb',b)
c = a + b
c.sort(reverse=True)
print('Output\nc',c)
print('-----------------------------------------------')

a = [1,2,3,4,5,6,7,8]
print('Input\na', a)
#o/p -- [1,8,3,6,5,4,7,2]
b = []
for i in range(len(a)):
    if(i%2 != 0):
        b.append(a[i])
for i in range(len(a)):
    if(i%2 != 0):
        a[i] = b.pop()

print('Output\na',a)
'''print('-----------------------------------------------')

a = list(input('Enter the expression: '))
open, close = 0, 0
for i in range(len(a)):
    if a[i] == '(':
        open = open + 1
    elif a[i] == ')':
        close = close + 1    

if open == close:
    print(True)
else:
    print(False) '''
print('-----------------------------------------------')

a = [1.3, 2, 6.8, 5]
#o/p -- [5, 6.8, 2, 1.3]
print('Input\n', a)
l = len(a) - 1 
b = []
for i in range(len(a)): 
    b.append(a[l])
    l = l - 1
print('Output\n', b)   
print('-----------------------------------------------') 

'''string = 'ABCDE'
print('Input\n', string)
s = list(string) 
x = []
n = int(input('Enter a number'))
while s != []:
    x += s[-n:]
    del s[-n:]
print('Output\n',''.join(x))  '''
print('-----------------------------------------------') 

import random
def fun():
    a = [2,3,4,1,5,5]
    b = a.copy()   
    sum1, sum2 = 0, 0 
    ind1, ind2 = [], []  
    for i in range(int(len(a)/2)):
        x = random.choice(b) 
        sum1 += x
        b.remove(x)
        ind1.append(x)
    for i in range(int(len(a)/2)):
        x = random.choice(b) 
        sum2 += x
        b.remove(x)
        ind2.append(x) 
    if sum1 == sum2:
        print(ind1, ind2)
    else:
        fun() 
fun()    
print('-----------------------------------------------') 

a = 'Hi Kamali! How are you?'
b = ' '
x = a.split(' ')
print(b.join(a.split(' ')[::-1]))
print(a[::-1]) 
print('-----------------------------------------------') 

print('10'.isnumeric())
print('10'.isdigit())
print('This is great'.split(' '))
print('This is great'.partition(' '))
print('This is great'.replace('ist', 'hiw'))
mapping = str.maketrans("ist", "hiw")
print("This is great".translate(mapping))
print('-----------------------------------------------') 


