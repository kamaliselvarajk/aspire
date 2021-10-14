f = open("file.txt", "a")
f.write("This content is added dynamically!")
f.close()

f = open("file.txt", "w")
f.write("New content!")
f.close()

f = open('file.txt', 'r')
print(f.read())
