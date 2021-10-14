'''a = [1,2,3,4,5,6,7,8,9,10]
#O/P: 1,4,7,10

b = a[0::3]
print(b)
for i in range(0, len(a), 3):
        print(i)

a = [1,2,3,4,5,6,7,8,9,10]
b = [x*2 for x in a if x%2==0 else x**2]'''

a = -5**2+34>6+8/2*3
'''25 + 34>6+4*3
25 + 34>6 + 12
59>18'''
print(a)
print(-5**2)

a = 52.0478
b = 9
c = str(a).zfill(b)
print(c)