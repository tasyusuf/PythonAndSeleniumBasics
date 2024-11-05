values = [1, 2, "yusuf", 4, 5] #List is datatype that allows multiple values and can be different datatypes

print(values)

print(values[0])
print(values[3])
print(values[-1]) #last index returned
print(values[1:3]) #index 1 to 3 (3 is excluded)

values.insert(3, "Tas") #insert Tas in index 3
print(values)

values.append("End") #put the value at the end
print(values)

values[2] = "YUSUF" #update value
print(values)

del values[0] # delete index 0
print(values)



val = (1, 2, "Yusuf", 4.5) #tuple. It is immutable. List is not immutable.

print(val[1])

#val[2] = "YUSUF" #'tuple' object does not support item assignment error

print(val)

#Dictionary

dic = {"a":2, 4:"bcd", "c":"Hello"}

print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Yusuf"
dict["lastname"] = "Tas"

print(dict)
