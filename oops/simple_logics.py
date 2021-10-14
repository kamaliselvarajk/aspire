print('Swap first an last element')
x = [12,23,35,56,68]
print(x)
x[0], x[len(x)-1] = x[len(x)-1], x[0]
print(x)
