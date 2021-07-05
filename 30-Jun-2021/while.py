print('1)Addition of first 5 numbers')
i = 1; sum = 0;
while(i<=5):
    sum = sum + i
    i = i + 1
print('Addition of first 5 numbers is', sum)
print('--------------------------------------------------')
print('2)Addition of first 5 even numbers')
i = 1; sum = 0;
while(i<=10):
    if(i%2==0):
        sum = sum + i
    i = i + 1
print('Addition of first 5 even numbers is', sum)
print('--------------------------------------------------')
