file = open('test.txt')
#read all the contents of file
#print(file.read(6)) #if you specify parameter it will read first ... character

#read one single line
#print(file.readline())
#print(file.readline())


#print line by line using ReadLine method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

allText = file.readlines()
print(allText)

file.close()