def sum(a,b,c):
    d = a + b + c
    print('Sum of', a, ',', b, ',', c, 'is', d)
sum(10,20,30)
print('---------------------------------------------------------')
def sum(a,b,c):
    d = a + b + c
    return d
total = sum(12,23,34)
print('Total sum is', total)
print('---------------------------------------------------------')
def avg(a,b,c,d,e):
    avr = (a + b + c + d + e) / 5
    return avr
average = avg(99, 86, 100, 100, 100)
print('Average mark is', average)
print('---------------------------------------------------------')
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, ' ')
        a, b = b, a+b
fib(10)
print('---------------------------------------------------------')
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
fibonacci = fib(15)
print(fibonacci)
print('---------------------------------------------------------')
