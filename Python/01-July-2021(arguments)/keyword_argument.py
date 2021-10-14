print('Program for keyword arguments')
def fun(a, b):
    print("Value of a and b before swapping")
    print(a, b)
    a, b = b, a
    print("Value of a and b after swapping")
    print(a, b)
fun(a=10, b=20)
