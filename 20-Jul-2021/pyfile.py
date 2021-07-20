f = open("file.txt", "r")
print(f.read())
print('*********************************************')

f = open("file.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print('*********************************************')

f = open("file.txt", "a")
f.write('This content is added dynamically!')
f.close()

f = open('file.txt', 'r')
f.read()

