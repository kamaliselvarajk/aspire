import os
f = open('create_file.txt', 'w')
f.write("New file created")
f.close()

#f = open('create_file.txt', 'r')
#print(f.read())
#f.close()

f = open('create_file.txt', 'a')
f.write('\nNew data appended')
f.close()

f = open('create_file.txt', 'r')
print(f.read())

#f = open('demofile.txt', 'x')
#f.close()

#deleting the file
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
    print('The demofile.txt file is deleted')
else:
    print("The file doesn't exists")
