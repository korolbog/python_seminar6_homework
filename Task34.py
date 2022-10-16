path = 'Task33_file1.txt'
x = open(path, 'r')
for line in x:
    print(line)
x.close()


path = 'Task33_file2.txt'
y = open(path, 'r')
for line in y:
    print(line)
y.close()