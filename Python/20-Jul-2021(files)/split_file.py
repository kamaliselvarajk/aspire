with open('file.txt', 'r') as f:
    data = f.readlines()
    print(data)
    for line in data:
        print(line)
        op = line.split()
        print(op)
        print()
