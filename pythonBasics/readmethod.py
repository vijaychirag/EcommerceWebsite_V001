file = open('test.txt')

#print(file.read())
B
#print(file.readline())

# by using while loop through iterate readline method:
'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()'''

# create test.txt file > save test.txt file in object > again save, saved obj into another variable

# By using for loop through iteration
for line in file.readlines():
    print(line)