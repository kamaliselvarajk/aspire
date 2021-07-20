f = open("file.txt", "a")
f.write("This content is added dynamically!")
f.close()

f = open('file.txt', 'r')
print(f.read())
