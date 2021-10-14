a=[[1,2,3], ['Kamali', 'Dharshu', 'Papu'], 'Aspire']
for i in a:
    print(i, len(i))
print('------------------------------------------')
sum = 0
for i in range(11):
    sum = sum + i
print('Sum of first 10 numbers is: ', sum)
print('------------------------------------------')
sum = 0
for i in range(11):
    if(i%2 == 0):
        sum = sum + i
print('Sum of first 5 even numbers is ',sum)
print('------------------------------------------')
for i in range(11):
    for j in range(2):
        sum = sum + i + j
print(sum)
print('------------------------------------------')
s = ['Python', 'PHP', 'Java', 'HTML', 'CSS', 'JS', 'MySql']
for i in range(len(s)):
    print(i, s[i], len(s[i]))
print('------------------------------------------')
for i in range(2,10):
    for j in range(2,i):
        if(i%j == 0):
            print(i, 'not a prime number')
            break
    else:
        print(i, 'is prime number')
print('-------------------------------------------')
for i in range(1,10):
    if(i%2 == 0):
        continue
    else:
        print(i)
print('-------------------------------------------')
