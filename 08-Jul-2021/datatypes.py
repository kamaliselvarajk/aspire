print('1)None Type')
a = type(None)
print(a)
print(None==False)
print(None==True)
print(None==0)
print(None==10)
print(None=='Kamali')
print(None==None)
a = None
b = None
print(a==b)
print('******************************************************')
print('******************************************************')
print('2)Numeric Type')
print('2.1)Integer')
a = 10
b = -2.5
print(a,',', b)
n = 0o6         #Ocatal to integer
print(n)
n = 0O65
print(n)        #Hexadecimal to integer  
n = 0x9DA
print(n)
n = 0X5CF
print(n)
n = 0b0101      #Binary to integer
print(n)
n = 0B100101001
print(n)
n = oct(15)     #Integer to octal
print(n)
n = hex(123)    #Integer to hexadecimal    
print(n)
n = bin(22)     #Integer to binary
print(n)
print('******************************************************')
print('2.2)Floating point numbers')
n = 9.13
print(n)
n = 52.56e2     #e signifies 10th power
print(n)
print('******************************************************')
print('2.3)Complex numbers')
n = 5 + 6j
m = 2 + 12j
print(n+m)
n = 5.6 + 2.3j
m = 1.2 + 3.4j
print(n+m)
print('******************************************************')
print('2.4)Conversion of number types')
n = int(10.23)      #float to int
print(n)
n = float(25)       #int to float
print(n)
n = complex(15)     #int to complex
print(n)
n = complex(10.23)  #float to complex
print(n)
n = complex(5,6)
print(n)
print('******************************************************')
print('2.5)Boolean')
print(2==2)
print(2==2.0)
print(2==3)
print('******************************************************')
print('******************************************************')
print('3)Sequences')
print('3.1)String')
n = 'Kamali'
print(n)
print(n[0])
print(n[-4])
print(n[:])
print(n[1:4])
print(n[-6:-3])
print(n[0::2])
print(n[:] + 'Selvaraj')
print(type(n))
a = 'Kamali'
b = 'Aspire'
print('I am %s working in %s' %(a,b)) #string formatting operator
print('******************************************************')
print('3.2)List')
list = ['a', 'b', 'c']
print(list)
print(type(list))
print('******************************************************')
print('3.3)Tuple')
a = 1,
print(a)
print(type(a))
a = (1,2,3,4)
print(a)
print('******************************************************')
print('3.4)Range')
a = range(10)
print(a)
for i in a:
    print(i, end=" ")
print('******************************************************')
print('******************************************************')
print('4)Set')
city = set(('Chennai', 'Bangalore', 'Hyderabad', 'Chennai'))
print(city)
print(type(city))
print('******************************************************')
print('******************************************************')
print('5)Mapping(Dictionary)')
dict = {"name":'Kamali', 'domain':'Python', "position":'Trainee', 'joining year':2021}
print(dict)


print(type(dict))
