def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i] #yield is for returnng the data
for c in reverse('Kamali'):
    print(c)
