class Calculator:
    num = 100
    #default constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num



obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.num)
print(obj.Summation())